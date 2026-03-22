# 트리 - 트리 만들기 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/14244

n, m = input().split()

n, m = int(n), int(m)
# n개의 노드, m개의 리프


for i in range(n - m) :
    print(i, i + 1)

for i in range(n - m + 1, n):
    print(n - m, i)