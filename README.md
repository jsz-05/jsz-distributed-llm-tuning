# [LLM Fine-tuning for Distributed Computing](https://jsz.pythonanywhere.com/)

This repository contains the code and documentation I have created for training and deploying a chatbot for use in CS142, Distributed Computing at Caltech. The chatbot in it's current work in progress state can be accessed [here.](https://jsz.pythonanywhere.com/)
## Tuning the Model

### Data Collection
A simple web scraper was implemented to create a rough dataset from the course website. This dataset includes questions and answers, as well as text data from the website that were used to train the model. NOTE: work is being done to greatly improve the performance of the chatbot, including testing various base LLMs, dataset cleaning/optimization, and prompt engineering.

The data is currently stored in 4 formats:
- `distributed_complex.csv`: This contains complex questions generated from the course content which prompt about specific concepts and details.
- `distributed_simple.csv`: This contains simpler questions generated from the course content which can usually be answered with 1-2 sentences.
- `distributed_mixed.csv` : A mix of the above two datasets
- `reference.txt`: A text file containing 

### Model Used
The model used for this project is Gemini 1.0 Pro, one of Google's older flagship models. The training and tuning were done using Google's API, and Google Cloud Console was used for compute/storage. 

### Training Process
- **Initial Test:** I performed an initial test (`gemini_optimized.ipynb`) using default parameters, which showed that the learning process very was fast.
- **Tuning:** After tuning based on the initial test in (`gemini_fast_mixed.ipynb`), I achieved a mean loss of ~0.4% at only 15 epochs. The LLM was able to learn very well even with the rough dataset.

### Results
The results of the tuning process were very promising, showing that the model could efficiently learn from the provided dataset. Even better results can be achieved by further scrutinizing the training data set for anomolies.

## Costs and Deployment

All resources, including the model, compute resources, and infrastructure, were handled by Google Cloud Console. For deployment, I wrote a Flask application for the backend and designed a simple frontend interface for the chatbot. To avoid paying for Google's cloud hosting, I integrated the chatbot as a subpage on my portfolio , and hosted the app via Pythonanywhere.

You can access the chatbot here: [https://jsz.ext.io/chatbot](https://jsz.pythonanywhere.com/)


For any questions or suggestions, feel free to open an issue or contact me directly at [jsz@caltech.edu](mailto:jsz@caltech.edu).

---
