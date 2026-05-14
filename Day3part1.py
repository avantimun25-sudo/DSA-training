# maximum consecutive 1's
a=[1,1,0,1,1,1,1,1,0,1,0,1]
count=0
b=0
for i in a:
    if i ==1:
        b+=1
        if b>=count:
            count = b
    elif i==0:
        b=0
print("maximum consecutive 1's: ",count)

# input "abababab" and "ab" output 4
a="abababab"
b="ab"
count=0
for i in range(len(a)-1):
    if a[i:i+len(b)] == b:
        count += 1
print(count)

#while loop
i=1
while i<=5:
    print(i)
    i+=1

# function
def hello():
    print("hello world")
hello()

def arithmatic():
    a=int(input("enter value of a: "))
    b=int(input("enter value of b: "))
    sum = a+b
    sub = a-b
    mul = a*b
    div = a/b
    return sum, sub, mul, div
print(arithmatic())

# how many types of arguments can we pass in function?
# 1.positional
# 2.keyword
# 3.default
# 4.variable length/variable number

# positional argument
def arithmatic(a,b):
    sum = a+b
    sub = a-b
    mul = a*b
    div = a/b
    return sum, sub, mul, div
result = arithmatic(5,5)
print("Arithmatic = ",result)

# keyword argument
def credential(username, password):
    if username==password:
        print("login successfull")
    else:
         ("invalid credentials")
credential(username="admin", password="admin")

# default argument
def cityname(city="pune"):
    print(city)
cityname("nagpur")
cityname("mumbai")
cityname()

# variable length argument
def cityname(*name):
    print(name)
cityname("nagpur", "delhi", "mumbai", "pune")

# modularity approach in function
import sys
def add():
    a=int(input("enter value for a: "))
    b=int(input("enter value for b: "))
    print(a+b)
def sub():
    a=int(input("enter value for a: "))
    b=int(input("enter value for b: "))
    print(a-b)
def mul():
    a=int(input("enter value for a: "))
    b=int(input("enter value for b: "))
    print(a*b)
def div():
    a=int(input("enter value for a: "))
    b=int(input("enter value for b: "))
    print(a/b)
while True:
    print("1. addition")
    print("2. subtraction")
    print("3. multiplication")
    print("4. division")
    print("5. exit")
    choice = int(input("Enter your choice: "))
    if choice ==1:
        add()
    elif choice ==2:
        sub()
    elif choice ==3:
        mul()
    elif choice ==4:
        div()
    elif choice ==5:
        sys.exit()

                                                        # DSA
# different ways of organizing data on your computer that can be used effectively

def findBiggestNumber(sampleArray):
    biggestNumber = sampleArray[0]
    for index in range(1,len (sampleArray)):
        if sampleArray[index] > biggestNumber:
            biggestNumber = sampleArray[index]
    print(biggestNumber)
sampleArray =[5,7,9,2,3,4]
findBiggestNumber(sampleArray)