# PROBLEM DESCRIPTION:
# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: 
# (you may want to display this pattern in a fixed font for better legibility)
# P   A   H   N
# A P L S I I G
# Y   I   R
# And then read line by line: "PAHNAPLSIIGYIR"
# 
# Write the code that will take a string and make this conversion given a number of rows:
# 
# string convert(string s, int numRows);
# 
# EXAMPLES:
# INPUT:                                                        OUTPUT:
# s = "PAYPALISHIRING", numRows = 3                             "PAHNAPLSIIGYIR"             
# 
# INPUT:                                                        OUTPUT:
# s = "PAYPALISHIRING", numRows = 4                             "PINALSIGYAHRPI"             
# 
# EXPLANATION:
# P     I    N
# A   L S  I G
# Y A   H R
# P     I

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if not s: return ""
        
        result = [''] * numRows
        invert = False
        ind = 0
        for char in s:
            if invert:
                ind -= 1
                result[ind] += char     
                if ind <= 0: 
                    invert = not invert
                    ind += 1
                    
            else:
                result[ind] += char
                ind +=1
                if ind >= numRows: 
                    invert = not invert
                    ind -= 1
                    
        res = ""
        for i in range(len(result)):
            res += result[i]
            
        return res