import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='3'
import random
import pickle
import json
import numpy as np
import nltk
from nltk.stem import WordNetLemmatizer
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense,Activation,Dropout
from tensorflow.keras.optimizers import SGD

print("Started")
lemmatizer=WordNetLemmatizer()

intents=json.load(open(r'intents.json'))
words=[]
classes=[]
documents=[]
ignore_letters=['?','!',',','.']

for intent in intents['intents']:
    for pattern in intent['patterns']:
        word_list=nltk.word_tokenize(pattern)
        words.extend(word_list)
        documents.append((word_list,intent['tag']))
        if intent['tag'] not in classes:
            classes.append(intent['tag'])

words=[lemmatizer.lemmatize(word) for word in words if word not in ignore_letters]
words=sorted(set(words))
classes=sorted(set(classes))
pickle.dump(words, open(r'model\words.pkl','wb'))
pickle.dump(classes, open(r'model\classes.pkl','wb'))

training=[]
output_empty=[0]* len(classes)

for document in documents:
    bag=[]
    word_pattern=document[0]
    word_pattern=[lemmatizer.lemmatize(word) for word in word_pattern if word not in ignore_letters]
    for word in words:
        bag.append(1) if word in word_pattern else bag.append(0)
    output_row=list(output_empty)
    output_row[classes.index(document[1])]=1
    training.append([bag,output_row])
    
random.shuffle(training)
training=np.array(training,dtype=object)
train_x=list(training[:,0])
train_y=list(training[:,1])

model=Sequential()
model.add(Dense(128,input_shape=(len(train_x[0],),), activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(64, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(len(train_y[0]),activation='softmax'))

sgd=SGD(learning_rate=0.01,weight_decay=1e-6,momentum=0.9, nesterov=True)
model.compile(loss='categorical_crossentropy',optimizer=sgd,metrics=['accuracy'])
model.fit(np.array(train_x),np.array(train_y),epochs=200, batch_size=5,verbose=1)
model.save(r'model\chatbot_model.keras')
