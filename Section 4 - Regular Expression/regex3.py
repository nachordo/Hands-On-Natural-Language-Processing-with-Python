# Introduction to Python Regular Expressions

# Importing Libraries
import re

pattern1 = "I love Avengers" #I love Justice League

print(re.sub(r"Avengers","Justice League",pattern1))

print(re.sub(r"[a-z]","0",pattern1,1,flags=re.I)) #re.I --- Case insensitive

#############################

print(re.sub(r"[a-z]","0",pattern1))
print(re.sub(r"[a-z]","0",pattern1,flags=re.I))

print(re.sub(r"[a-z]","0",pattern1,7))