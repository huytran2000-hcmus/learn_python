'''This module provide MyLinkedList class, which is a implementation of single linked list.

Classes:
    MyLinkedList
'''

class MyLinkedList:
    '''An implementation of singly linked list.'''

    def __init__(self):
        '''Initialize an empty link list.'''
        self.head = None
        self.length = 0

    def get(self, index: int) -> int:
        '''Return the value of node index-th node in the link list.

        If the index is invalid return -1.
        '''

        if index < 0 or index >= self.length or self.length == 0:
            return -1

        curr_node = self.head
        for _ in range(index):
            curr_node = curr_node.next

        return curr_node.val

    def add_at_head(self, val: int) -> None:
        '''Add a new node of value val at the head of linked list.'''
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node

        self.length += 1

    def add_at_tail(self, val: int) -> None:
        '''Append a new node of value val at the end of linked list'''
        new_node = Node(val)

        if self.length == 0:
            self.head = new_node
        else:
            curr_node = self.head
            while curr_node.next:
                curr_node = curr_node.next

            curr_node.next = new_node

        self.length += 1

    def add_at_index(self, index: int, val: int) -> None:
        '''Add a new node of value val at before the index-th node in linked list.'''
        if index < 0 or index > self.length:
            return

        if index == 0:
            self.add_at_head(val)
        else:
            prev_node = self.head
            for _ in range(index - 1):
                prev_node = prev_node.next

            new_node = Node(val)
            new_node.next = prev_node.next
            prev_node.next = new_node
            self.length += 1

    def delete_at_index(self, index: int) -> None:
        '''Remove the index-th node in linked list.'''
        if index < 0 or index >= self.length:
            return

        if index == 0:
            rm_node = self.head
            self.head = self.head.next
            del rm_node
        else:
            prev_node = self.head
            for _ in range(index - 1):
                prev_node = prev_node.next

            rm_node = prev_node.next
            prev_node.next = prev_node.next.next
            del rm_node

        self.length -= 1


class Node:
    '''Implementation of node for MyLinkedList'''

    def __init__(self, val: int):
        self.val = val
        self.next = None


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
