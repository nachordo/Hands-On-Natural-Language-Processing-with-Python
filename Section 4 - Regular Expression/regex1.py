# Introduction to Python Regular Expressions

# Importing Libraries
import re

pattern1 = "abcd"
pattern1 = "9876 efg 98"
#pattern1 = "a"

print("Occurences of any character: ",re.match(r".+",pattern1)) 
#. matches every character
# .* 0 or more, .+ one or more
print("Occurences of A_Za-z: ",re.search(r"[a-z]+",pattern1))
print("Occurences of ab*: ",re.search(r"ab?",pattern1))

if re.match(r"[a-z]+",pattern1) != None:
    print("Match!")
else:
    print("No Match!")
    
    
####################


sentence="I was born in USA, in 1996"

re.sub(r"\d","",sentence)
# 'I was born in USA, in '

re.sub(r"\d","XXXX",sentence)
# 'I was born in USA, in XXXXXXXXXXXXXXXX'

re.sub(r"\d","X",sentence)
# 'I was born in USA, in XXXX'

#####################################

sentence="ab" # try "a" "abb" "abbbbbb"
re.match("ab?",sentence) #a followed by no b or one b