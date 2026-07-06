class Solution:
    def isPathCrossing(self, path: str) -> bool:
        x, y = 0, 0
        hs = set()
        hs.add((x,y))

        for ch in path:
            match ch:
                case 'N':
                    x += 1
                case 'S':
                    x -= 1
                case 'E':
                    y -= 1
                case 'W':
                    y += 1
                
            if (x, y) in hs:
                return True
            hs.add((x,y))
        
        return False