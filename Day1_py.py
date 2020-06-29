# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 20:03:22 2020

@author: pitambarmishra
"""

#Assign value to a variable
x=12
print(x)

a,b,c=1,2,3
a
y=5.72

print(y)

#Assign multiple values into a variable
z=(10,20,30)
print(z)

a,b,c=(21,52,65)
print(a)


para = '''My Name is Ranju
I am in Bangalore'''

print(para)

type(para)

TRUE == True #NameError: name 'TRUE' is not defined
#mutable : as x var is created once, if i create it again with different value the id will be different

x=12
print(x)
print(id(x))

x=20
print(x)
print(id(x))

mydata =[1,5,8]
print(id(mydata))
print(type(mydata))

mydata=[10,45,78]
print(id(mydata))

#if else
x=40

if x<30:
    print("num is less than 30")
elif x==30:
    print("num is equal to 30")
else:
    print("num is greater than 30")

#list:mutable, tuple : immutable
#569282654152
lv=[1,5,8]
print(id(lv))
print(lv[0])

tv=(4,5,6)
print(tv[0])

#value change : list vs tuple
lv=[1,5,8]
print(id(lv))#569282652744
lv[0]= 9
print(lv)

tv=(4,5,6)
tv[0]=85 #unable to assign a new value to any index. getting error as " tuple object does not support item assignment."
print(tv)

lv +=[52,25,65]
print(id(lv)) #569282652744(same memory location)
print(lv)

tv += (45,44,46)
print(id(tv)) #569255212328(different memory location)
print(lv)

#loops

num=(2,5,7,8,9,10)
for x in num:
    print(x)
num=(2,5,7,8,9,10)
for x in num:    
    print(x,end=",")

#while
count=0
while count<5:
    count=count+1
    print(count)
    

count1 = 10
while count1<5:
    count1=count1+1
    print(count1)
else:
    print("condition is not satisfied")    


count1 = 10 
while (count1 <5):
 count1 = count1+1
 print(count1) 
else:
  print("condition not satisfied") 


# is operator
  
x = ['apple', 'mango']
y = ['apple', 'mango']
z = x
x is y   #False

x is z   # True

'apple' in z  #True

'strawberry' in z  #False

num = [1,2,3]
num2 = []
for i in num:
    num2.append(i*i)
num2 


# list comprehensaion
num3 = [i*i for i in num]
num3   

# to square only even numbers
num2 = []
for i in num:
    if i%2 == 0:
        num2.append(i*i)
        print(num2)
        
num3 = []
num3 = [i*i for i in num if i%2==0]
num3

#lamda function
x = lambda a: a+10
x(5)

y = lambda c,d:c+d
y(5,2)












