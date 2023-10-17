class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        s=""
        curr=head
        while(curr):
            s+=str(curr.val)
            curr=curr.next
        return int(s,2)