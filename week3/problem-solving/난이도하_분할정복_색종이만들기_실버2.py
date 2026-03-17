# 분할정복 - 색종이 만들기 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/2630
import sys

N = int(input())
paper=[]
for _ in range(N):
    paper.append(list(map(int, sys.stdin.readline().strip().split())))

blueCount = 0
whiteCount = 0

def cutPaper(y, x, paper_len):
    global blueCount, whiteCount
    # 파란색 종이일 때
    if paper[y][x] == 1:
        for i in range(y, y + paper_len):
            for j in range(x, x + paper_len):
                if paper[i][j] == 0:
                    cutPaper(y + paper_len//2, x + paper_len//2, paper_len//2)
                    cutPaper(y + paper_len//2, x, paper_len//2)
                    cutPaper(y, x + paper_len//2, paper_len//2)
                    cutPaper(y, x, paper_len//2)
                    return
        blueCount +=1

    # 흰색 종이일 때                
    else : 
        for i in range(y, y + paper_len):
            for j in range(x, x + paper_len):
                if paper[i][j] == 1:
                    cutPaper(y + paper_len//2, x + paper_len//2, paper_len//2)
                    cutPaper(y + paper_len//2, x, paper_len//2)
                    cutPaper(y, x + paper_len//2, paper_len//2)
                    cutPaper(y, x, paper_len//2)
                    return
        whiteCount +=1

cutPaper(0, 0, N)

print(whiteCount)
print(blueCount)