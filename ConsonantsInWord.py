# Consonants in a given word
"""""
vowel=['a','e','i','o','u']
word="programing"
count=0
for character in word:
    if character not in vowel:
        count +=1
        print(count)"""

vowel=['a','e','i','o','u']
word="programing"
count=0
for character in word:
    if character not in word:
        count +=1
        print(count)
