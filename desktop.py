import os
import json
import pickle
import numpy as np
import nltk
from nltk.stem import WordNetLemmatizer
import tkinter as tk
from tkinter import Scrollbar


import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

import random


from tensorflow.keras.models import load_model



# Load necessary files
lemmatizer = WordNetLemmatizer()
print("Current Working Directory:", os.getcwd())
print("File Exists:", os.path.exists("intents.json"))

with open(r"intents.json", "r") as file:
    intents = json.load(file)

words = pickle.load(open(r"model\words.pkl", "rb"))
classes = pickle.load(open(r"model\classes.pkl", "rb"))
model = load_model(r"model\chatbot_model.keras")

# Function to clean and prepare user input
def clean_text(text):
    text_words = nltk.word_tokenize(text)
    text_words = [lemmatizer.lemmatize(word.lower()) for word in text_words]
    return text_words

# Convert text input to bag-of-words
def bag_of_words(text, words):
    text_words = clean_text(text)
    bag = [1 if word in text_words else 0 for word in words]
    return np.array(bag).reshape(1, -1)

# Predict response
def predict_response(text):
    bow = bag_of_words(text, words)
    res = model.predict(bow)[0]
    index = np.argmax(res)
    
    if res[index] > 0.7:  # Confidence threshold
        tag = classes[index]
        for intent in intents["intents"]:
            if intent["tag"] == tag:
                return random.choice(intent["responses"])
    return "I don't understand. Can you rephrase?"

# Function to handle user input in Tkinter
def send_message():
    user_text = entry.get()
    if user_text.strip() == "":
        return
    
    chat_history.config(state=tk.NORMAL)
    chat_history.insert(tk.END, "You: " + user_text + "\n", "user")
    entry.delete(0, tk.END)

    bot_response = predict_response(user_text)
    chat_history.insert(tk.END, "Bot: " + bot_response + "\n", "bot")
    chat_history.config(state=tk.DISABLED)
    chat_history.yview(tk.END)  # Auto-scroll to the latest message

# --- GUI Setup ---
root = tk.Tk()
root.title("Chatbot")
root.geometry("400x500")

# Chat display area
chat_history = tk.Text(root, wrap=tk.WORD, state=tk.DISABLED, font=("Arial", 12))
chat_history.pack(pady=10, padx=10, expand=True, fill=tk.BOTH)

# Scrollbar
scrollbar = Scrollbar(root, command=chat_history.yview)
chat_history.config(yscrollcommand=scrollbar.set)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Input field
entry = tk.Entry(root, font=("Arial", 12))
entry.pack(pady=5, padx=10, fill=tk.X)

# Send button
send_button = tk.Button(root, text="Send", command=send_message, font=("Arial", 12))
send_button.pack(pady=5)

# Custom styles
chat_history.tag_config("user", foreground="blue")
chat_history.tag_config("bot", foreground="green")

root.mainloop()
