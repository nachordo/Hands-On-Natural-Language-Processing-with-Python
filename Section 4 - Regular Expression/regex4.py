# Introduction to Python Regular Expressions

# Importing the libraries
import re

sentence1 = "Welcome to the year 2018"
sentence2 = "Just ~%* ++++--- arrived at @Jack's place. #fun"
sentence3 = "I                  love                u"

sentence1_modified = re.sub(r'\d','',sentence1) #\d -- any digit

sentence2_modified = re.sub(r'[@#\.\']','',sentence2)

sentence2_modified = re.sub(r'\W',' ',sentence2) #\w=a-zA-Z0-9, \W= not \w

sentence2_modified2 = re.sub(r'\s+',' ',sentence2_modified) #\s = single space                               

sentence2_modified3 = re.sub(r"\s+[a-zA-Z]\s+",' ',sentence2_modified2) #eliminates the "s", removes a single letter

sentence3_modified = re.sub(r'\s+',' ',sentence3)      
sentence3_modified2 = re.sub(r'\s+love\s+',' hate ',sentence3)                                