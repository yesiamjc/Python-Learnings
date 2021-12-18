n=int(input("Enter Number Of Rows : "))
for i in range (n,0,-2):
    for j in range(i,n+1,2):
        print(j,end=" ")
    print()