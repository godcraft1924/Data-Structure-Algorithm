
class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        maxi = 0
        for i in range(len(nums1)):
            maxi = max(maxi,abs(nums1[i]-nums2[i]))
        currDiff = [0]*(maxi+1)
        for i in range(len(nums1)):
            d = abs(nums1[i]-nums2[i])
            currDiff[d] += 1 
        k = k1+k2
        for i in range(maxi, 0, -1):
            if currDiff[i] == 0 :
                continue
            if k ==0 :
                break
            numOps =min(k,currDiff[i])
            currDiff[i] -= numOps
            currDiff[i-1] += numOps
            k -= numOps
        print(k,currDiff)
        minSum = 0
        for i in range(len(currDiff)):
            minSum += (i*i)*currDiff[i]
        return minSum


