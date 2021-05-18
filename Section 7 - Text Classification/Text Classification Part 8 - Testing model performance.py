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

# Creating the BOW model
from sklearn.feature_extraction.text import CountVectorizer
vectorizer = CountVectorizer(max_features = 2000, min_df = 3, max_df = 0.6, stop_words = stopwords.words('english'))
X = vectorizer.fit_transform(corpus).toarray()


# Creating the Tf-Idf Model
from sklearn.feature_extraction.text import TfidfTransformer
transformer = TfidfTransformer()
X = transformer.fit_transform(X).toarray()


# Creating the Tf-Idf model directly
from sklearn.feature_extraction.text import TfidfVectorizer
vectorizer = TfidfVectorizer(max_features = 2000, min_df = 3, max_df = 0.6, stop_words = stopwords.words('english'))
X = vectorizer.fit_transform(corpus).toarray()


# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
text_train, text_test, sent_train, sent_test = train_test_split(X, y, test_size = 0.20, random_state = 0)


# Training the classifier
from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression()
classifier.fit(text_train,sent_train)


# Testing model performance
sent_pred = classifier.predict(text_test)


from sklearn.metrics import confusion_matrix
cm = confusion_matrix(sent_test, sent_pred)
print("Accuracy: ",(cm[0][0]+cm[1][1])*100/400)





print("\n\n\nOTHER PARAMETERS\n\n\n")
def testing_pars(max_features, min_df , max_df):
    vectorizer = TfidfVectorizer(max_features = max_features, min_df = min_df, max_df = max_df, stop_words = stopwords.words('english'))
    X = vectorizer.fit_transform(corpus).toarray()
    
    
    # Splitting the dataset into the Training set and Test set
    from sklearn.model_selection import train_test_split
    text_train, text_test, sent_train, sent_test = train_test_split(X, y, test_size = 0.20, random_state = 0)
    
    
    # Training the classifier
    from sklearn.linear_model import LogisticRegression
    classifier = LogisticRegression()
    classifier.fit(text_train,sent_train)
    
    
    # Testing model performance
    sent_pred = classifier.predict(text_test)
    
    
    from sklearn.metrics import confusion_matrix
    cm = confusion_matrix(sent_test, sent_pred)
    return (cm[0][0]+cm[1][1])*100/400


for fe in [100,500,1000,1500,1750,2000,2250,2500,2750,3000,4000]:
    for mindf in range(1,10):
        for mxdf in [0.5,0.55,0.6,0.65,0.7,0.75,0.8,0.85,0.9]:
            score = testing_pars(fe,mindf,mxdf)
            if score > 85.:
                print("Score:",score,"   with:",fe,mindf,mxdf)