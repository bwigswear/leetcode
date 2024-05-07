class Solution {

    List<List<Integer>> ret = new ArrayList<>();
    int[] nums;

    public void abc(List<Integer> current, int index){
            System.out.print(index + " ");
            System.out.println(current); 
            if(index == nums.length){
                List<Integer> copy = new ArrayList<>(current);
                ret.add(copy);
                return;
            }
            if(!(current.size() > 0 && nums[index] == current.get(current.size() - 1))){
                abc(current, index + 1);
            }
            current.add(nums[index]);
            abc(current, index + 1);
            current.remove(current.size() - 1);
        }
    public List<List<Integer>> subsetsWithDup(int[] nums) {
        this.nums = nums;
        Arrays.sort(nums);
        List<Integer> b = new ArrayList<>();

        abc(b, 0);
        return ret;
    }
}