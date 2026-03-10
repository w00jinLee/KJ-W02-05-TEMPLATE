# 재귀함수 - 하노이 탑 (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/1914

N = int(input())


k=0
cur=[]

            #원반개수 시작기둥 목표기둥 보조기둥
def hanoiTop(count, moveFrom, moveTo, sub):
    global k
    k+=1
    #시작,보조,목표
    if count == 1:
        print(moveFrom, moveTo)
        return
    # 가장 큰 원판을 제외한 모든 원판을 보조 기둥으로 옮겨야함.
    hanoiTop(count-1, moveFrom, sub, moveTo)
    print(moveFrom, moveTo)
    hanoiTop(count-1, sub, moveTo, moveFrom)



hanoiTop(N, 1, 3, 2)
print(k)