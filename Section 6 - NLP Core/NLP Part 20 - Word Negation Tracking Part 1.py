# Word Negation Tracking - Strategy 1

import nltk

sentence = "I was not happy with the team's performance"

words = nltk.word_tokenize(sentence)

new_words = []

temp_word = ''
for word in words:
    print(word)
    if word == 'not':
        temp_word = 'not_'
    elif temp_word == 'not_':
        word = temp_word + word
        temp_word = ''
    if word != 'not':
        new_words.append(word)
    
    print(new_words)

sentence = ' '.join(new_words)
print(sentence)