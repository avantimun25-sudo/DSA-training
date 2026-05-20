def func(value, values):
    var=1
    values[0]=44
t=3
v=[1,2,3]
func(t,v)
print(t,v[0])

def f(i, values=[]):
    values.append(i)
    print(values)
f(1)
f(2)
f(3)

# Queue DS:-
# 1. EnQueue
# 2. DeQueue
# 2. display queue
# 4. isEmpty()
# 5. isFull()
# 6. Delete
# 7. peek()

import sys
class Queue:
    def __init__(self, size):
        self.myQueue =[]
        self.Queuesize = size
    
    def isFull(self):
        if len(self.myQueue) == size:
            return True
        else:
            return False
        
    def enQueue(self, value):
        if self.isFull():
            print("Queue is full")
        else:
            self.myQueue.append(value)
            
    def Display(self):
        print(self.myQueue)
        
    def isEmpty(self):
        if len(self.myQueue) == []:
            return True
        else:
            return False
        
    def deQueue(self):
        if self.isEmpty():
            print("Queue is empty")
        else:
            self.myQueue.pop(0)
            
    def peek(self):
        if self.isEmpty():
            print("Queue is empty")
        else:
            print(self.myQueue[0])
            
    def deleteQueue(self):
        self.myQueue=None
    

size = int(input("enter the size of queue: "))
obj=Queue(size)
print("stack has been created")
while True:
    print("1. Enqueue: ")
    print("2. Display queue: ")
    print("3. Delete: ")
    print("4. Peek: ")
    print("5. Delete Queue: ")
    print("6. Exit")
    choice = int(input("Enter your choice: "))
    if choice==1:
        value = int(input("Enter element to add in queue: "))
        obj.enQueue(value)
    elif choice==2:
        obj.Display()
    elif choice==3:
        obj.deQueue()
    elif choice==4:
        obj.peek()
    elif choice==5:
        obj.deleteQueue()
    elif choice==6:
        sys.exit()

#printing string using while loop from forward and backwords
a="Learning python is very easy"
i=0
while i<len(a):
    print(a[i],end=' ')
    i+=1
n=len(a)
i=-1
while i>=-n:
    print(a[i],end=' ')
    i-=1

a='abcdfjgerj abcdfjger'
b=[]
c=[]
for i in a:
    if i == ' ':
        break
    
print(b)

v=['a','e','i','o','u']
w=input("Enter the word where we will search the vowels: ")# w = prashantjha
found=[]#a
for i in w:#i=2:a
    if i in v:
        if i not in found:
            found.append(i)
print('Found vovels=',found)
print('Unique vowels',len(found), 'from the given word=',w)

x,y,z = map(int, input().split())
mylist=[]
# mylist =[29,38,12,48,39,55]
# y=30
# z=50
for i in range(x):
    a = int(input())
    mylist.append(a)
for j in mylist: 
    if j>=y and j<=z:
        print(j, end=' ')


import datetime
date=datetime.datetime.now()
print("It's now: {:%d/%m/%y %H:%M:%S}".format(date))

x=['A','B', 'C']
y=['A', 'B', 'C']
z=[1,2,3,4]
print(x==y)
print(x==z)
print(x != z)

# list comprehension
s=[i*i for i in range(1,11)]
print(s)

# dictionary comprehension
squares={x:x*x for x in range(1,6)}
print(squares)

doubles={x:2*x for x in range(1,6)}
print(doubles)

a,b=[int(x) for x in input("Enter 2 numbers: ").split()]
print("Product is : ",a*b)

a,b,c=[float(x) for x in input("Enter 3 float numbers: ").split(',')]
print("The sum is: ",a+b+c)

mycart=[10,20,800,60,70]
for item in mycart: #item =5:?
    if item>400:
        print("This is not in my budget")
        continue
    print(item)
else:
    print ("you have purchased everything")


while True:
    username=input("Enter username: ")
    Password=input("Enter password: ")
    if username=='admin' and Password=='admin':
        print("Login successful")
        break
    else:
       print("Invalid")

import time
class Tower:
    def __init__(self):
        print ("WELCOME TO TOWER OF HANOI GAME")
        print()
        print("Given Problem A= [3,2,1]  B= []  C[]  ")
        print()
        print ("Expected Output A= []    B= []  C[3,2,1] ")
        self.A = []
        self.B = []
        self.C = []
    def tower(self, item): #item =3 
        self.A.append(item) 
        time.sleep(3) 
        print("A=", self.A) 
        print("Items in Tower A\n")
    def pass1(self):
        self.temp = self.A.pop(2)
        self.C.append(self.temp)
        time.sleep(3)
        print("A=",self.A      ,"    ",     "B=",self.B    ,"      ","C=",self.C)
        print("Pass one Completed==========================================\n")
    def pass2(self):
        self.temp = self.A.pop(1)
        self.B.append(self.temp)
        time.sleep(3)
        print("A=",self.A      ,"    ",     "B=",self.B    ,"      ","C=",self.C)
        print("Pass Two Completed==========================================\n")
    def pass3(self):
        self.temp = self.C.pop(0)
        self.B.append(self.temp)
        time.sleep(3)
        print("A=",self.A      ,"    ",     "B=",self.B    ,"      ","C=",self.C)
        print("Pass three Completed==========================================\n")
    def pass4(self):
        self.temp = self.A.pop(0)
        self.C.append(self.temp)
        time.sleep(3)
        print("A=",self.A      ,"    ",     "B=",self.B    ,"      ","C=",self.C)
        print("Pass four Completed==========================================\n")
    def pass5(self):
        self.temp = self.B.pop(1)
        self.A.append(self.temp)
        time.sleep(3)
        print("A=",self.A      ,"    ",     "B=",self.B    ,"      ","C=",self.C)
        print("Pass five Completed==========================================\n")
    def pass6(self):
        self.temp = self.B.pop(0)
        self.C.append(self.temp)
        time.sleep(3)
        print("A=",self.A      ,"    ",     "B=",self.B    ,"      ","C=",self.C)
        print("Pass six Completed==========================================\n")
    def pass7(self):
        self.temp = self.A.pop(0)
        self.C.append(self.temp)
        time.sleep(3)
        print("A=",self.A      ,"    ",     "B=",self.B    ,"      ","C=",self.C)
        print("Pass seven Completed==========================================\n")
obj = Tower()
obj.tower(3)
obj.tower(2)
obj.tower(1)
obj.pass1()
obj.pass2()
obj.pass3()
obj.pass4()
obj.pass5()
obj.pass6()
obj.pass7()