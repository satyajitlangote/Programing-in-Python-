## Counting the number of occurance of a charcter in a string

word="programing"
character="r"
count=0
for i in word:
    if i == character:
        count +=1
        print(count)