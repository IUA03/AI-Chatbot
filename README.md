# AI Chatbot

This is a Flask-based AI chatbot that uses a trained neural network model to understand user input and return contextually relevant responses. The chatbot uses natural language processing (NLP) techniques to classify intents from user messages.

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

<video controls width="100%">
  <source src="https://github.com/IUA03/AI-Chatbot/raw/main/Demo/demo%20video.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

---

