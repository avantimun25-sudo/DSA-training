mytuple = ("prashant", "Ashish", "Rahul", "sandip", 23,3.15,77, "sandíp")
print (mytuple)
print(type(mytuple))
#mytuple[2]="sunil"
#print(mytuple)

init_tuple=()
print(init_tuple.__len__())

init_tuple_a= 'a', 'b'
init_tuple_b= ('a', 'b')
print (init_tuple_a == init_tuple_b)

init_tuple_a='1', '2'
init_tuple_b= ('3', '4')
print (init_tuple_a+ init_tuple_b)

a= [1, 2, 3]
init_tuple = ('Python',) * (a.__len__() - a[::-1][0])
print(init_tuple)

init_tuple = ('Python',) * 3
print(type(init_tuple))

init_tuple = (1,) * 3
init_tuple[0]= 2
print(init_tuple)

init_tuple = ((1, 2),) * 7
print(len(init_tuple[3:8]))

#Dict
mydict = {
    101:"prashant",
    102:"ashish",
    "103":"mohini",
    "104":"trivani",
    101: "ashish",
    104: "ashish"
}
print(mydict)

a=mydict[102]
print(a)
mydict[102]="peter"
print(mydict)

for i in mydict:
    print(i)
    
for i in mydict.values():
    print(i)

for x,y in mydict.items():
    print(x,y)

#adding a new key value pair
mydict["mobile_no"]=1212121212
print(mydict)

mydict.pop(101)
print(mydict)

a= {(1,2):1, (2,3):2, (4,5):3}
print(a[4,5])

a={'a':1,'b':2,'c':3}
print(a['a','b']) #two kyes are nt allowed to access

arr = {}
arr[1] = 1
arr['1'] = 2
arr[1] += 1
print(arr)
sum = 0
for k in arr:
    sum += arr[k]
print(sum)

my_dict = {}
my_dict[1]=1
my_dict['1'] = 2
my_dict[1.0] = 4
print(my_dict)
sum = 0
for k in my_dict:
    sum += my_dict[k]
print (sum)

my_dict = {}
my_dict[(1,2,4)] = 8
my_dict[(4,2,1)] = 10
my_dict[(1,2)] = 12
sum=0
for k in my_dict:
    sum += my_dict[k]
print (sum)
print(my_dict)

box = {}
jars = {}
crates = {}
box['biscuit'] = 1
box['cake'] = 3
jars['jam'] = 4
crates['box'] = box
crates ['jars'] = jars
print(len(crates[box]))

rec = {"Name": "Python", "Age":"20", "Addr": "NJ", "Country": "USA"}
id1=id(rec)
print(id1)
del rec
rec = {"Name" : "Python", "Age":"20", "Addr" : "NJ", "Country" : "USA"}
id2 = id(rec)
print(id2)
print(id1 == id2)

a={"A":50,"B":30,"C":70}

num =123456
a = num%10
num=num//10
b= num % 10
num=num//10 
c = num%10
num=num//10
d = num%10
num=num//10
e = num%10
f=num=num//10
rev = a*100000 + b*10000 + c*1000 + d*100 + e*10 + f
print(rev)

Amount = int(input("Please Enter Amount for Withdraw :")) #630
print(" 500 notes= ", Amount//500)
print(" 100 notes= ", (Amount % 500)//100)
print(" 50 notes= ", ((Amount % 500) //100)//50)
print(" 20 notes= ", (((Amount % 500) % 100) %50)//20)
print(" 10 notes= ", ((((Amount % 500) % 100) %50) %20 )//10)
print(" 5 notes= ", (((((Amount % 500) % 100) %50) %20 ) %10) //5)