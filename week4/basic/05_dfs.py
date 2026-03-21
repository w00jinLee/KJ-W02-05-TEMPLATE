# """
# [DFS - 깊이 우선 탐색 (Depth-First Search)]

# 문제 설명:
# - DFS로 그래프를 탐색합니다.
# - 깊이 방향으로 끝까지 탐색합니다.
# - 재귀 또는 스택을 사용합니다.

# 입력:
# - graph: 그래프 (인접 리스트)
# - start: 시작 정점

# 출력:
# - 방문 순서

# 예제:
# 그래프:
#   0 ─── 1
#   │     │
#   └─ 2 ─┘
#       │
#       3

# 시작: 0
# DFS: [0, 1, 2, 3] (순서는 구현에 따라 다를 수 있음)

# 힌트:
# - 재귀로 구현
# - 방문 체크 필요
# - 깊이 우선으로 방문
# """

# def dfs(graph, start, visited=None):
#     """
#     깊이 우선 탐색 (재귀)
    
#     Args:
#         graph: 그래프 딕셔너리
#         start: 현재 정점
#         visited: 방문 리스트
    
#     Returns:
#         방문 순서 리스트
#     """
#     # TODO: visited가 None이면 초기화
#     if visited is None :
#         visited = []
    
#     # TODO: 현재 정점 방문
#     visited.append(start)

#     # TODO: 인접한 정점들에 대해 재귀
#     ## 방문하지 않은 정점이면 재귀 호출
#     for i in graph[start]: 
#         if i not in visited:
#             dfs(graph, i, visited)

#     return visited

# # 테스트 케이스
# if __name__ == "__main__":
#     # 그래프 생성
#     graph = {
#         0: [1, 2],
#         1: [0, 2],
#         2: [0, 1, 3],
#         3: [2]
#     }
    
#     print("=== DFS (깊이 우선 탐색) ===")
#     result = dfs(graph, 0)
#     print(f"시작 정점: 0")
#     print(f"방문 순서: {result}")

"""
[DFS - 깊이 우선 탐색 (Depth-First Search)]

문제 설명:
- DFS로 그래프를 탐색합니다.
- 깊이 방향으로 끝까지 탐색합니다.
- 스택(Stack)을 사용합니다.

입력:
- graph: 그래프 (인접 리스트)
- start: 시작 정점

출력:
- 방문 순서

예제:
그래프:
  0 ─── 1
  │     │
  └─ 2 ─┘
      │
      3

시작: 0
DFS: [0, 1, 2, 3] (순서는 구현에 따라 다를 수 있음)

힌트:
- 스택으로 구현
- 방문 체크 필요
- 깊이 우선으로 방문
"""

def dfs(graph, start, visited=None):
    """
    깊이 우선 탐색 (스택)
    
    Args:
        graph: 그래프 딕셔너리
        start: 시작 정점
        visited: 방문 리스트
    
    Returns:
        방문 순서 리스트
    """
    # TODO: visited가 None이면 초기화
    if visited is None:
        visited = [False for _ in range(len(graph))]

    stack = []
    result = [] # 방문순서 리스트
    # TODO: 스택에 시작 정점 추가
    stack.append(start)
    visited[start] = True
    # TODO: 스택이 빌 때까지 반복
    while stack:
    ## 스택에서 정점 꺼내기
        v = stack.pop()
        result.append(v)
    ## 아직 방문하지 않았다면 방문 처리
        for i in graph[v][::-1]:
            if visited[i] is False :
                visited[i] = True
                stack.append(i)
    ## 인접한 정점들을 스택에 추가

    return result

# 테스트 케이스
if __name__ == "__main__":
    # 그래프 생성
    graph = {
        0: [1, 2],
        1: [0, 2],
        2: [0, 1, 3],
        3: [2]
    }
    
    print("=== DFS (깊이 우선 탐색) ===")
    result = dfs(graph, 0)
    print(f"시작 정점: 0")
    print(f"방문 순서: {result}")
