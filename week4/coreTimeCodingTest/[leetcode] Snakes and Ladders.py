class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        # board = [[36,35,34,33,32,31],
#         [25,26,27,28,29,30],
#         [24,23,22,21,20,19],
#         [13,14,15,16,17,18],
#         [12,11,10,9,8,7],
#         [1,2,3,4,5,6]]

        # print(board)

        from collections import deque


        n = len(board)


        reverseBoard = list(reversed(board))

        for i in range(1, n, 2):
            reverseBoard[i] = list(reversed(reverseBoard[i]))

        # print(reverseBoard)

        sortedBoard = {}

        num=1 
        for i in range(n):
            for j in range(n):
                sortedBoard[num] = reverseBoard[i][j]
                num+=1

        queue = deque()
        visited=[False for _ in range(n*n+1)]
        # print(sortedBoard)

        queue.append(1)
        visited[1]=True
        count=0

        while queue:
            for _ in range(len(queue)):
                current = queue.popleft()

                if current == n * n:
                    return count

                for dice in range(1, 7):
                    next_pos = current + dice

                    if next_pos > n * n:
                        break

                    if sortedBoard[next_pos] != -1:
                        next_pos = sortedBoard[next_pos]

                    if not visited[next_pos]:
                        visited[next_pos] = True
                        queue.append(next_pos)

            count += 1

        return -1