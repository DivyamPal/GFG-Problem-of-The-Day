def reverse(s):
    stack=[]
    ns=""
    for i in range(len(s)):
        stack.append(s[i])
    for i in range(len(stack)):
        ns+=stack.pop()
    return ns
