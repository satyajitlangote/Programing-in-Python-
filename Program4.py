# Program to create a list of numbers and separate those numbers in two 
#different list one includes odd number other even

def Split(mix):
    ev_li=[]
    od_li=[]
    for i in mix:
        if i % 2 == 0:
            ev_li.append(i)
        else:
            od_li.append(i)
            print("Even lists",ev_li)
            print("Odd Lists",od_li)
           
mix=[2,5,13,17,51,62,73,84,95]
Split(mix)