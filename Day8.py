a=[0,0,1,2,0,3,0,0,4]
for i in a:
    while a[0] == 0:
        a.pop(i)
    else:
        break
print(a)
    
# Complete Binary Tree
# All levels except possibly the last are completely filled 
# Nodes in the last level are filled from left to right

# Perfect Binary Tree
# All internal nodes have exactly two nodes
# All leaf nodes are at the same level

# Why BST?
# it performs faster than binary tree for insertion and deletion
#                 70
#         50             90
#     30      60    80        100
# 20     40

class BSTNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

def insertNode(rootNode, nodeValue):
    if rootNode.data == None:
        rootNode.data = nodeValue
    elif nodeValue <= rootNode.data:
        if rootNode.leftChild is None:
            rootNode.leftChild = BSTNode(nodeValue)
        else:
            insertNode(rootNode.leftChild, nodeValue)
    else:
        if rootNode.rightChild is None:
            rootNode.rightChild = BSTNode(nodeValue)
        else:
            insertNode(rootNode.rightChild, nodeValue)
            
def preOrderTraversal(rootNode):
    if not rootNode:
        return
    print(rootNode.data, end=" ")
    preOrderTraversal(rootNode.leftChild)
    preOrderTraversal(rootNode.rightChild)
    
def inOrderTraversal(rootNode):
    if not rootNode:
        return
    preOrderTraversal(rootNode.leftChild)
    print(rootNode.data, end=" ")
    preOrderTraversal(rootNode.rightChild)

def postOrderTraversal(rootNode):
    if not rootNode:
        return
    preOrderTraversal(rootNode.leftChild)
    preOrderTraversal(rootNode.rightChild)
    print(rootNode.data, end=" ")
    
def searchNode(rootNode, nodeValue):
    if rootNode.data == nodeValue:
        print("The value is found")
    elif nodeValue < rootNode.data:
        if rootNode.leftChild.data == nodeValue:
            print("The value is found")
        else:
            searchNode(rootNode.leftChild, nodeValue)
    else:
        if rootNode.rightChild.data == nodeValue:
            print("The value is found")
        else:
            searchNode(rootNode.rightChild, nodeValue)
 

newBST = BSTNode(None)
insertNode(newBST, 70)
insertNode(newBST, 50)
insertNode(newBST, 90)
insertNode(newBST, 30)
insertNode(newBST, 60)
insertNode(newBST, 80)
insertNode(newBST, 100)
insertNode(newBST, 20)
insertNode(newBST, 40)
print("preorder: ")
preOrderTraversal(newBST)
print()
print("inorder: ")
inOrderTraversal(newBST)
print()
print("postorder: ")
postOrderTraversal(newBST)
print()
searchNode(newBST, 100)

try:
    a= int(input("Enter first number: "))
    b= int(input("Enter second number: "))
    print(a/b)
except ZeroDivisionError:
    print("cant divide by zero")
except ValueError:
    print("Enter only integer value")
except:
    print("Error")
finally:
    print("im always executed")
# else:
#     print("Everything is okay")
# except (ZeroDivisionError, ValueError) as msg:
#     print(msg)

import logging
logging.basicConfig(filename="newfile.txt", level=logging.DEBUG)
try:
    a=int(input("enter first integer no")) 
    b=int(input("enter second integer no")) 
    print(a/b)
except (ZeroDivisionError, ValueError) as message:
    print(message)
    logging.exception(message)
print("Logging Level is set up. Check 'newfile.txt' for log details.")