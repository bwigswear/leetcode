class Solution {
    public int orangesRotting(int[][] grid) {
        int rows = grid.length;
        int cols = grid[0].length;
        List<Integer[]> adj = new ArrayList<>();
        for(int x = 0; x < rows; x++){
            for(int y = 0; y < cols; y++){
                if(grid[x][y] == 2){
                    if(x - 1 > -1 && grid[x-1][y] == 1){
                        Integer[] a = {x-1, y};
                        adj.add(a);
                    }
                    if(x + 1 < rows && grid[x+1][y] == 1){
                        Integer[] a = {x+1, y};
                        adj.add(a);
                    }
                    if(y - 1 > -1 && grid[x][y-1] == 1){
                        Integer[] a = {x, y-1};
                        adj.add(a);
                    }
                    if(y + 1 < cols && grid[x][y+1] == 1){
                        Integer[] a = {x, y+1};
                        adj.add(a);
                    }
                }
            }
        }
        List<Integer[]> replace = new ArrayList<>();
        int minutes = 0;
        while(adj.size() > 0){
            for(Integer[] print: adj){
                grid[print[0]][print[1]] = 2;
            }
            for(Integer[] orange: adj){
                int x = orange[0];
                int y = orange[1];
                if(x - 1 > -1 && grid[x-1][y] == 1){
                    Integer[] a = {x-1, y};
                    replace.add(a);
                }
                if(x + 1 < rows && grid[x+1][y] == 1){
                    Integer[] a = {x+1, y};
                    replace.add(a);
                }
                if(y - 1 > -1 && grid[x][y-1] == 1){
                    Integer[] a = {x, y-1};
                    replace.add(a);
                }
                if(y + 1 < cols && grid[x][y+1] == 1){
                    Integer[] a = {x, y+1};
                    replace.add(a);
                }
            }
            adj = new ArrayList<>(replace);
            replace.clear();
            minutes++;
        }
        for(int x = 0; x < rows; x++){
            for(int y = 0; y < cols; y++){
                if(grid[x][y] == 1){
                    return -1;
                }
            }
        }
        return minutes;
}
}