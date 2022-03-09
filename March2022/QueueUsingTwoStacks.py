#User function Template for python3

#Function to push an element in queue by using 2 stacks.
def Push(x,stack1,stack2):
    '''
    x: value to push
    stack1: list
    stack2: list
    '''
    #code here
    stack1.append(x)
    return stack1

#Function to pop an element from queue by using 2 stacks.
def Pop(stack1,stack2):
    
    '''
    stack1: list
    stack2: list
    '''
    #code here
    if len(stack1)>=1:
        return stack1.pop(0)
    else:
        return -1
