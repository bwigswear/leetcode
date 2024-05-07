class Solution {
    public boolean isPalindrome(int x) {
        String num = String.valueOf(x);
        int a = 0;
        int b = num.length() - 1;
        while(a < b){
            if(num.charAt(a) != num.charAt(b)){return false;}
            a++;
            b--;
        }
        return true;
    }
}