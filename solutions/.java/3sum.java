class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        List<List<Integer>> ret = new ArrayList<>();
        Arrays.sort(nums);
        int a = 0;
        int b = 1;
        int c = nums.length - 1;
        while(a < nums.length - 2){
            if(a > 0 && nums[a] == nums[a - 1]){
                a++;
                b++;
                continue;
            }
            while(b < c){
                if(b > a + 1 && nums[b] == nums[b - 1]){
                    b++;
                    continue;
                }else if(c < nums.length - 1 && nums[c] == nums[c+1]){
                    c--;
                    continue;
                }
                int d = -1 * nums[a];
                int e = nums[b] + nums[c];
                if(e == d){
                    List<Integer> add = new ArrayList<>();
                    add.add(nums[a]);
                    add.add(nums[b]);
                    add.add(nums[c]);
                    ret.add(add);
                    b++;
                    c--;
                }else if(e > d){
                    c--;
                }else{
                    b++;
                }
            }
            a++;
            b = a + 1;
            c = nums.length - 1;
        }
        return ret;
        
    }
}