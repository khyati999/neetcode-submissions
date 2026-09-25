# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        cur = head
        grp=0
        while cur and grp<k:
            cur=cur.next
            grp+=1

        if grp==k:
            cur=self.reverseKGroup(cur, k)
            while grp>0:
                temp=head.next
                head.next=cur
                cur=head
                head=temp
                grp-=1
            head=cur
        return head