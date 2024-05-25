#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Face Detection using OpenCV
import cv2

def detect_faces(image_path):
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    return faces

image_path = 'path_to_image.jpg'
faces = detect_faces(image_path)
print(f"Detected faces: {faces}")


# In[ ]:


#Face Recognition using Pre-trained Model (FaceNet)
from keras.models import load_model
import numpy as np

# Load pre-trained model
model = load_model('facenet_keras.h5')

def preprocess_image(image_path):
    image = cv2.imread(image_path)
    image = cv2.resize(image, (160, 160))
    image = image.astype('float32')
    mean, std = image.mean(), image.std()
    image = (image - mean) / std
    image = np.expand_dims(image, axis=0)
    return image

image_path = 'path_to_image.jpg'
processed_image = preprocess_image(image_path)
embedding = model.predict(processed_image)
print(f"Face embedding: {embedding}")


# In[ ]:


# Attendance Marking and Database Interaction
import sqlite3
from datetime import datetime

# Connect to the database
conn = sqlite3.connect('attendance.db')
c = conn.cursor()

# Create table
c.execute('''CREATE TABLE IF NOT EXISTS attendance
             (id INTEGER PRIMARY KEY, name TEXT, timestamp TEXT)''')

def mark_attendance(name):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    c.execute("INSERT INTO attendance (name, timestamp) VALUES (?, ?)", (name, timestamp))
    conn.commit()

# Example of marking attendance
mark_attendance('John Doe')

