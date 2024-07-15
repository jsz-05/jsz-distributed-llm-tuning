from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import re

def preprocess_text(text):
    # Convert to lowercase and remove punctuation
    return re.sub(r'[^\w\s]', '', text.lower())

def get_relevant_passages(question, reference_text, num_passages=5, passage_length=300, overlap=100):
    # Preprocess the question and reference text
    processed_question = preprocess_text(question)
    processed_reference = preprocess_text(reference_text)
    
    # Create overlapping passages
    passages = []
    for i in range(0, len(processed_reference) - passage_length + 1, passage_length - overlap):
        passages.append(processed_reference[i:i+passage_length])
    
    # If there are fewer passages than requested, adjust num_passages
    num_passages = min(num_passages, len(passages))
    
    # Create TF-IDF vectors
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(passages + [processed_question])
    
    # Calculate cosine similarity between question and passages
    cosine_similarities = cosine_similarity(tfidf_matrix[-1], tfidf_matrix[:-1]).flatten()
    
    # Get indices of top similar passages
    top_passage_indices = cosine_similarities.argsort()[-num_passages:][::-1]
    
    # Sort indices to maintain original text order
    top_passage_indices = sorted(top_passage_indices)
    
    # Return original (non-processed) passages
    relevant_passages = []
    for i in top_passage_indices:
        start = i * (passage_length - overlap)
        end = start + passage_length
        relevant_passages.append(reference_text[start:end])
    
    return relevant_passages

def combine_passages(passages, max_length=2000):
    combined = " ".join(passages)
    if len(combined) > max_length:
        return combined[:max_length]
    return combined


# from sklearn.feature_extraction.text import TfidfVectorizer
# from sklearn.metrics.pairwise import cosine_similarity
# import re

# def preprocess_text(text):
#     # Convert to lowercase and remove punctuation
#     return re.sub(r'[^\w\s]', '', text.lower())

# def get_relevant_passages(question, reference_text, num_passages=3, passage_length=200):
#     # Preprocess the question and reference text
#     processed_question = preprocess_text(question)
#     processed_reference = preprocess_text(reference_text)
    
#     # Split the reference text into passages
#     passages = [processed_reference[i:i+passage_length] for i in range(0, len(processed_reference), passage_length)]
    
#     # Create TF-IDF vectors
#     vectorizer = TfidfVectorizer()
#     tfidf_matrix = vectorizer.fit_transform(passages + [processed_question])
    
#     # Calculate cosine similarity between question and passages
#     cosine_similarities = cosine_similarity(tfidf_matrix[-1], tfidf_matrix[:-1])
    
#     # Get indices of top similar passages
#     top_passage_indices = cosine_similarities.argsort()[0][-num_passages:][::-1]
    
#     # Return original (non-processed) passages
#     return [reference_text[i*passage_length:(i+1)*passage_length] for i in top_passage_indices]
