class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        number = [[],[],["a", "b", "c"], ["d", "e", "f"],
                ["g", "h", "i"], ["j", "k", "l"], ["m", "n", "o"],
                ["p", "q", "r", "s"],["t", "u", "v"],["w", "x", "y", "z"]]
        
        combine = []
        

        def backTracking(num, currentString) :
            if len(digits) == len(currentString):   #  모두 추가됐을 때, combine[]에 추가 후 종료
                return combine.append(currentString)    
                                                                  
            for j in range(len(number[int(digits[num])])):  # digist의 num번째 숫자를 number의 인덱스로 설정, 그리고 number[num]의 문자 개수 만큼 반복
                currentString += number[int(digits[num])][j]    # number[num]의 j번째(0 ~ number[num]의 개수) 글자 추가
                backTracking(num+1 , currentString) # 다음 글자를 추가하기 위해 num+1(다음 글자), currentString(현재 글자)를 매개변수로 함수 재호출
                currentString = currentString[ : -1]    # 마지막 문자를 제외하고 슬라이싱하여 다음 조합 글자 찾기

        backTracking(0, "")
        return combine