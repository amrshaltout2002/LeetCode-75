# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        lst = []
        curr = head
        result = []
        while curr:
            lst.append(curr.val)
            curr = curr.next

        n = len(lst)
        for i in range(n-1):
            result.append(lst[i] + lst[n-1-i])

        return max(result)