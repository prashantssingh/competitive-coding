# PROBLEM DESCRIPTION:
# Given a string, devide it into two substrings such that the substrings have the most possible characters
# in common. The cut commonality is number of characters in common between the two substrings. Determine the
# cut commonality.
# 
# For example, s = 'abcdedeara', there are 9 ways to split the string into two non-empty substrings. The best
# possible way is to split it into 'abcde' and 'deara' which gives the cut commonality of 3 with 1 each for a,
# d and e.
# 
# If a character is repeated, the cut commonality count for that character is the minimum of the count of that
# character in the two substrings. Given the original string 'aabbbbaa', the best way to split is 'aabb' and 
# 'bbaa' and the cut commonality is 4 with two a's and two b's

def maximal_commanality(s):
    if not s or len(s) == 1:
        return 0
    
    freq1 = [0] * 26  
    freq2 = [0] * 26

    for ch in s:  
        freq2[ord(ch) - ord('a')] += 1

    count = 0 
    for i in range(len(s)):
        curr_count = 0
        for alph_ind in range(26):
            curr_count += min(freq1[alph_ind], freq2[alph_ind]); 
        count = max(count, curr_count)

        freq1[ord(s[i]) - ord('a')] += 1
        freq2[ord(s[i]) - ord('a')] -= 1

    return count

print(maximal_commanality('abcdedeara'))        # should print 3
print(maximal_commanality('aabbbbaa'))          # should print 4
print(maximal_commanality('aabbcdcdfbbaa'))     # should print 6