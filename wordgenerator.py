import random

VOWELS = "aeiou"
CONSONANTS = "bcdfghjklmnpqrstvwxyz"
ALPHABETICAL='abcdefghijklmnopqrstuvwxyz'
AUTO='#%*'
word_format=""

length=int(input('Enter the password length:'))
for i in range(1,length+1):
    i=random.choice(AUTO)
    word_format +=i

print (word_format)
word = ""
for kind in word_format:
    if kind == "%":
        word += random.choice(CONSONANTS)
    elif kind =="#":
        word += random.choice(VOWELS)
    elif kind=="*":
        word+=random.choice(ALPHABETICAL)
    else:
        word+=kind
print(word)
