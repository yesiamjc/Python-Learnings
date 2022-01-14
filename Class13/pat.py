def pat(c='%',n=6,r=1):
    for i in range(r):
        print()
        for j in range(n):
            print(c,end=' ')
c=input("Enter the charecter to be displayed :")
n=int(input("Enter the number of rows :"))
m=int(input("Enter the number of columns :"))
pat()
pat(c)
pat(c,n)
pat(c,n,m)