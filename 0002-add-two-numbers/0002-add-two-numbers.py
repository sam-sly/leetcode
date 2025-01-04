# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        num = l1.val + l2.val
        remainder = num / 10

        head = ListNode(num % 10, None)
        last_node = head

        l1 = l1.next
        l2 = l2.next

        while True:
            if l1 == None and l2 == None:
                break

            num1 = 0
            if l1 != None:
                num1 = l1.val
                l1 = l1.next

            num2 = 0
            if l2 != None:
                num2 = l2.val
                l2 = l2.next

            num = num1 + num2 + remainder
            remainder = num / 10

            new_node = ListNode(num % 10, None)
            last_node.next = new_node
            last_node = new_node

        if remainder > 0:
            new_node = ListNode(remainder, None)
            last_node.next = new_node

        return head