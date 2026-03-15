class Solution:
    def simplifyPath(self, path: str) -> str:
        
        list = path.split("/")
        stack = []
        string = ""
        # /으로 끝나는 경우
        # /가 이어서 나오는 경우 (//, /// 등)
        #  . 은 현재 디렉토리( / 바로 뒤 경로), ..은 상위 디렉토리 ( / 디렉토리 이름 / 뒤 경로)
        #  .이 세 개 이상인 경우는 파일 이름으로 간주/

        # /를 기준으로 나눔. 경로가 "/home/" 인 경우
        # ["", "home", ""] 이렇게 저장됨
        # "/.../a/../b/c/../d/./" 인 경우
        # ["", "...", "a", "..", "b", "c", "..", "d", ".", ""]

        for i in range(len(list)):
            if list[i] == "" or list[i] == "." :
                continue
            elif list[i] == ".." :
                if len(stack) > 0 :
                    stack.pop()
            else :
                # 빈 문자열이거나 ".", ".."을 제외하고 스택에 추가
                stack.append(list[i])

        for i in range(len(stack)) :
            # 파일이름 뒤 / 추가
            string += stack[i]+"/"
        #최상단 루트에 / 추가
        result =  "/" + string.rstrip("/")
        return result