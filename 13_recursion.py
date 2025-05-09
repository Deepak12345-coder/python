''' Recursion invloves in calling itself directly or indirectly to solve a problem by breaking 
it down in to simpler and more managable part ''' 
def factorial(n):
    if n==0:
        return 1
    else :
        return n*factorial(n-1)

print(factorial(20))

#base case and recursive case we have condition in recursive code
#it use stack for function call store 

#type of recursion 
# 1 tail recursion :recursive call is last opration executed in the function 
# 2 Non tail Reacursion : this occurs when there are operations or calculations follow the recursive call 

     