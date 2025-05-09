# list is a buildt in dynamic sized array  .we can store all type of items also list inside list

a=[10,20,"gfg",40,True]
print(a)
print(a[0])
print(a[1])
print(a[2])

#create list
b=[1,2,3,4]
#list of string 
c=['apple','banana','cherry ']
#mixed data types
d=[1,3,4,'hello']

print(b)
print(c)
print(d)

# using list constructor
f=list((1,2,3,4,5))
print(f)

#create list with repeeated elements
g=[2]*5
h=[0]*5
print(g)
print(h)

# Accessing List Elements
i=[10,20,30,40] 
print(i[0])
print(i[-1]) #last element 

#adding the elements 
j=[]
j.append(10)
j.insert(0,5)
j.extend([14,20,40])
print(j)

# updating Elements into list
k=[10,20,30,40]
k[1]=40
print(k)

#remove the element from list
k.remove(30) #remove the first occurence of 30 
#remove the value at index 1
value=a.pop(1)
del k[0]


#itrerate over the list
dummy=[10,20,30,40]
for item in dummy:
    print(item)

#Nested list in pytohn 
matrix=[[1,2,3],[4,5,6],[6,7,8]]
print(matrix)

# range function
list1=list(range(0,5))
print(list1)
#using comprehension
list2=[i for i in range(0,5)] 
print(list2)

#remove duplicate from list 
item=3
list3=[1,2,3,4,5,3,4,5]
a=[x for x in list3 if x!=item]
