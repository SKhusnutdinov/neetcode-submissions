class Solution:
    def minOperations(self, logs: List[str]) -> int:
        depth = 0
        for op in logs:
            match op:
                case "../":
                    if depth > 0:
                        depth -= 1
                case "./":
                    depth = depth
                case _:
                    depth += 1
                
        return depth