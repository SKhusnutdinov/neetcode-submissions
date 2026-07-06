class Solution:
    def isPathCrossing(self, path: str) -> bool:
        current = [0,0]
        path_set = set()
        path_set.add(tuple(current))

        for p in path:
            if p == 'N':
                current[0] += 1
            elif p == 'S':
                current[0] -= 1
            elif p == 'E':
                current[1] -= 1
            else:
                current[1] += 1

            path_set.add(tuple(current))

        return len(path_set) != len(path) + 1