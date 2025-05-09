'''in python *args anf **kargs are usesd to follow functions to accept an Arbitrary number of Arguments'''
# *args used for pass variable number of arguments to function: in which just position of  
def fun(*args):
    for num in args:
        print(num)
    return sum(args )
fun(1,2,3,4)

# **kwargs=keyword arguments in which key value pair matters 
def fun1(**kwargs):
    print(kwargs)
    for key,value in kwargs.items():
       print("%s===%s"%(key,value))
    
fun1(s1=3,s2=4,s3="Deepak") 

#We can pass *args **kwargs together they can take according to passing item 
def fun2(*args,**kwargs):
    print(args)
    print(kwargs)
    for key, value in kwargs.items():
        print(key ,value)

fun2(1,3,4,name="deepak",age=24)
