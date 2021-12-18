number = int(input("Enter the number : "))
choice = print("Options : \n1.Factorial of each digit.\n2.Reverse of that number.\n3.Factor’s of that number")
option=input("Enter Option Number : ")
factorial =1
ans =1
if (option==1):
    for i in range(1,number + 1):
        factorial = factorial*i
    ans=ans*factorial
print("The factorial of ",number," is ",ans)