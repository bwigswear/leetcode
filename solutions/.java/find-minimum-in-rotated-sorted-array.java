class Solution {
    public int findMin(int[] nums) {
        int l = 0;
        int r = nums.length - 1;
        int m = (l + r) / 2;
        int min = nums[0];
        while(l <= r){
            if(nums[l] < nums[r]){
                if(min > nums[l]){
                    return nums[l];
                }
            }

            if(min > nums[m]){
                min = nums[m];
            }

            if(nums[l] <= nums[m]){
                l = m + 1;
                m = (l + r) / 2;
            }else{
                r = m;
                m = (l + r) / 2;
            }
        }

        return min;
    }
}