class Solution {
    public List<Integer> spiralOrder(int[][] matrix) {
        int direction = 1;
        int toprow = 0;
        int bottomrow = matrix.length - 1;
        int leftcol = 0;
        int rightcol = matrix[0].length - 1;
        int x = 0;
        int y = 0;
        List<Integer> ret = new ArrayList<>();
        while(toprow <= bottomrow && leftcol <= rightcol){
            if(direction == 1){
                if(y > rightcol){
                    direction = 2;
                    toprow++;
                    y--;
                    x++;
                }else{
                    ret.add(matrix[x][y]);
                    y++;
                }
            }else if(direction == 2){
                if(x > bottomrow){
                    direction = 3;
                    rightcol--;
                    x--;
                    y--;
                }else{
                    ret.add(matrix[x][y]);
                    x++;
                }
            }else if(direction == 3){
                if(y < leftcol){
                    direction = 4;
                    bottomrow--;
                    y++;
                    x--;
                }else{
                    ret.add(matrix[x][y]);
                    y--;
                }
            }else if(direction == 4){
                if(x < toprow){
                    direction = 1;
                    leftcol++;
                    x++;
                    y++;
                }else{
                    ret.add(matrix[x][y]);
                    x--;
                }
            }
        }
        return ret;
    }
}