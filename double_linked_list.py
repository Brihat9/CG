#!/usr/bin/env python

''' THIS IS DOUBLY LINKED LIST IMPLEMENTATION '''

class Node:
    def __init__(self, prev=None, next=None, data=None):
        self.prev = prev
        self.next = next
        self.data = data

    def __str__(self):
        return str(self.data)

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.count = int(0)

    def display(self):
        temp = self.head
        print("\nDLL Content: "),
        while (temp):
            print(str(temp.data)),
            temp = temp.next
        print(" #")

    def show_count(self):
        print(self.count)

    def get_count(self):
        return self.count

    def push(self, new_data):
        new_node = Node(data=new_data)
        new_node.prev = None
        new_node.next = self.head

        if self.head is not None:
            self.head.prev = new_node

        self.head = new_node
        self.count = self.count + 1

    def insertBefore(self, cursor, new_data):
        if cursor is None:
            print("Error: Node doesn't exist")
            return

        new_node = Node(data=new_data)

        new_node.prev = cursor.prev
        new_node.next = cursor

        if cursor.prev is not None:
            cursor.prev.next = new_node

        cursor.prev = new_node
        self.count = self.count + 1


    def insertAfter(self, cursor, new_data):
        if cursor is None:
            print("Error: Node doesn't exist")
            return

        new_node = Node(data=new_data)

        new_node.prev = cursor
        new_node.next = cursor.next
        cursor.next = new_node

        if new_node.next is not None:
            new_node.next.prev = new_node

        self.count = self.count + 1


    def append(self, new_data):
        new_node = Node(data=new_data)
        new_node.next = None

        if self.head is None:
            new_node.prev = None
            self.head = new_node
            self.count = self.count + 1
            return

        last = self.head
        while (last.next is not None):
            last = last.next

        new_node.prev = last
        last.next = new_node
        self.count = self.count + 1


def menu():
    print("Doubly Linked List\n")
    print("1. Show List")
    print("2. Insert at Start")
    print("3. Insert Before")
    print("4. Insert After")
    print("5. Insert at End")
    print("9. # of Element")
    print("0. Exit")
    print(">> "),

def main():
    dll = DoublyLinkedList()

    while(True):
        menu()
        choice = int(raw_input())
        if choice == int('1'):
            dll.display()
        elif choice == int('2'):
            print("Enter data to insert: "),
            data = raw_input()
            dll.push(data)
        elif choice == int('3'):
            print("Enter data to insert: "),
            data = raw_input()
            print("Enter position of cursor (before): "),
            pos = int(raw_input())

            if pos == int('1'):
                dll.push(data)
                continue

            cursor = dll.head
            for i in range(1, pos):
                cursor = cursor.next
                print(cursor)
            dll.insertBefore(cursor, data)
            # print("3")
        elif choice == int('4'):
            print("Enter data to insert: "),
            data = raw_input()
            print("Enter position of cursor (after): "),

            pos = int(raw_input())

            cursor = dll.head
            for i in range(pos - 1):
                cursor = cursor.next
                print(cursor)
            dll.insertAfter(cursor, data)
            # print("4")
        elif choice == int('5'):
            print("Enter data to insert: "),
            data = raw_input()
            dll.append(data)
            # print("5")
        elif choice == int('9'):
            print("No of element: "),
            dll.show_count()
        elif choice == int('0'):
            break
        else:
            print("Invalid Selection")

        print('\n\nEND\n\n')

if __name__ == '__main__':
    main()
