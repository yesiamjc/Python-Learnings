n=int(input("Enter Number Of Rows : "))
for i in range (n,0,-1):
    for j in range(n,i-1,-1):
        print(j,end=" ")
    print()