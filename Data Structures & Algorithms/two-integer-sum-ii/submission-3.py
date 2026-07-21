class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        p1, p2 = 0, len(numbers) - 1
        curSum = 0

        while p1 < p2:
            curSum = numbers[p1] + numbers[p2]

            if curSum > target:
                p2 -= 1
            elif curSum < target:
                p1 += 1
            else:
                return [p1+1, p2+1]