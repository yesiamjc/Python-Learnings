keys=[]
values=[]
n=int(input("Enter number of elements you want to have in the dictionary :"))
for x in range(0,n):
    element=input("Enter key element-"+str(x+1)+":")
    keys.append(element)
for x in range(0,n):
    element=input("Enter value element-"+str(x+1)+":")
    values.append(element)
d=dict(zip(keys,values))
print("The dictionary is :",d)