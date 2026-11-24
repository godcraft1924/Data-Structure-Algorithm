class Solution {
    public void moveZeroes(int[] nums) {
        int n = nums.length; 
        int right = 0 ;
        for (int i = 0 ; i< n ; i++) {
            if (nums[i] == 0 ){
                if (right < i ){
                    right  = i; 
                }
                while (right < n && nums[right]== 0 ){
                    right++;
                }
                if (right  < n) {
                    int temp = nums[i];
                    nums[i]  = nums[right];
                    nums[right] = temp ;
                }
            }
        }
    }
}