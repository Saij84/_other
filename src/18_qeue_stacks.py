import sys


class Solution:
    def __init__(self):
        self.qeue = []
        self.stack = []

    def pushCharacter(self, ch):
        self.stack.append(ch)

    def enqueueCharacter(self, ch):
        self.qeue.append(ch)

    def popCharacter(self):
        first_ch = self.stack[0]
        self.stack.pop(0)
        return first_ch

    def dequeueCharacter(self):
        last_index = len(self.qeue) - 1
        last_ch = self.qeue[last_index]
        self.qeue.pop(last_index)
        return last_ch

# Write your code here

# read the string s
s = "raR"
# Create the Solution class object
obj = Solution()

l = len(s)
# push/enqueue all the characters of string s to stack
for i in range(l):
    obj.pushCharacter(s[i])
    obj.enqueueCharacter(s[i])

isPalindrome = True
'''
pop the top character from stack
dequeue the first character from queue
compare both the characters
'''
for i in range(l // 2):
    if obj.popCharacter() != obj.dequeueCharacter():
        isPalindrome = False
        break
# finally print whether string s is palindrome or not.
if isPalindrome:
    print("The word, " + s + ", is a palindrome.")
else:
    print("The word, " + s + ", is not a palindrome.")
