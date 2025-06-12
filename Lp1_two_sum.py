class TwoSum:
    def twosum(self,nums,target):
        sumdict={}
        i=0
        for no in nums:
            result=target-no
            if result in sumdict:
                return [sumdict[result],i]
            sumdict[no]=i
            i+=1

nums=[2,10,3,4,6,7]
t=TwoSum()
print(t.twosum(nums,9))
