def fib(n):
    if(n<1):
        return 0
    elif(n<2):
        return 1
    return(fib(n-1)+fib(n-2))
n=int(input("Enter Number of terms :"))
for i in range(n):
    print("fib (",i,") = ",fib(i))