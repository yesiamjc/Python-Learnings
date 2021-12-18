# Write a program to input a number and print its table.
#Write a program to input the value of N. Print all the ODD and EVEN numbers between 1 to N.
#Write a program to input a number and check and print whether it is a prime number or not.
n = int(input("Enter number : "))
print("Table :")
for i in range (1,11):
    print(n,"x",i,"=",n*i)
print("Odd-Even :")
print("Even Numbers : ")
for i in range (1,n+1):
    if(i%2==0):
        print(i)
print("Odd Numbers : ")
for i in range (1,n+1):
    if(i%2!=0):
        print(i)
print("Prime-Nonprime :")
for i in range (2,n):
    if(n%i==0):
        print(n,"is Non-Prime")
        break
    else:
        print(n,"is Prime")
        break


