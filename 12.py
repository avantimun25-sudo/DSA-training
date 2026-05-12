mylist = ["Avanti", "Ashish","komal","ankush","Ashish", 77,"sandip",68.52,"Avanti"]
print(mylist)
print(type(mylist))
print(mylist[0])
print(mylist[1]) #Ashish
print(mylist[2])# Komal
print (mylist[-1]) #Avanti
print(mylist[2:5]) # n=5,n-1=4 komal", "ankush", "Ashish
print(mylist[:5]) # n=5, n-1=4 "Avanti"
print(mylist[1:]) # n=8, n-1=8-1=7
print(mylist[1:8:2])#1,3,5

mylist[2]="Akshay"
print(mylist)

if "ankush" in mylist:
    print("present")
else:
    print("not present")

mylist.append("harsh")
mylist.append("laxman")
print(mylist)

mylist.insert(3,"sanket")
print(mylist)

mylist.remove("sandip")
print(mylist)

newlist = mylist.copy()
print(newlist)

mylist = [['prashant', 'jha'], ['85.56'], [440022,"yyy"]]

print("example of multidimensional list: ")
print(mylist)
print(mylist[0][0])
print(mylist[0][1])
print(mylist[1][0])
print(mylist[2][0])
print(mylist[2][1])

list2 =[5,3,6,'avanti']
del list2[2]
print(list2)

list2 =[5,3,6,'avanti']
list2.clear()
print(list2)

name="avanti"
print(name)
myname=list(name)
print(myname)

mylist=[44,22,77,0,9,88]
#mylist.sort()
mylist.sort(reverse=True)
print(mylist)

mylist=[44,22,77,8,9,88]
newlist = mylist
print(mylist)
print(newlist)

mylist=[44,22,77,8,9,88]
newlist = mylist
newlist[3] = 4
print(mylist)

mylist=[44,22,77,8,9,88]
for i in mylist:
    print(i)

i/p mylist = [0,1,4,0,2,5]
o/p mylist = [1,4,2,5,0,0]
mylist = [0,1,4,0,2,5]
for i in mylist:
    if i==0:
        mylist.remove(i)
        mylist.append(i)
print(mylist)

second largest
mylist = [7,3,9,2,8]
mylist.sort(reverse=True)
print(mylist[1])

a=[1,2,3,4,5,6,7,8,9]
a[::2]=10,20,30,40,50,60
print(a)
Error: attempt to assign sequence of size 6 to extended slice of size 5

a=[1,2,3,4,5]
print(a[3:0:-1])

arr = [[1,2,3,4],[4,5,6,7],[8,9,10,11],[12,13,14,15]]
for i in range(0,4):
    print(arr[i].pop())

arr=[1,2,3,4,5,6]
for i in range(1,6):
    arr[i-1]=arr[i]
for i in range(0,6):
    print(arr[i], end=" ")

fruit_list1=['apple','berry','cherry','papaya']
fruit_list2=fruit_list1
fruit_list3=fruit_list1[:]
fruit_list2[0]="guava"
fruit_list3[1]="kiwi"
sum=0
for ls in (fruit_list1, fruit_list2, fruit_list3):
    if ls[0]=='guava':
        sum+=1
    if ls[1]=='kiwi':
        sum+=20
print(sum)

a=[1,2,3]
b=[2,3,4]
c=[3,4,5]
for i in a:
    if i in b and i in c:
        print(i)

a=[]
n=int(input("enter the value of n: "))
for i in range(n):
    val = int(input("enter value: "))
    a.append(val)
print(a)
sum=0
for i in range(n-1):
     sum += abs(a[i]-a[i+1])
print(sum)