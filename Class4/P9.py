a1=int(input("Enter Angle 1 :"))
a2=int(input("Enter Angle 2 :"))
a3=int(input("Enter Angle 3 :"))
if (a1+a2+a3==180):
    if (a1+a2>a3 or a2+a3>a1 or a3+a1>a2 ):
     print("Triangle Possible")
     if (a1==90 or a2==90 or a3==90):
        print("Triangle is Right angled triangle") 
     elif(a1<90 and a2<90 and a3<90):
        print("Triangle is Acute angled traingle") 
     elif (a1>90 or a2>90 or a3>90):
        print("Triangle is Obtuse") 
else:
    print("Triangle not possible")