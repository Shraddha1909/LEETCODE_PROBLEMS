class LongestPallindrome:
    def longeststring(self,s):
        start,end=0,0
        for i in range(len(s)):
            len1=self.findlen(s,i,i)
            len2=self.findlen(s,i,i+1)
            maxlen=max(len1,len2)

            if maxlen > end-start:
                start=i-(maxlen-1)//2
                end=i+maxlen//2

        return s[start:end+1]
    
    def findlen(self,s,left,right):
        while left >=0 and right < len(s) and s[left]==s[right]:
            left-=1
            right+=1
        return right-left-1

s="abbaccdcca"
obj=LongestPallindrome()
print(obj.longeststring(s))
