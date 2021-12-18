Lan={"Python":100,"CPP":95,"JAVA":90}
kill=str(input("Enter key you want to delete from the dictionary : "))
if (kill in Lan.keys()):
    del Lan[kill]
    print("Updated List : ",Lan)
else:
    print("Input",kill,"not found in the dictionary !!!")