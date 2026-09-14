class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        right = 0 
        for i in range(len(nums)):
            if nums[i]==0 :
                if right < i:
                    right = i 
                while right < len(nums)-1 and nums[right]==0  :
                    right += 1
                if right< len(nums):
                    nums[i], nums[right] = nums[right]  ,nums[i] 
                 
            # else:
            #     print(len(nums),right)
            #     while right <len(nums) and nums[right]==0  :
            #         right += 1
            #     nums[i], nums[right] = nums[right]  ,nums[i]
                # right +=1 
        