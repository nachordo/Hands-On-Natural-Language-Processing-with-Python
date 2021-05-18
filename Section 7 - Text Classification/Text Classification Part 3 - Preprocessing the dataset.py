# Text Classifiation using NLP

# Importing the libraries
import numpy as np
import re
import pickle 
import nltk
from nltk.corpus import stopwords
from sklearn.datasets import load_files
nltk.download('stopwords')


# Importing the dataset
reviews = load_files('txt_sentoken/')
X,y = reviews.data,reviews.target


# Pickling the dataset
with open('X.pickle','wb') as f:
    pickle.dump(X,f)
    
with open('y.pickle','wb') as f:
    pickle.dump(y,f)

# Unpickling dataset
X_in = open('X.pickle','rb')
y_in = open('y.pickle','rb')
X = pickle.load(X_in)
y = pickle.load(y_in)


# Creating the corpus
corpus = []
for i in range(0, len(X)): #instead of 2000 to make it dynamic
    review = re.sub(r'\W', ' ', str(X[i])) #Remove all special characters
    review = review.lower()  # Lowercase
    #review = re.sub(r'^br$', ' ', review)  
    #review = re.sub(r'\s+br\s+',' ',review) 
    review = re.sub(r'\s+[a-z]\s+', ' ',review) #remove all single characters
    review = re.sub(r'^[a-z]\s+', ' ',review) #remove all single characters
    #review = re.sub(r'^b\s+', '', review)
    review = re.sub(r'\s+', ' ', review) #substitute all multiple spaces with single one
    corpus.append(review)    