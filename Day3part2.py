# Linear search
def linearsearch(array, target):
    for i in range(0, len(array)):
        if array[i] == target:
            return i
    return -1
array = [1,2,3,4,8,7,9]
target = 7
result = linearsearch(array, target)
if result == -1:
    print("target not found")
else:
    print("element found at index: ",result)

# Removing spaces from the string:
# 1. rstrip()===>To remove spaces at right hand side
# 2. 1strip()===>To remove spaces at left hand side
# 3. strip() ==>To reměve spaces both sides
city=input("Enter your city Name:") 
scity=city.strip()
if scity=='Hyderabad':
    print("Hello Hyderbadi..Adab")
elif scity=='Chennai':
    print("Hello Madrasi... Vanakkam")
elif scity=="Bangalore":
    print("Hello Kannadiga... Shubhodaya")
else:
    print("entered city is invalid")

# row wsie maximum Value
# [[100,198,333,323],
#  [122,232,221,111],
#  [223,565,245,764]]
a=[[100,198,333,323],[122,232,221,111],[223,565,245,764]]
a1=[]
for i in range(3):
    j=0
    max=a[i][j]
    for j in range(4):
        c_max = a[i][j]
        if max<c_max:
            max=c_max
    a1.append(max)
print(a1)

# input = avanti*is*a*good*programmer
# output = ****avantiisagoodprogrammer
s="avanti*is*a*good*programmer"
new_s=""
val=''
for i in s:
    if i!='*':
        new_s+=i
    else:
        val+=i
print(new_s)
print(str(val+new_s))

# input = aaabbbbccceeeee
# output = a3b4c3e5