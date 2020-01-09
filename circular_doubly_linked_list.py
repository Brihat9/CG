#!/usr/bin/env python

''' THIS IS CIRCULAR DOUBLY LINKED LIST IMPLEMENTATION '''

class Node:
    ''' Node Class '''
    def __init__(self, prev=None, next=None, data=None):
        self.prev = prev
        self.next = next
        self.data = data

    def __str__(self):
        return str(self.data)

class CircularDoublyLinkedList:
    ''' Implementation of Circular Doubly Linked List (CDLL) '''
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = int(0)

    def display(self, text="CDLL Content: "):
        ''' displays content of CDLL '''
        temp = self.head
        print("\n" + text + ": ["),
        while (temp != self.tail):
            print(str(temp.data)),
            temp = temp.next

        if(temp != None):
            print(str(temp.data)),
        print("] #")

    def display2(self):
        ''' temp content display function (for testing only) '''
        temp = self.head
        print("\nCDLL Content: "),

        for index in range(self.count * 2):
            print(str(temp.data)),
            temp = temp.next
        print(" #")

    def show_head(self):
        ''' displays current HEAD of CDLL '''
        if self.head is not None:
            print(self.head.data)
        else:
            print("None")

    def show_tail(self):
        ''' displays current TAIL of CDLL '''
        if self.tail is not None:
            print(self.tail.data)
        else:
            print("None")

    def show_count(self):
        ''' displays total number of nodes in CDLL '''
        print("No of element: "),
        print(self.count)

    def get_count(self):
        ''' returns total number of nodes in CDLL '''
        return self.count

    def push(self, new_data):
        ''' inserts new node in the beginning of the CDLL '''
        new_node = Node(data=new_data)
        new_node.prev = self.tail
        new_node.next = self.head

        if self.head is not None:
            self.head.prev = new_node

        self.head = new_node

        if self.tail is not None:
            self.tail.next = new_node

        if self.tail is None:
            self.tail = new_node
        self.count = self.count + 1

    def insertBefore(self, cursor, new_data):
        ''' inserts new node before `cursor` node '''
        if cursor is None:
            print("Error: Node doesn't exist")
            return

        if cursor == self.head:
            return self.push(new_data)

        new_node = Node(data=new_data)

        new_node.prev = cursor.prev
        new_node.next = cursor

        if cursor.prev is not None:
            cursor.prev.next = new_node

        cursor.prev = new_node
        self.count = self.count + 1

    def insertAfter(self, cursor, new_data):
        ''' inserts new node after `cursor` node '''
        if cursor is None:
            print("Error: Node doesn't exist")
            return

        if cursor.next == self.head:
            return self.append(new_data)

        new_node = Node(data=new_data)

        new_node.prev = cursor
        new_node.next = cursor.next
        cursor.next = new_node

        if new_node.next is not None:
            new_node.next.prev = new_node

        self.count = self.count + 1

    def append(self, new_data):
        ''' inserts new node at the end of CDLL '''
        new_node = Node(data=new_data)
        new_node.next = self.head

        if self.head is None:
            return self.push(new_data)

        if self.tail is None:
            self.tail = new_node

        new_node.prev = self.tail
        if self.tail is not None:
            self.tail.next = new_node
            self.tail = new_node
        self.count = self.count + 1

    def pop(self):
        ''' deletes head of the CDLL '''
        temp = None
        if self.count == 0:
            print("CDLL empty, cannot pop")
            return

        elif self.count == 1:
            temp = self.head.data
            self.head = None
            self.tail = None
            self.count = 0

        else:
            temp = self.head.data
            new_head = self.head.next
            self.tail.next = new_head
            new_head.prev = self.tail
            self.head = new_head
            self.count = self.count - 1

        print("deleted: " + str(temp))

def menu():
    ''' MAIN MENU '''
    print("Circular Doubly Linked List")
    print("Brihat Ratna Bajracharya")
    print("\nMAIN MENU\n---------\n")

    print("1. Show List")
    print("2. Insert at Start")
    print("3. Insert Before")
    print("4. Insert After")
    print("5. Insert at End")
    # print("6. Show Head")
    # print("7. Show Tail")
    print("8. Delete Head")
    print("9. # of Element")
    print("0. Exit")

    print(">> "),

def main():
    ''' MAIN FUNCTION '''
    cdll = CircularDoublyLinkedList()

    while(True):
        menu()
        choice = int(raw_input())

        if choice == int('1'):
            cdll.display(text="brihat")

        elif choice == int('2'):
            print("Enter data to insert: "),
            data = raw_input()
            cdll.push(data)

        elif choice == int('3'):
            print("Enter data to insert: "),
            data = raw_input()
            print("Enter position of cursor (before): "),
            pos = int(raw_input())

            if pos == int('1'):
                cdll.push(data)
                continue

            cursor = cdll.head
            for i in range(1, pos):
                cursor = cursor.next
                # print(cursor)
            cdll.insertBefore(cursor, data)

        elif choice == int('4'):
            print("Enter data to insert: "),
            data = raw_input()
            print("Enter position of cursor (after): "),

            pos = int(raw_input())

            cursor = cdll.head
            for i in range(pos - 1):
                cursor = cursor.next
                # print(cursor)
            cdll.insertAfter(cursor, data)

        elif choice == int('5'):
            print("Enter data to insert: "),
            data = raw_input()
            cdll.append(data)

        # elif choice == int('6'):
        #     print("Head: "),
        #     cdll.show_head()
        #
        # elif choice == int('7'):
        #     print("Tail: "),
        #     cdll.show_tail()

        elif choice == int('8'):
            cdll.pop()

        elif choice == int('9'):
            cdll.show_count()

        elif choice == int('0'):
            break

        else:
            print("Invalid Selection")

        print('\n\nEND\n\n')

if __name__ == '__main__':
    main()
