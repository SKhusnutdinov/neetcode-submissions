class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = 0
        fast = 0
        p3 = 0
        
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                while True:
                    slow = nums[slow]
                    p3 = nums[p3]
                    if p3 == slow:
                        return p3
