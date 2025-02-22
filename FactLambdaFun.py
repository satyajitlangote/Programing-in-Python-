# Finding factorial using lambada function
#f=lambda n: 1 if n==0 else n*f(n-1)

num=int(input("Enter a number "))
factorial=1
if num <0:
    print("Sorry,factorial dor=es not exist for negative numbers")
elif num==0:
    print("The factorial of ) is 1")
else:
    for i in range(1,num+1):
        factorial =factorial*i
        print(f"The factorial of{num}is ",factorial)
