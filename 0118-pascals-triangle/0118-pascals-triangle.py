class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        output = []
        
        for num_row in range(0, numRows, 1):
            col = []
            for idx in range(0, num_row+1, 1):
                if idx == 0 or idx == num_row:
                    col.append(1)
                else:
                    col.append(output[num_row-1][idx-1] + output [num_row-1][idx])
            output.append(col)   
        return output
                