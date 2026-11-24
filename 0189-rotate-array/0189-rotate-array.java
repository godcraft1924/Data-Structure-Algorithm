class Solution {
    public void rotate(int[] nums, int k) {
        int n  = nums.length ; 
        int actual = k% n ;
        if (actual ==  0 ){
            return ;
        }
        reverse(0,n-1,nums);
        reverse(0,actual-1,nums);
        reverse(actual,n-1,nums);}
        public void reverse(int start, int end , int[] nums ){
            int left  = start ; 
            int right = end ;
            while(left < right) {
                int temp = nums[left]; 
                nums[left] = nums[right];
                nums[right]= temp; 
                left++;
                right--;
            } 
        }

    
}