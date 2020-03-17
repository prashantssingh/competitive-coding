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

# Brute force solution
# class Solution:
#     def shortestDistance(self, words: List[str], word1: str, word2: str) -> int:
#         words_indices = {
#             word1: [],
#             word2: []
#         }
#       
#         for i in range(len(words)):
#             if words[i] == word1:
#                 words_indices[word1].append(i)
#            
#             if words[i] == word2:
#                 words_indices[word2].append(i)            
#    
#         minimum = len(words)
#         for i in words_indices[word1]:
#             for j in words_indices[word2]:
#                 print(i, j)
#                 minimum = min(minimum, abs(i-j))
# 
#         return minimum

# Keep two indices to track the most recent locations of word1 and word2. Each time we find a
#  new occurrence of one of the words, we do not need to search the entire array for the other 
# word, since we already have the index of its most recent occurrence.
class Solution:
    def shortestDistance(self, words: List[str], word1: str, word2: str) -> int:
        ind1, ind2 = None, None
        minimum = len(words)
        for i in range(len(words)):
            if words[i] == word1:
                ind1 = i
            
            if words[i] == word2:
                ind2 = i
            
            if (ind1 is not None and ind2 is not None):
                minimum = min(minimum, abs(ind1 -ind2))
                
        return minimum