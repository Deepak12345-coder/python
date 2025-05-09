# global variable are those which are not defined inside any function 
#local variable which are defined inside a function and their scope is limited 

#local variable
def f():
    name ="Deepak"
    print(name)

f()
#global varaible
def f1():
    print("inside function",s)
    global s
    s+="gfg"

s="My Name is Deepak"
f1()

#if we want to change global variable inside function scope   then we need global keyword inside function with variable