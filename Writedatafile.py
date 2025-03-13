# Program to show various ways to 
# write data to a file using with statement  14-3

L=["This is Delhi \n ","This is paris \n ","This is London \n"]
with open("myfile.txt","w") as file1:
    file1.write("Hello \n")
    file1.writelines(L)
with open("myfile.txt","r+") as file1:
    print(file1.read())
