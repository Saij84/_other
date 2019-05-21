class Node:
    def __init__(self, data):
        self.right = None
        self.left = None
        self.data = data
class Solution:
    def insert(self,root,data):
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

    def getHeight(self, root):
        #Write your code here
        if not root:
            return -1

        if not root.left and not root.right:
            return 0

        height_left = self.getHeight(root.left)
        height_right = self.getHeight(root.right)

        return max(height_left, height_right) + 1


T=7
myTree = Solution()
root = None
for i in range(T):
    data = [3, 5, 2, 1, 4, 6, 7]
    root = myTree.insert(root, data[i])
height = myTree.getHeight(root)
print(height)