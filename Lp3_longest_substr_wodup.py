class LongestSubstring:
    def lenofsubstring(self,s):
        seen=set()
        left=0
        maxlen=0
        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left+=1
            seen.add(s[right])
            maxlen=max(maxlen,right-left+1)

        return maxlen

s1="abcabcd"
s2="abca"
obj=LongestSubstring()
print(obj.lenofsubstring(s1))
print(obj.lenofsubstring(s2))

