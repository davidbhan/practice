# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def get_sum_and_carry(self, l1_val, l2_val, old_carry):
        new_carry = 0
        temp_sum = l1_val + l2_val + old_carry
        if temp_sum > 9:
            temp_sum = temp_sum % 10
            new_carry = 1
        return temp_sum, new_carry
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        temp_sum = 0
        head = ListNode(0)
        temp = head
        while l1 or l2:
            temp.next = ListNode(0)
            temp = temp.next            
            if l1 is None:
                temp.val, carry = self.get_sum_and_carry(0, l2.val, carry)
                l2 = l2.next
            elif l2 is None:
                temp.val, carry = self.get_sum_and_carry(l1.val, 0, carry)
                l1 = l1.next
            else:
                temp.val, carry = self.get_sum_and_carry(l1.val, l2.val, carry)
                l1, l2 = l1.next, l2.next
        if carry > 0:
            temp.next = ListNode(1)
        return head.next

l1 = ListNode(5)
# l1.next = ListNode(4)
# l1.next.next = ListNode (3)
l2 = ListNode(5)
# l2.next = ListNode(6)
# l2.next.next = ListNode (4)
solution = Solution()
print(solution.addTwoNumbers(l1, l2).val)
                