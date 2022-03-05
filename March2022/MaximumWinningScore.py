'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''

class Solution:
    def findMaxScore(self, root):
        #code here
        if root.left == None and root.right == None:
            return root.data
        elif root.right == None:
            return root.data*self.findMaxScore(root.left)
        elif root.left == None:
            return root.data*self.findMaxScore(root.right)
        else:
            return max(root.data*self.findMaxScore(root.left),root.data*self.findMaxScore(root.right))
