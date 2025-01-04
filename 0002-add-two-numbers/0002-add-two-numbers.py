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
        remainder = 0
        nums = []

        while True:
            num = l1.val + l2.val + remainder
            remainder = num / 10
            num = num % 10
            nums.insert(0, num)

            if l1.next == None or l2.next == None:
                break
            
            l1 = l1.next
            l2 = l2.next

        if l1.next != None:
            while True:
                l1 = l1.next
                num = l1.val + remainder
                remainder = num / 10
                num = num % 10
                nums.insert(0, num)

                if l1.next == None:
                    break

        if l2.next != None:
            while True:
                l2 = l2.next
                num = l2.val + remainder
                remainder = num / 10
                num = num % 10
                nums.insert(0, num)

                if l2.next == None:
                    break
        
        if remainder > 0:
            nums.insert(0, remainder)

        ans = ListNode(nums[0], None)
        i = 1

        while i < len(nums):
            ans = ListNode(nums[i], ans)
            i += 1
        
        return ans