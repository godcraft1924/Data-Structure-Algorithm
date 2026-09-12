class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        low = 0
        high = len(nums)-1
        greater = -1
        lower  = -1
        while low  <= high :
            mid = low  + (high-low)//2 
            if nums[mid] == target :
                greater = mid
                high = mid - 1
            elif nums[mid] < target :
                low = mid +1 
            else:
                high = mid- 1 
        low = 0
        high = len(nums)-1

        while low  <= high :
            mid = low  + (high-low)//2 
            if nums[mid] == target :
                lower = mid
                low = mid + 1
            elif nums[mid] < target :
                low = mid +1 
            else:
                high = mid- 1 
        return [greater,lower ]


        