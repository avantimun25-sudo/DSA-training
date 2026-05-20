a='leetcode'
for i in a:
    if a.count(i) == 1:
        print("first non repeting chaaracter: ",i)
        break

def factorial(num):#num=4
    if num <= 1:# base condition 
        return 1
    return num * factorial(num-1)
print(factorial(4))

def capitalizeFirst(arr):
    result=[]
    if len(arr) == 0:
        return result
    result.append(arr[0][0].upper() + arr[0][1:])
    return result + capitalizeFirst(arr[1:])
print(capitalizeFirst(['car', 'taco', 'banana']))

def power(base, exponent):
    if exponent == 0:
        return 1
    return base * power(base, exponent-1)
print (power(2,0))
print (power(2,2))
print (power(2,4)) 

def productofArray(arr):
    if len(arr) == 0:
        return 1
    return arr[0] * productofArray(arr[1:])
print(productofArray([1,2,3]))
print (productofArray([1,2,3,10]))

def reverse(strng):
    if len(strng) < 1:
        return strng
    return strng[len(strng)-1] + reverse(strng[0:len(strng)-1])
print(reverse('python')) # 'nohtyp'
print(reverse('appmillers')) # 'srellimppa'

# can store tree by uing linkedlist and array
# creating tree using list

# LinkedList
class Tree:
    def __init__(self, data):
        self.data = data
        self.children = []

    def __str__(self, level=0):
        ret = " " * level + str(self.data) + "\n"
        for ch in self.children:
            ret += ch.__str__(level + 1)
        return ret

    def addChild(self, node):
        self.children.append(node)
        print("Tree Node Added")


rootNode = Tree("Drinks")

Hot = Tree("Hot")
Cold = Tree("Cold")

Tea = Tree("Tea")
Coffee = Tree("Coffee")

NonAlcoholic = Tree("NonAlcoholic")
Alcoholic = Tree("Alcoholic")

rootNode.addChild(Hot)
rootNode.addChild(Cold)

Hot.addChild(Tea)
Hot.addChild(Coffee)

Cold.addChild(NonAlcoholic)
Cold.addChild(Alcoholic)

print(rootNode)