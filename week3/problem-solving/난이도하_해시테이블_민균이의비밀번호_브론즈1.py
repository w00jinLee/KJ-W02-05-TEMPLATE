# 해시 테이블 - 민균이의 비밀번호 (백준 브론즈1)
# 문제 링크: https://www.acmicpc.net/problem/9933

N = int(input())

wordList = [input() for _ in range(N)]

for i in range(N):
    reveredWord = wordList[i][::-1]

    if wordList[i] in wordList and reveredWord in wordList  :
        print(len(wordList[i]), wordList[i][len(wordList[i])//2])
        break