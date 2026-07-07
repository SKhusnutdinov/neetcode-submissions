class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        total = 0
        reminders = {0:-1}

        for i in range(len(nums)):
            total += nums[i]
            rem = total % k

            if rem in reminders:
                a = reminders[rem]
                b = i

                if b - a > 1:
                    return True
            else:
                reminders[rem] = i
        
        return False