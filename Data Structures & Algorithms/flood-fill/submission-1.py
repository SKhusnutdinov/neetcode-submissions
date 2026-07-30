class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        def dfs(sr, sc, startColor, color):
            ROW, COL = len(image), len(image[0])

            if min(sr, sc) < 0 or sr >= ROW or sc >= COL:
                return
            if image[sr][sc] == color or image[sr][sc] != startColor:
                return
            
            image[sr][sc] = color

            dfs(sr + 1, sc, startColor, color)
            dfs(sr, sc + 1, startColor, color)
            dfs(sr - 1, sc, startColor, color)
            dfs(sr, sc - 1, startColor, color)

        dfs(sr, sc, image[sr][sc], color)
        
        return image