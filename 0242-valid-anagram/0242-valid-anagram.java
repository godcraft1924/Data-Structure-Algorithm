class Solution {
    public boolean isAnagram(String s, String t) {
        if(s.length() != t.length()){
            return false;
        }
        int n = s.length();
        int[] a = new int[26];
        for (int i = 0 ; i <n ; i++ ){
            int character = (int)s.charAt(i);
            a[character-97] += 1 ;
            character = (int)t.charAt(i);
            a[character-97] -= 1 ;
        }
        for (int i = 0 ; i<26; i++){
            System.out.println(a);
            if (a[i] != 0){
                return false;
            }
        }
        return true;
        
    }
}