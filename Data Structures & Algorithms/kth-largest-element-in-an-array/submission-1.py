class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxHeap = nums[:k]
        heapq.heapify(maxHeap)

        for x in nums[k:]:
            if x > maxHeap[0]:
                heapq.heapreplace(maxHeap, x)
        
        return maxHeap[0]