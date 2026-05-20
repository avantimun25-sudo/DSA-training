import sys
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def addNode(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def display(self):
        temp = self.head
        while temp is not None:
            print(temp.data, "| -->", end=" ")
            temp = temp.next
        print("None")

    def addnodebig(self, value):
        print("Add node at beginning:")
        node = Node(value)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head = node

    def addbetween(self, value, position):
        node = Node(value)
        if position == 1:
            node.next = self.head
            self.head = node
            if self.tail is None:
                self.tail = node
            print("Node inserted successfully")
            return
        temp = self.head
        count = 1
        while temp is not None and count < position - 1:
            temp = temp.next
            count += 1
        if temp is None:
            print("Invalid position")
            return
        node.next = temp.next
        temp.next = node
        if node.next is None:
            self.tail = node
        print("Node inserted successfully")

if __name__ == "__main__":
    obj = LinkedList()
    while True:
        print("\n1. Add node in linked list")
        print("2. Add node at beginning")
        print("3. Add node in between")
        print("4. Display linked list")
        print("5. Exit")
        ch = int(input("Enter your choice: "))
        if ch == 1:
            value = int(input("Enter value for node: "))
            obj.addNode(value)
            print("Node added successfully")
        elif ch == 2:
            value = int(input("Enter value for node: "))
            obj.addnodebig(value)
        elif ch == 3:
            value = int(input("Enter value for new node: "))
            position = int(input("Enter position: "))
            obj.addbetween(value, position)
        elif ch == 4:
            obj.display()
        elif ch == 5:
            sys.exit()
        else:
            print("Invalid choice")