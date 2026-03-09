class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # 첫 번째 풀이

        # k=1
        # for i in range(0, len(nums)-2):
        #     for j in range(0, len(nums)-2):
        #         if nums[j] == nums[j+1]:
        #             nums[j+1] = nums[j+2]

        # for i in range(0, len(nums)-1):     
        #     if nums[i] == nums[i+1]:
        #         break
        #     k+=1
        # return k

        # 시간초과문제가 있음

        # 두 번째 풀이

        k=0
        check = [False for i in range(201)]
        arr = []
        for i in range(len(nums)):
            if check[nums[i]] == False:
                check[nums[i]] = True
                arr.append(nums[i])
    
        for i in range(len(arr)):
            nums[i] = arr[i]
            k+=1

        return k