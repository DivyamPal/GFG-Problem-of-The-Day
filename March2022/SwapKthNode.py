#User function Template for python3
'''
Function Arguments :
		@param  : head (given head of linked list), k(value of k)
		@return : None, Just swap the nodes
		
# Node Class
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None

'''
#Function to swap Kth node from beginning and end in a linked list.
from typing import *

def swapkthnode(head, num, k):
    if n<k:
        return head
    if (2 * k - 1) == n:
        return head
    x = head
    x_prev = Node(None)
    for i in range(k - 1):
        x_prev = x
        x = x.next
    y = head
    y_prev = Node(None)
    for i in range(n - k):
        y_prev = y
        y = y.next
    if x_prev is not None:
        x_prev.next = y
    if y_prev is not None:
        y_prev.next = x
    temp = x.next
    x.next = y.next
    y.next = temp
    if k == 1:
        head = y
    if k == n:
        head = x
    return head
    
    
    #Wrong Answer
    # if ((head==None) or (k==0) or (k>n) or (2*k-1==n)):
    #     return head
    # node = x = y = head; xprev = yprev=None
    # i=1; j=1; kn=n-k+1; 
    
    # while(node):
    #     if(i<k):
    #         xprev = node
    #         x = node.next
    #         i+=1
    #     if(j<kn):
    #         yprev = node
    #         y = node.next
    #         j+=1
    #     node = node.next

    # x.data, y.data = y.data, x.data
    # return head
