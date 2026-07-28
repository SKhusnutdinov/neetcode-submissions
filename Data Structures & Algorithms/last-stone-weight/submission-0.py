class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-x for x in stones]
        heapq.heapify(heap)

        while len(heap) > 1:
            left = heap[0]
            right = heap[1]
            if len(heap) > 2:
                right = min(heap[1], heap[2])
            
            heapq.heappop(heap)
            heapq.heappop(heap)

            if abs(left - right) > 0:
                heapq.heappush(heap, -abs(left - right))
        
        return -heap[0] if heap else 0