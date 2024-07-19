# -*- coding: utf-8 -*-
"""MovieSentimentAnalysis.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1AICsYJNheqEkA-ktozeTpjdJS3jnz3XT
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
from sklearn.naive_bayes import MultinomialNB

data = pd.read_csv('/content/movie_review.csv')

x = data['review']
y = data['sentiment']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

vectorizer = CountVectorizer()
x_train_vectorized = vectorizer.fit_transform(x_train)
x_test_vectorized = vectorizer.transform(x_test)

model = MultinomialNB()
model.fit(x_train_vectorized, y_train)
y_prediciton = model.predict(x_test_vectorized)
accuracy = accuracy_score(y_test, y_prediciton)
print("Accuracy:", accuracy)

print("Classification Report: \n")
print(classification_report(y_test, y_prediciton))

def predict_sentiment(review):
  vectorizedReview = vectorizer.transform([review])
  prediction = model.predict(vectorizedReview)
  if prediction[0] == 'positive':
    return 'positive'
  else:
    return 'negative'

while True:
  newReview = input("Enter a movie review or type 'exit' to stop the process: ")
  if newReview.lower() == 'exit':
    print("Exiting from the process, Thanks for Analyzing.")
    break
  else:
    print(f"Sentiment for your review: {predict_sentiment(newReview)})")

