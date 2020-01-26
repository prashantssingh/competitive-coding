# PROBLEM DESCRIPTION 
# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000

# For example, two is written as II in Roman numeral, just two one's added together. Twelve is written
# as, XII, which is simply X + II. The number twenty seven is written as XXVII, which is XX + V + II.

# Roman numerals are usually written largest to smallest from left to right. However, the numeral for 
# four is not IIII. Instead, the number four is written as IV. Because the one is before the five we 
# subtract it making four. The same principle applies to the number nine, which is written as IX. 
# There are six instances where subtraction is used:

# I can be placed before V (5) and X (10) to make 4 and 9. 
# X can be placed before L (50) and C (100) to make 40 and 90. 
# C can be placed before D (500) and M (1000) to make 400 and 900.
# Given a roman numeral, convert it to an integer. Input is guaranteed to be within the range from 1 to 3999.

# SAMPLE INPUT                                      SAMPLE OUTPUT
# "III"                                             3

# SAMPLE INPUT                                      SAMPLE OUTPUT
# "IV"

# SAMPLE INPUT                                      SAMPLE OUTPUT
# "IX"

# SAMPLE INPUT                                      SAMPLE OUTPUT
# "LVIII"
# EXPLANATION
# L = 50, V= 5, III = 3.

# SAMPLE INPUT                                      SAMPLE OUTPUT
# "MCMXCIV"
# EXPLANATION
# M = 1000, CM = 900, XC = 90 and IV = 4.

class Solution:
    def romanToInt(self, s: str) -> int:
        symbol_dict = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        
        res = i = 0
        while i < len(s):
            print(i, res, s[i])
            if i < len(s)-1:
                if s[i] == 'I' and s[i+1] == 'V':
                    res += 4
                    i += 2
                elif s[i] == 'I' and s[i+1] == 'X':
                    res += 9
                    i += 2
                elif s[i] == 'X' and s[i+1] == 'L':
                    res += 40
                    i += 2
                elif s[i] == 'X' and s[i+1] == 'C':
                    res += 90
                    i += 2
                elif s[i] == 'C' and s[i+1] == 'D':
                    res += 400
                    i += 2
                elif s[i] == 'C' and s[i+1] == 'M':
                    res += 900
                    i += 2
                else: 
                    res += symbol_dict[s[i]]
                    i += 1
            else: 
                res += symbol_dict[s[i]]
                i += 1

        return res
                
                
            
            