class MedianOfTwoSortedArray:
    def findMedian(self,A1,A2):
        comArr=[]
        i,j=0,0
        while i < len(A1) and j <len(A2):
            if A1[i] <A2[j]:
                comArr.append(A1[i])
                i+=1
            else:
                comArr.append(A2[j])
                j+=1
        if i <len(A1):
            comArr.extend(A1[i:])
        if j < len(A2):
            comArr.extend(A2[j:])

        fl=len(comArr)
        half=fl//2
        if(fl%2==0):
            return (comArr[half-1]+comArr[half])/2
        else:
            return comArr[half]

obj=MedianOfTwoSortedArray()
l1=[1,2,3,4]
l2=[5,8]
l3=[6,7,9]
print(obj.findMedian(l1,l2))
print(obj.findMedian(l2,l3))
