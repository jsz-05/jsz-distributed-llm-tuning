# First, set up API and all authentications to be able to use tuned models

import os
import google.generativeai as genai
from load_creds import load_creds, load_iam_creds
from relevancy_processor import preprocess_text, get_relevant_passages

# Load credentials
creds = load_iam_creds()

# Configure generative AI with credentials
genai.configure(credentials=creds)
print()
print('Available base models:', [m.name for m in genai.list_models()])
print()
print('Available tuned models:')
try:
    tuned_models = genai.list_tuned_models()
    for i, model in enumerate(tuned_models):
        print(model.name)
        if i >= 4:  # Limit to first 5 models
            break
except Exception as e:
    print(f"Error listing tuned models: {e}")


# Below is a quick implementation for deploying our tuned model. I will create a Flask application and web interface, then connect the backend to our tuned Gemini model.
# I've implemented two routes for now, which is all a chatbot really needs. I've included '/' for the main page, and '/chat' for handling chat message requests.

from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

@app.route('/')
def distributed_chatbot():
    return render_template('chatbot.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')
    # Here you would integrate the logic for processing the user message and generating a response.
    # For demonstration purposes, we'll return a dummy response.
    bot_response = "This is a placeholder response."
    return jsonify(response=bot_response)

if __name__ == '__main__':
    app.run(debug=True)

import google.generativeai as genai

app = Flask(__name__)

# We can change which model to use later on
# model_name = 'generate-num-optimized'
model_name = 'distributed-fast-mixed'

model = genai.GenerativeModel(model_name=f'tunedModels/{model_name}')
reference_file_path = 'qa_datasets/reference.txt'

@app.route('/')
def distributed_chatbot():
    return render_template('chatbot.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json['message']
    if os.path.exists(reference_file_path):
        with open(reference_file_path, 'r') as file:
            reference_material = file.read()
    else:
        print(f"Warning: Reference file '{reference_file_path}' not found.")
        reference_material = ""
    
    # Get relevant passages
    relevant_passages = get_relevant_passages(user_input, reference_material)
    
    # Create the full prompt
    full_prompt = f"""
    MY PROMPT:
    {user_input}

     Relevant Reference Material: 
    {"".join(relevant_passages)}

     RULES: 
     First, If I ask or say anything not loosely related to distributed computing or computer science, reply with "I am an LLM trained to answer questions for CS142 only."
     If my prompt is a greeting, reply introducing yourself as a CS142 help chatbot.
     
     Pretend you are an computer science professor with tons of experience in distributed computing and CS theory.
     Please always try and reference the text material provided to help answer the prompt question in paragraph format. 
     Your answer should ALWAYS be detailed and easy to understand, with 3 sentences MINIMUM. 
     If the question topic/answer/clarification request isn't specified in the reference material, DRAW UPON YOUR OWN KNOWLEDGE, and add (test_metric:ext) at the end of your response. 
     WHATEVER YOU DO, PLEASE DO NOT LEAVE ME WITHOUT AN ANSWER. Otherwise if you used info from the reference, put (test_metric:ref) at the end. 
     If I ask for clarification, please do a quick recap of your previous answer, and feel free to use your own knowledge as a supplement to give the best, most clear, and easiest to understand follow up. 
    """
    
    # Generate response using the model
    result = model.generate_content(full_prompt)
    
    return jsonify({'response': result.text})


if __name__ == '__main__':
    app.run(debug=True)