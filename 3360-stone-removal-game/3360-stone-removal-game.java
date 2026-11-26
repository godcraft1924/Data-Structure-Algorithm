class Solution {
    public boolean canAliceWin(int n) {
        int a[] = new int[11];
        int total = 0 ;
        a[0]  = 0 ;
        for(int i =10 ; i>0 ; i--){
            total += i ;
            a[11-i] = total ;
           
        }
         int idx = FindOrLarger(a , n );
            if (a[idx] == n ){
                if (idx%2 == 0 ){
                    return false;
                }
                return true;
            }

            if(idx%2 == 0 ){
                return true;
            } return false; 
    
        }
        public  int FindOrLarger(int[] nums , int target){
            int n = nums.length;
            int low = 0 ;
            int high = n-1 ;
            while (low<high) {
                int mid = low + (high-low )/2; 
                if (nums[mid]<target){
                    low = mid +1 ;
                }else{
                    high = mid ;
                }
                if (low  == n ){
                    return -1 ;
                }
            }
                return low ; 
        }

}