class ListNode:
    def __init__(self,val=0,next=None):
        self.val=val;
        self.next=next
class Solution:
    def addTwoNum(self,l1,l2):
        temp = ListNode()
        current = temp
        carry = 0

        while l1 or l2 or carry:
            val1=l1.val if l1 else 0
            val2=l2.val if l2 else 0
            total=val1+val2+carry
            carry=total//10

            current.next=ListNode(total%10)
            current=current.next

            if l1 : l1=l1.next
            if l2 : l2=l2.next

        return temp.next
def create_linked_list(lst):
    dummy = ListNode()
    current = dummy
    for val in lst:
        current.next = ListNode(val)
        current = current.next
    return dummy.next
def print_linked_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    print(result)

s=Solution()
l1=create_linked_list([1,2,3])
l2=create_linked_list([5,6,7])
result=s.addTwoNum(l1,l2)
print_linked_list(result)
