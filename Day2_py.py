# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 19:06:44 2020

@author: pitambarmishra
"""



a= 4|6
print(a)

a=['a','b']
b=['r','n']
z = a.insert(1,b)
print(z)



List1 = ['Python', 'Py', 'Pyth', 'Python3'] 
List2 = List1*2 
List3 = List1[:] 
List2[0] = 'Hello' 
List3[1] = 'World' 
sum = 0 
for ls in (List1, List2, List3): 
    if ls[0] == 'Hello': 
        sum += 1 
        if ls[1] == 'World': 
            sum += 2 
            print(sum, List2)
#Contnue statement: it returns the control to the start of the loop if condition satisfied

x=0
y='datascientist'

while x < len(y):
    if y[x]=='t' or y[x]=='e':
        x+=1
        continue
    print("value :", y[x])
    x+=1
    
#Break Statement: It gets control out of the loop if the condition satisfied

x=0
y='datascientist'

while x < len(y):
    if y[x]=='t' or y[x]=='e':
        x+=1
        break
    print("value :", y[x])
    x+=1    
    
#Type the following code to create a list with numbers named nums from 1 to 3 and
#print its type and run it by pressing Shift + Enter.  
    
mydata=[1,2,4]
print(id(mydata))
print(type(mydata))
print(mydata[0])

#Type the following code to Loop over the list and print all numbers in it separated by
#commas.

mydata=[5,8,2]
for x in mydata:
    print(x, end=',')

mydata=[4,2,7]
for x in mydata:
    print(x)
  
#append another number to the list
print(mydata)
mydata.append(100)
print(mydata)

#To print the last value in the list
print(mydata[3])

#To remove the last element from the list -----used with index
mydata.pop(3)
print(mydata)

#To remove a value from the list using remove-------used with values
mydata.remove(2)
print(mydata)

#working with list
mydata=(1,2,4)
print(type(mydata))
print(mydata[1])

for x in mydata:
    print(x)

#To print the last value from the list
print(mydata[-1])

#working with Set
#A set can store unordered values i.e different data types. A set cannot contain duplicate values.
# Where list and tuple can contain duplicate values
mydata=set([1,2,3])
print(mydata)
print(type(mydata))

for x in mydata:
    print(x)
    
mydata.add(12)
mydata

#To remove a value from set
mydata.remove(12)
mydata

#for loop example
#Here, the for loop prints items of the list until the loop exhausts. When the for loop exhausts, 
 #it executes the block of code in the else and prints No  values left.
 
a=[0,10,5,8,7]
 
for x in a:
     print(x)
else:
    print("no values left")

#This for...else statement can be used with the break keyword to run the else
#block only when the break keyword was not executed. Let's take an example:

# program to display student's scores

ds_std="ranju"

scores = {'pitu':90,'pita':80,'chora':85}

for ds_std1 in scores:
    if ds_std==ds_std1:
        print(scores[ds_std1])
        break
else:
    print("No scores found")
    
ds_std="ranju"

scores = {'pitu':90,'pita':80,'ranju':85}

for ds_std1 in scores:
    if ds_std==ds_std1:
        print(scores[ds_std1])
        break
else:
    print("No scores found")
    
z={5,7,3,'dfdg',7,3}
z
print(z) # output Out[60]: {3, 5, 7, 'dfdg'}
print(type(z))
   
#Type the following code to add items to dictionaries with keys as numbers 1, 2 and 3
#and value as their squares.
 
#Type the following code to create an empty dictionary and print its type and run it by
#pressing Shift + Enter.   
mydata= dict()       
print(type(mydata))  

#Type the following code to add items to dictionaries with keys as numbers 1, 2 and 3
#and value as their squares.
mydata[1]=1
mydata[2]=4
mydata[3]=9

#To view the elements of the dictionary in key:value format

for key, value in mydata.items():
    print("{0}:{1}".format(key,value))

    
    #File Handling
f = open("myfile.txt","x")
f.write("This is my file")
f.close()

# to get input from user
input('what is your name? ')









