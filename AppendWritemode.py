# Append vs write mode 
file1=open("myfile.txt","w")
L=["This is Delhi \n","This is Paris \n","This is london \n "]
file1.writelines(L)
file1.close()
file1=open("myfile.txt","a")
file1.write("Today \n")
file1.close()
file1=open("myfile.txt","r")
print("Output of Readlines after appending ")
print(file1.read())
print()
file1.close()

file1=open("myfile.txt","w")
file1.write("Tommorrow \n")
file1.close()
file1=open("myfile.txt","r")
print("Output of readlines after writing  ")
print(file1.read())
print()
file1.close()
