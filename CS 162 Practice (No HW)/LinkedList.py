class Node:
    """
    Represents a node in a linked list
    """
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self._head = None

    def add(self, val):

        if self._head is None:
            self._head = Node(val)
        else:
            current = self._head
            while current.next is not None:
                current = current.next
            current.next = Node(val)

    def display(self):
        current = self._head
        while current.next is not None:
            print(current.data, end=" ")
            current = current.next

    def remove(self, val):
        if self._head is None:
            return
        if self._head.data == val:
            self._head = self._head.next
        else:
            current = self._head
            while current is not None and current.data != val:
                previous = current
                current = current.next
            if current is not None:
                previous.next = current.next


linked_list_1 = LinkedList()
linked_list_1.add(1)
linked_list_1.add(2)
linked_list_1.add(3)
linked_list_1.add(4)
linked_list_1.display()
linked_list_1.remove(3)
