class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer,Integer> dict = new HashMap<>();
        int[]  a = new int[2];
        int n = nums.length;
        for (int i = 0 ; i <n ; i++){
            int complement = target-nums[i] ;
            if(dict.containsKey(complement)){
                a[0] = dict.get(complement);
                a[1] = i ;
                return a ;
            }else{
                dict.put(nums[i] , i );
            }}
            return new int[] {};
    }
}