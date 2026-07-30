class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        orig = image[sr][sc]
        if orig == color:
            return image
        ROW, COL = len(image), len(image[0])

        def dfs(sr, sc):
            if min(sr, sc) < 0 or sr >= ROW or sc >= COL or image[sr][sc] != orig:
                return
            
            image[sr][sc] = color

            dfs(sr + 1, sc)
            dfs(sr, sc + 1)
            dfs(sr - 1, sc)
            dfs(sr, sc - 1)

        dfs(sr, sc)
        
        return image