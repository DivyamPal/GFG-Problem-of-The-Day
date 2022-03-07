#User function Template for python3
'''
	Your task is to merge the given k sorted
	linked lists into one list and return
	the the new formed linked list class.

	Function Arguments:
	    arr is a list containing the n linkedlist head pointers
	    n is an integer value
    
    node class:
    
class Node:
    def __init__(self,x):
        self.data = x
        self.nxt = None
'''
class Solution:
    #Function to merge K sorted linked list.
    def mergeKLists(self,arr,K):
        # code here
        # return head of merged list
        l=[]
        for i in arr:
            temp=i
            while temp:
                l.append(temp.data)
                temp=temp.next
        l.sort()
        head=Node(l[0])
        str=head
        for i in range(1,len(l)):
            node=Node(l[i])
            str.next=node
            str=node
        return head
