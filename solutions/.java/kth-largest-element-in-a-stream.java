class KthLargest {

    PriorityQueue<Integer> q;
    int size = 0;
    int k;

    public KthLargest(int k, int[] nums) {
        q = new PriorityQueue<>();
        this.k = k;
        for(int i = 0; i < nums.length; i++){
            add(nums[i]);
        }
    }
    
    public int add(int val) {
        if(size < k){
            q.add(val);
            size++;
        } else {
            int top = q.peek();
            if(top < val){
                q.poll();
                q.add(val);
            }
        }
        return q.peek();
    }
}

/**
 * Your KthLargest object will be instantiated and called as such:
 * KthLargest obj = new KthLargest(k, nums);
 * int param_1 = obj.add(val);
 */