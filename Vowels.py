#counting vowels in a given word

vowel=['a','e','i','o','u']
word="programing"
count=0
for character in word:
    if character in vowel:
        count +=1
        print(count)