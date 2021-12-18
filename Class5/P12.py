#Write a program to input a number and check and print whether it is palindrome or not.


n=int(input("Enter number : "))
t=n
rev=0
while(n>0):
    last_digit=n%10
    rev=rev*10+last_digit
    n=n//10
if(t==rev):
    print("Palindrome")
else:
    print("Not palindrome")