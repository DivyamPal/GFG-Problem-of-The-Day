class Solution:
    def minRepeats(self, A, B):
        c = 1
        sc = 0;
        s = A
        for i in range(int(len(B)/len(A))+1):
            x = s.count(B)
            if x>0:
                sc = sc+1
                break
            c = c+1
            s = s+A
        if sc>0:
            return c
        else:
            return -1
        # code here 
        # def Substr(Str, target):
        #     t = 0
        #     Len = len(Str)
        #     i = 0
        #     for i in range(Len):
        #         if (t == len(target)):
        #             break
        #         if (Str[i] == target[t]):
        #             t += 1
        #         else:
        #             t = 0
             
        #     if (t < len(target)):
        #         return -1
        #     else:
        #         return (i - t)
            
        # count=1
        # temp=A
        # while (Substr(A,B) <0):
        #     A=A+temp
        #     count+=1
        # return count
