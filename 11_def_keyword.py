# def keyword used for function
import math
def subnumber(x,y):
    return (x-y)
subnumber(5,3)
#prime number 

def fun(n):
   x=2
   while x<=n:
     flag=True
     for d in range(2,int (math.sqrt(x))+1):
       if x%d==0:
           flag=False
           break
     if flag:
        print(x)
     x+=1
fun(10)

#lambda function
# Syntax: lambda arguments : expression
f1= lambda x:"nagative" if x< 0 else "positive " if x>0  else "zero" 
print(f1(5))
