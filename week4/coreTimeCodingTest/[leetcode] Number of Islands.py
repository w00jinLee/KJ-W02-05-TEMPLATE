class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
 
        m = len(grid)
        n = len(grid[0])

        visited = [[False for _ in range(n)] for _ in range(m)]
        islandCount = 0
        
        def dfs(y, x):
            if y < 0 or y >= m or x < 0 or x >= n :
                return

            if grid[y][x] == "0" or visited[y][x] == True:
                return

            visited[y][x] = True
            #상
            dfs(y-1, x) 
            #하
            dfs(y+1, x)
            #좌
            dfs(y, x-1)
            #우
            dfs(y, x+1)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1" and visited[i][j] ==False:
                    islandCount +=1
                    dfs(i, j)

        return islandCount