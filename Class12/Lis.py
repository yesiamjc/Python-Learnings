lis1=[1,2,3,4,5]
def change_list(lis1):
    lis1[4]=18
    print("value inside function :",lis1,"address :",id(lis1))
    return
print("before function call :",lis1,"address :",id(lis1))
change_list(lis1)
print("after function call :",lis1,"address :",id(lis1))