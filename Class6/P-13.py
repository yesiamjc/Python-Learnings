l1= int(input("Input lower range : "))
l2 = int(input("Input upper range : "))
print("Prime numbers are :")
count =0
for N in range(l1, l2 + 1):
   if N > 1:
       for i in range(2, N):
           if (N % i) == 0:
               break
       else:
           print(N)
           if(N>9 and N<100):
               count=count+1
print("Total 2 digit prime numbers : ",count)