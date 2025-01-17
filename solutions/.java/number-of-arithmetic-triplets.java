class Solution {
    public int arithmeticTriplets(int[] nums, int diff) {
        int ret = 0;
        HashSet<Integer> set = new HashSet<>();
        for(int num : nums){
            set.add(num);
        }
        for(int i = 0; i < nums.length; i++){
            if(set.contains(nums[i] + diff) && set.contains(nums[i] + diff * 2)){
                ret++;
            }
        }
        return ret;
    }
}