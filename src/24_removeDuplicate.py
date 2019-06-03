class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Solution:
    def insert(self, head, data):
        p = Node(data)
        if head == None:
            head = p
        elif head.next == None:
            head.next = p
        else:
            start = head
            while (start.next != None):
                start = start.next
            start.next = p
        return head

    def display(self, head):
        current = head
        while current:
            print(current.data, end=' ')
            current = current.next

    def removeDuplicates(self, head):
        # Write your code here
        current = head
        while current:
            current_next = current.next
            if current.data == current_next.data:
                print("YES")
            current = current.next



mylist = Solution()
T = 6
head = None
for i in range(T):
    data = [1, 2, 2, 3, 3, 4]
    head = mylist.insert(head, data[i])
head = mylist.removeDuplicates(head)
mylist.display(head)
