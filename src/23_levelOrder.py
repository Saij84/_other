import sys


class Node:
    def __init__(self, data):
        self.right = self.left = None
        self.data = data


class Solution:
    def insert(self, root, data):
        if root == None:
            return Node(data)
        else:
            if data <= root.data:
                cur = self.insert(root.left, data)
                root.left = cur
            else:
                cur = self.insert(root.right, data)
                root.right = cur
        return root

    def levelOrder(self, root):
        # Write your code here
        queue = []
        node_traversed = ""
        queue.append(root)

        while queue:
            tree = queue.pop(0)

            if tree.left:
                queue.append(tree.left)
            if tree.right:
                queue.append(tree.right)
            node_traversed += str(tree.data) + " "
        print(node_traversed)


            # self.queue.append(root.data)
            # left_vals = self.levelOrder(root.left)
            # right_vals = self.levelOrder(root.right)


        # queue.append()
        # queue.append()
        #
        # print(queue)




T = 6
myTree = Solution()
root = None
for i in range(T):
    data = [3, 2, 5, 1, 4, 7]
    root = myTree.insert(root, data[i])
myTree.levelOrder(root)
