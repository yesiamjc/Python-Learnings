Marks={"Maths":100,"English":95,"Science":90}
sub=str(input("Enter the key you want to cheeck :"))
if sub in Marks.keys() :
    print(sub," is present.")
    print("Its value : ",Marks[sub])
else:
    print("Not present !!!")