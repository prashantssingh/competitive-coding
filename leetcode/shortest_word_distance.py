# PROBLEM DESCRIPTION:
# Given a list of words and two words word1 and word2, return the shortest distance between these
#  two words in the list.
# 
# EXAMPLE:
# Assume that words = ["practice", "makes", "perfect", "coding", "makes"].
# 
# INPUT:                                                            OUTPUT:
# word1 = “coding”, word2 = “practice”                              3
# 
# INPUT:                                                            OUTPUT:
# word1 = "makes", word2 = "coding"                                 1
# 
# NOTE:
# You may assume that word1 does not equal to word2, and word1 and word2 are both in the list.

class Solution:
    def shortestDistance(self, words: List[str], word1: str, word2: str) -> int:
        words_indices = {
            word1: [],
            word2: []
        }
        
        for i in range(len(words)):
            if words[i] == word1:
                words_indices[word1].append(i)
            
            if words[i] == word2:
                words_indices[word2].append(i)
                
        minimum = len(words)
        for i in words_indices[word1]:
            for j in words_indices[word2]:
                print(i, j)
                minimum = min(minimum, abs(i-j))
                
        return minimum