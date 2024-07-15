# [CS142 Distributed Computing Chatbot](https://jsz.ext.io/chatbot)

This repository contains the code and documentation I have created for training and deploying a chatbot for use in CS142, Distributed Computing at Caltech. The chatbot in it's current work in progress state can be accessed [here.](https://jsz.ext.io/chatbot)
## Tuning the Model

### Data Collection
I started by using a web scraper to create a rough dataset from a website. This dataset includes questions and answers that were used to train the model.

### Model Used
The model used for this project is Gemini 1.0 Pro, one of Google's older flagship models. The training and tuning were done using Google's API, and Google Cloud Console was used for compute/storage. 

### Training Process
- **Initial Test:** I performed an initial test (`gemini_optimized.ipynb`) using default parameters, which showed that the learning process very was fast.
- **Tuning:** After tuning based on the initial test in (`gemini_fast_mixed.ipynb`), I achieved a mean loss of ~0.4% at only 15 epochs. The LLM was able to learn very well even with the rough dataset.

### Results
The results of the tuning process were very promising, showing that the model could efficiently learn from the provided dataset.

## Costs and Deployment

All resources, including the model, compute resources, and infrastructure, were handled by Google Cloud Console. For deployment, I wrote a Flask application for the backend and designed a simple frontend interface for the chatbot. To avoid paying for Google's cloud hosting, I hosted the chatbot as a subpage on my portfolio website.

You can access the chatbot here: [https://jsz.ext.io/chatbot](https://jsz.ext.io/chatbot)


For any questions or suggestions, feel free to open an issue or contact me directly at [jsz@caltech.edu](mailto:jsz@caltech.edu).

---
