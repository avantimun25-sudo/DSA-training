age=22
pi=3.14
name="Avanti"
result=True
print(type(age))
print(id(pi))
print(id(name))
print(type(result))

math = 55
chem = 55
phy = 55
print(id(math))
print(id(chem))
print(id(phy))

print(2+2)
print("2"+"2")
a = int(input("enter first number: "))
b = int(input("enter the second number: "))
print(a+b)

print(int(3.14))
#print(int(18+5g))
print(int(True))
print(int(False))
#print(int("4.22"))
print(int("4"))

print(float(3))
#print(float(50+4f))
print(float(True))
print(float(False))
print(float(4.22))
print(float("4"))
#print(float("name"))

print(complex(3))
print(complex(12.5))
print(complex(True))
print(complex(False))
print(complex("5"))
print(complex("5.6"))
#print(complex("name"))
print(complex(5,-3))
print(complex(True,False))

print(bool(0))
print(bool(15))
print(bool(3.14))
print(bool(0.0))
print(bool(1+2))
print(bool(0+0))
print(bool(-1))
print(bool(False))
print(bool(True))
print(bool(""))
print(bool("Avanti"))

a = int(input("Enter any digit: "))
if a>0:
    print("positive")
if a<0:
    print("negative")
if a==0:
    print("0")

a = input("Enter day: ")
if a=="Monday"or a=="monday" or a=="Tuesday"or a=="tuesday" or a=="Wednesday" or a=="wednesday" or a=="Thursday" or a=="thusrday" or a=="Friday" or a=="friday":
    print("Working day")
else:
    print("Weekend")

per = 65
if per>=65:
    print("grade A")
elif per<=65 and per>=50:
    print("grade B")
else:
    print("Fail")

a = ord(input("enter a character: "))
if a >= 65 and a<=90:
    print("uppercase")
elif a>=97 and a<=122:
    print("lowercase")
elif a>=48 and a <=57:
    print("mumber")
else:
    print("special character")
    
#membership operator = in, not in
name = "Avanti"
print('a' in name)

#identity operator = is, is not (address comparison)
math = 50
chem = 50
print(math is chem)

for i in range(5):
    print(i)
for i in range(2,10):
    print(i)
for i in range(2,11,2):
    print(i)
for i in range(5,0,-1):
    print(i)
for i in range(1,11):
    print(i*2)

for i in range(1,11):
    print(i*2,"  ",i*3,"  ",i*4,"  ",i*5,"  ",i*6,"  ",i*7,"  ",i*8,"  ",i*9,"  ",i*10)
print("------------------------------------------------------------------------------")
for i in range(1,11):
    print(i*11,"  ",i*12,"  ",i*13,"  ",i*14,"  ",i*15,"  ",i*16,"  ",i*17,"  ",i*18,"  ",i*19,"  ",i*20)

#write a program to accept marks of three papers and calculate total, percentage and check if he/she passed in all the sbjects. print pass of fail.
# if percentage is greaer than 65 and gender = male, he is eligible for placement

math = int(input("Enter marks for math: "))
chem = int(input("Enter marks for chem: "))
phy = int(input("Enter marks for phy: "))
gender = input("enter your gender: ")
total = math+chem+phy
per = total/300*100
print("total = ",total)
print("percentage = ",per)
if phy>=35 and math>=35 and chem>=35:
    print("pass")
else:
    print("fail")
if per>=65 and gender=="male":
    print("Eligible for placement")
else:
    print("not eligible for placement")

for i in range(1,5):
    if i ==3:
        break
    print(i)
for i in range(1,5):
    if i ==3:
        continue
    print(i)

#1 5
#2 4
#4 2
#5 1
#zip()  we can take multiple range function inside zip
for i,j in zip(range(1,6),range(5,0,-1)):
    if i ==3 and j==3:
        continue
    print(i,"  ",j)