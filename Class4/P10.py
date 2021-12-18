name = input("Enter name of employee : ")
Basic=int(input("Enter Baic payout : "))
if (Basic>=10000):
    DA=float(Basic*0.40)
    HRA=float(Basic*0.30)
    print("Grade 1")
elif (Basic==5000 or Basic<10000):
    DA=float(Basic*0.40)
    HRA=float(Basic*0.25)
    print("Grade 2")
elif (Basic>2000 or Basic<5000):
    DA=float(Basic*0.30)
    HRA=float(Basic*0.20)
    print("Grade 3")
elif (Basic<=2000):
    DA=float(Basic*0.30)
    HRA=float(Basic*0.15)
    print("Grade 4")
Salary= int(Basic+DA+HRA)
print("Basic : ",Basic)
print("DA : ",DA)
print("HRA : ",HRA)
print("Salary : ",Salary)
TaxApplicable=float((Salary-50000)*12*0.30)
if (TaxApplicable > 0):
    print("Monthly Taxable Ammount : ",TaxApplicable/12)
    print("Net Monthly Salary : ",(Salary-(TaxApplicable/12)))
else:
    print("Tax is not applicable")