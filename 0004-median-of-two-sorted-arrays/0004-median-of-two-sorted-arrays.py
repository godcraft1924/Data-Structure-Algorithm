class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        newlist = nums1 + nums2 
        newlist.sort()
        length = len(newlist)
        if len(newlist)%2 == 0 :
            median = (newlist[length//2-1] + newlist[length//2])/2
        else:
            median = newlist[(length)//2]
        return median 