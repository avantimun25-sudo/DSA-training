# basicSalary=20000
# so we have to calculate the
# HRA of basicSalary = 20%
# TA of ------------ = 30%
# DA of ------------ = 45%


basicSalary = 20000
HRA = (20 / 100) * basicSalary
TA = (30 / 100) * basicSalary
DA = (45 / 100) * basicSalary
grossSalary = basicSalary + HRA + TA + DA
print("Gross Salary is:", grossSalary)

#binary search is faster than linear search as it is not compulsory to visit every element in the array.
#Binary search works by repeatedly dividing in half the portion of the list that could contain the target value, 
# until you've narrowed down the possible locations to just one.
#Half of the remaining elements can be eliminated at a time, instead of eliminating them one by one.
#Binary search only works for sorted arrays.

#binary search algorithm
#create function with 2 parameters which are a sorted array and a value


def binarysearch(array, target):
    low=0
    high=len(array)-1
    while low<=high:
        mid=(low+high)//2  #flow division operator, it will give us the index of the middle element in the array.
        if array[mid]==target:
            return mid
        elif array[mid]<target:
            low=mid+1
        else:
            high=mid-1
    return -1 #if the value is never found return -1.
array =[2,4,5,9,11,13,14,15,19,20,22,23,27,30,32,39,42,44,45,49,51,53,54,55,59,60,62,63,67,70,72,79]
target=72
binarysearch(array,target)
result=binarysearch(array,target)
if result==-1:
    print("Element not found at index:", result)    
else:
    print("Element found at index:", result)

#stack implementation without size limit
#stack implementation with size limit

#there are two ways
#1. List/Array
#2. Linked List


#class
#way to bind data and functions together-- data members and member functions, 
# data members(variables) and member functions(methods) are
# encapsulated together in a class. It is a blueprint for creating objects. 
# #It defines a datatype by bundling data and methods that work on the data into one single unit.

#object
#runtime entity, created from a class, it is an instance of a class. It has state and behavior.
#Instance of a class. It is created from a class and has its own unique identity. It can access the data members and member functions of the class. It is created using the constructor of the class. It is destroyed when it goes out of scope or when the program ends.
#also called as reference variable, it is used to access the members of the class. It is created using the constructor of the class. It is destroyed when it goes out of scope or when the program ends.


#constructor


# class
class Name: #first letter of class name should be capital, #static variable- shared by all objects of the class, 
#instance variable- unique to each object
    age=30 #data member(class variable/static variable)
    def display(self):  #method(member function)
        print("Hello World")
#object
obj=Name() #creating an object of the class Name, obj is a reference variable, it is used to access the members of the class Name
print(obj.age) #accessing the data member age using the object obj
obj.display() #accessing the member function display using the object obj


class Student:
    def __init__(self): #constructor, special method/variable -- using double underscore before and after the method name.
        self.name="rj" #instance variable , 4 bytes of memory is allocated for the variable name, it is stored in the heap memory, it is created when the object is created and destroyed when the object is destroyed.
        self.age=22 #instance variable , 2 bytes of memory is allocated for the variable age, it is stored in the heap memory, it is created when the object is created and destroyed when the object is destroyed.

    def display(self): #method
        print("Name:",self.name)
        print("Age:",self.age)
stuObj=Student() #creating an object of the class Student, stuobj is a reference variable, it is used to access the members of the class Student
print(stuObj)


class Message:
    def __init__(self): #constructor
        print("I am a constructor")
    def shows(self):
        print("Class program")
obj=Message()
obj.shows()
obj2=Message()
#for one object, constructor will be called once only


#types of constructors--> 1. Parameterised  2. Default  3. Copy

#Parameterised constructor
class StudentInfo:
    def __init__(self, name, age, roll_no):
        self.Name = name
        self.Age =age
        self.roll_no =roll_no
    def displayStudentInfo(self):
        print("Name=", self.Name)
        print("Age=", self.Age)
studentObj = StudentInfo("Rj", 22, 101)
studentObj.displayStudentInfo()

# stack implementation witout size limit
# 1.Push
# 2.Pop
# 3.Peek
# 4.isEmpty
# 5.ifFull
# 6.Delete
# 7.Display

import sys

class Stack:
    def __init__(self):
        self.mystack = []   # creating stack

    def push(self, value):
        self.mystack.append(value)
        print("Element pushed")

    def display(self):
        print(self.mystack)

    def isEmpty(self):
        if self.mystack == []:
            return True
        else:
            return False

    def pop(self):
        if self.isEmpty():
            print("Stack is empty")
        else:
            print("Popped element:", self.mystack.pop())

    def peek(self):
        if self.isEmpty():
            print("Stack is empty")
        else:
            print("Top element:", self.mystack[-1])

    def deleteStack(self):
        self.mystack = []
        print("Stack deleted")


obj = Stack()
print("Stack has been created")

while True:
    print("\n1. Push")
    print("2. Display")
    print("3. Pop")
    print("4. Peek")
    print("5. Delete")
    print("6. Exit")

    choice = int(input("Enter your choice = "))

    if choice == 1:
        value = int(input("Enter value to push in stack = "))
        obj.push(value)

    elif choice == 2:
        obj.display()

    elif choice == 3:
        obj.pop()

    elif choice == 4:
        obj.peek()

    elif choice == 5:
        obj.deleteStack()

    elif choice == 6:
        print("Exiting...")
        sys.exit()

    else:
        print("Invalid choice")

        

    
#stack implementation with size limit
import sys

class Stack:
    def __init__(self, size):
        self.size = size
        self.mystack = []

    def isEmpty(self):
        return self.mystack == []

    def isFull(self):
        return len(self.mystack) == self.size

    def push(self, value):
        if self.isFull():
            print("Stack Overflow! Stack is full")
        else:
            self.mystack.append(value)
            print("Element pushed")

    def pop(self):
        if self.isEmpty():
            print("Stack Underflow! Stack is empty")
        else:
            print("Popped element:", self.mystack.pop())

    def peek(self):
        if self.isEmpty():
            print("Stack is empty")
        else:
            print("Top element:", self.mystack[-1])

    def display(self):
        if self.isEmpty():
            print("Stack is empty")
        else:
            print("Stack elements:", self.mystack)

    def deleteStack(self):
        self.mystack = []
        print("Stack deleted")


# Taking stack size from user
size = int(input("Enter size of stack = "))

obj = Stack(size)

print("Stack has been created")

while True:
    print("\n1. Push")
    print("2. Display")
    print("3. Pop")
    print("4. Peek")
    print("5. Delete")
    print("6. Exit")

    choice = int(input("Enter your choice = "))

    if choice == 1:
        value = int(input("Enter value to push in stack = "))
        obj.push(value)

    elif choice == 2:
        obj.display()

    elif choice == 3:
        obj.pop()

    elif choice == 4:
        obj.peek()

    elif choice == 5:
        obj.deleteStack()

    elif choice == 6:
        print("Exiting...")
        sys.exit()

    else:
        print("Invalid choice")




#the input consists of an integer data, representing the data to be transmitted.
#Output: find an integer representing the security key, if no such key exists, return -1.
#input: 5,7,8,3,7,8,9,2,3
#output: 3
#explanation: the repeated digits in the input are 3,7,8. The smallest of these is 3, which is the security key.

#the input consists of an integer data, representing the data to be transmitted.
#Output: find an integer representing the security key, if no such key exists, return -1.
#input: 5,7,8,3,7,8,9,2,3
#output: 3
#explanation: the repeated digits in the input are 3,7,8. The smallest of these is 3, which is the security key.

def securitykey(data):
    count = {}
    for i in data:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    repeated_digits = [digit for digit, freq in count.items() if freq > 1]
    if not repeated_digits:
        return -1
    return min(repeated_digits)
data = [5,7,8,3,7,8,9,2,3]
key = securitykey(data)
if key == -1:
    print("No security key found.")
else:
    print("The security key is:", key)


mylist = [5,7,8,3,7,8,9,2,3] #i=0
newlist = []
for i in range(len(mylist)):
    count = 0
    key=mylist[i] #key 5
    j=i+1 #j=1
    while j<len(mylist):
        if key==mylist[j]: #5==7
            newlist.append(key)
        j=j+1
print(len(newlist))

mylist = [5, 7, 2, 3, 7, 8, 2, 3, 4]

newdict = {}

for i in range(len(mylist)):
    count = 0
    key = mylist[i]

    j = 0
    while j < len(mylist):
        if key == mylist[j]:
            count += 1
        j = j + 1

    if count > 1:
        newdict[key] = count

max_value = max(newdict.values())

print("Duplicate elements with counts:", newdict)
print("Maximum duplicate count:", max_value)

#using tuple unpacking to swap the elements in the array
def bubblesort(array):
    for i in range(len(array)-1):
        for j in range(len(array)-1):
            if array[j]>array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]

array = [64, 34, 25, 12, 22, 11, 90]
bubblesort(array)
print("Sorted array is:", array)


#using temporary variable to swap the elements in the array
def bubblesort(array):
    for i in range(len(array)-1):
        for j in range(len(array)-i-1):
            if array[j]>array[j+1]:
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp
            print(array)
        print()

array = [64, 34, 25, 12, 22, 11, 90]
bubblesort(array)
print("Sorted array is:", array)