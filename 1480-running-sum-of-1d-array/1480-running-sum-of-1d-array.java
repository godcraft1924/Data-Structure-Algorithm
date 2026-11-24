import java.util.Vector;
class Solution {
    public int[] runningSum(int[] nums) {
        int n = nums.length;
        int[] a = new int[n];
        int total =0  ;
        for (int i = 0 ; i <n ; i++ ){
            total += nums[i];
            a[i] = total ;
        }
        return a;
    }
}