name = "prashantjha"#012345678910
print(name[0])
print(name[1]) #r
print(name[-1]) #a
#print(name[15])
print(name[0:5])
print (name[1:]) # rashantjha
print(name[:5])
print(name[:])
print(name[1:8:2])#''8-1=7= rsat
print(name[::-1])# reverse of string

s = "Python are High level programming"
print(s.lower())
print(s.upper())
print(s.swapcase())
print(s.title())
print(s.capitalize())

name = "prashant"
sal = 5000
age = 28
print("{} sal is {} age is{}".format(name,sal,age))
print("{0} sal is {1} age is {2}".format(name, sal, age))
print("{x} sal is {y} age is{z}".format(x=name, y=sal,z=age))
A=1
print(f"{A} is a good boy")

name ="Avanti"
for i in name:
    print(i)

#i/p Avanti
#o/p Avnti
name="avanti"
a=""
for i in name:
    if i not in a:
        a = a + i
print(a)

#reverse
n=len(name)
for i in range(n-1,-1,-1):
    a = a + name[i]
print(a)
print(name[::-1])

name=input("eenter a word: ")
a=""
n=len(name)
for i in range(n-1,-1,-1):
    a+=name[i]
if name==a:
    print("pallindrome")
else:
    print("not a pallindrome")

#consonent and vowels
a=input("enter a word: ")
vowels=['a','e','i','o','u']
c=0
v=0
for i in a:
    if i in vowels:
        v+=1
    else:
        c+=1
print("count of vowels: ",v)
print("count of consonents: ",c)

#count the words in a string
a=input("enter a sentence: ")
count=1
if a=="":
    print("number of words = 0")
else:
    for i in a:
        if i == " ":
            count+=1
    print("number of words = ",count)

a=50
b=30
c=20
d=10
print((a+b)*c/d) #160
print((a-b)*(c/d)) #40
print(a+(b*c)/d) #110

#count special characters
ab=(input("enter a string: "))
count=0
for b in ab:
    a=ord(b)
    if a>= 65 and a<=90:
       continue
    elif a>=97 and a<=122:
        continue
    elif a>=48 and a <=57:
        continue
    else:
        count+=1
print("special character count: ",count) 

s="this is a test"
print(s.title())

print('prashantjha777'.isalnum()) #True
print('prashantjha'.isalpha()) #True
print('777f'.isdigit())
print('sdsdsdsd' .islower())
print(''.islower())
print('PRASHANTJ'.isupper())
print('My Name Is Prashant'.istitle())
print(''.istitle())
print(''.isspace())
print("Hello".startswith("He"))
print("Hello".endswith("lo"))

print("Prashant".find("n"))
print("Prashant".index("a"))
print("prashant jha".count("a"))

for i in range(1,4):
    for j in range(1,4):
        print(i,end=" ")
    print()

n=int(input("Enter the number of rows: "))
for i in range(1,n+1): 
    for j in range(1,n+1):
        print(chr(64+i), end=" ")
    print()

n=int(input("Enter the number of rows: "))
for i in range(1,n+1):
    for j in range(1,i+1): 
        print(chr(64+i), end=" ")
    print()

n=int(input("Enter the number of rows: "))
for i in range(1,n+1):
    for j in range(1,n+2-i): 
        print(chr(64+j), end=" ")
    print()

#      * 
#     * * 
#    * * * 
#   * * * * 
#  * * * * * 
import time
n=int(input("Enter the number of rows: "))
for i in range(1,n+1):
    print(" "*(n-i), end=" ")
    for j in range(1, i+1):
        time.sleep(1)
        print("*", end=" ")
    print()

#i/p [1,2,3,4]
#o/p [24,12,8,6] multiplication of all numbers except itself
