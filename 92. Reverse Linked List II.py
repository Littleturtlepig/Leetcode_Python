# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        count = 1
        newhead = ListNode(0)
        newhead.next = head
        pre = newhead

        while pre.next and count < left:
            pre = pre.next
            count += 1

        cur = pre.next
        tail = cur

        while cur and count <= right:
            nxt = cur.next
            cur.next = pre.next
            pre.next = cur
            tail.next = nxt
            cur = nxt
            count += 1

        return newhead.next