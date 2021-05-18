# Introduction to Python Regular Expressions

# Importing Libraries
import re

pattern1 = "Apples are tasty"
pattern2 = "Today I feel like crying."

if re.match(r"^Apples",pattern1):  # ^ --- Starts with ^**whatever**
    print("Matches!")
else:
    print("No Match!")
    
if re.search(r"\.$",pattern2): # $ --- ends with **whatever**$
    print("Match!")
else:
    print("No Match!")
    
    
#######################

st = "1996 is the year"
re.match(r"[a-zA-Z]+",st)  
# No match! Match only looks at the first pattern
re.search(r"[a-zA-Z]+",st)
#<re.Match object; span=(5, 7), match='is'>


