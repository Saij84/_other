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

    def get_index(self, head, index):
        self.head = head
        if self.head == None:
            return -1

        count = 0
        n_list = self.head
        while count != index:
            n_list = n_list.next
            count += 1
        return n_list

    def get_len(self, head):
        self.head = head
        count = 1
        if head == None:
            return -1

        n_list = self.head
        while n_list.next:
            n_list = n_list.next
            count += 1
        return count

    def insert(self, head, data):
        # Complete this method
        new_node = Node(data)
        if head == None:
            self.head = new_node
            return self.head
        n_list = self.head
        while n_list.next:
            n_list = n_list.next
        n_list.next = new_node
        return self.head

    def insert_after(self, head, data, index):
        index_count = 0
        new_node = Node(data)
        if head == None:
            self.head = new_node
            print("Linked list empty, inserting Node at index 1")
            return self.head
        n_list = self.head
        while not index_count == index:
            n_list = n_list.next
            index_count += 1

        next_node = n_list.next
        new_node.next = next_node
        n_list.next = new_node
        return self.head


mylist= Solution()
T = 4

head = None

for i in range(T):
    data = [3, 2, 1, 0]
    head = mylist.insert(head, data[i])
head = mylist.insert_after(head, 10, 1)
print(mylist.get_len(head))
data = mylist.get_index(head, 2).data
print("data:", data)
mylist.display(head)