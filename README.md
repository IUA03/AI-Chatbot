# AI Chatbot

This is a Flask-based AI chatbot that uses a trained neural network model to understand user input and return contextually relevant responses. The chatbot uses natural language processing (NLP) techniques to classify intents from user messages.

---

## 📁 Custom Dataset

This project was built entirely from scratch, without relying on any pre-existing datasets or external APIs. All of the training data, including intents, patterns, and responses, was created manually to ensure full control and ownership of the dataset.

By starting from the ground up, the model is trained on data that’s specifically tailored to the project’s needs. This helps ensure the chatbot is perfectly aligned with the intended use case, leading to more accurate and effective results.

---

## 🔧 Features

* Frontend: HTML template for chat UI
* Backend: Flask API for handling messages
* Model: Pre-trained Keras model for intent classification
* JSON-based intent training data
* Utility script to enrich patterns for better training
* Demo folder with an output video showcasing chatbot usage

---

## 🗂️ Project Structure

```
├── app.py                    # Flask backend
├── convertintosmaller.py     # Script to generate more training patterns
├── intents.json             # Original training data
├── main.py                  # Script to train or run the model
├── utils.py                 # Utility functions for predictions
├── model/
│   ├── chatbot_model.keras  # Trained Keras model
│   ├── classes.pkl          # Encoded classes
│   ├── words.pkl            # Encoded words
│   └── intents.json         # Backup or training-time intents file
├── templates/
│   └── index.html           # Frontend chat UI
├── Demo/
│   └── demo video.mp4           # Chatbot output video 
```

---

## ⚙️ How to Run

1. Clone the repository

```bash
git clone https://github.com/IUA03/AI-Chatbot.git
cd AI-Chatbot
```

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app

```bash
python app.py
```

4. Open your browser and go to `http://127.0.0.1:5000/`

---

## 🧠 About `convertintosmaller.py`

This script enriches the training dataset by creating multiple versions (lowercase, uppercase, title case, etc.) of each input pattern. This helps improve model accuracy without manually adding repetitive data.

Run with:

```bash
python convertintosmaller.py
```

---

## 🎥 Demo Video

https://github.com/user-attachments/assets/ad9ef65e-69c6-4133-8e9d-531f303589a3

---

