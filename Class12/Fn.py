a=7
def change_value(a):
    a=10
    print("inside function value of a :",a,"address :",id(a))
    return
print("before function call value of a :",a,"address :",id(a))
change_value(a)
print("before function call value of a :",a,"address :",id(a))