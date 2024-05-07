class Solution {
    public int search(int[] nums, int target) {
        int a = 0;
        int c = nums.length - 1;
        int b = (a + c) / 2;

        while(a <= c){
            if(nums[b] == target){
                return b;
            }else if(nums[b] < target){
                a = b + 1;
                b = (a + c) / 2;
            }else{
                c = b - 1;
                b = (a + c) / 2;
            }
        }
        return -1;
    }
}