class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    def display(self, head):
        current = head
        while current:
            print(current.data, end=' ')
            current = current.next

    def insert(self, head, data):
        # Complete this method
        new_node = Node(data)
        if head == None:
            self.head = new_node
            return self.head
        n = self.head
        while n.next:
            n = n.next
        n.next = new_node
        return self.head

mylist= Solution()
T = 4

head = None

for i in range(T):
    data = [3, 2, 1, 0]
    head = mylist.insert(head, data[i])
mylist.display(head)