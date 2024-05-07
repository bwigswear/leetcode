class Solution {
    public List<List<Integer>> generate(int numRows) {
        List<List<Integer>> a = new ArrayList<>();
        if(numRows == 0){return a;}
        List<Integer> old = new ArrayList<>();
        old.add(1);
        a.add(old);

        for(int i = 1; i < numRows; i++){
            List<Integer> b = new ArrayList<>();
            old = a.get(i - 1);
            b.add(1);
            for(int j = 0; j < old.size() - 1; j++){
                b.add(old.get(j) + old.get(j+1));
            }
            b.add(1);
            a.add(b);
        }
        return a;
    }
}