class Solution {
    public int maximumWealth(int[][] accounts) {
        int n = accounts.length;
        int house = accounts[0].length;
        int result  = 0  ;
        for (int i = 0 ; i<n ;i++){
            int total = 0 ;
            for (int j=0 ; j<house; j++) {
                total += accounts[i][j];
            }
            result = Math.max(total, result);
        }
        return result;
    }
}