def pyramid(n):
    for i  in range(n):
        for j in range(i,n):
            print("b",end="")
            for j in range(i+1):
                print("*",end="")
                for j in range(i):
                    print("*",end="")
                    print("")
                    pyramid(5)