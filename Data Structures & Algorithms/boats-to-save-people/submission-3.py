class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        p1, p2 = 0, len(people) - 1
        res = 0

        while p1 <= p2:
            val1 = people[p1]
            val2 = people[p2]
            
            total = val1 + val2

            if total <= limit:
                p1 += 1
                p2 -= 1
            else:
                p2 -= 1
            res += 1
        
        return res