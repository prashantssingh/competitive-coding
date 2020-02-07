# PROBLEM DESCRIPTION:
# Find the minimum length word from a given dictionary "words", which has all the letters from the string
# "licensePlate". Such a word is said to complete the given string "licensePlate"
# 
# Here, for letters we ignore case. For example, "P" on the "licensePlate" still matches "p" on the word.
# 
# It is guaranteed an answer exists. If there are multiple answers, return the one that occurs first in the array.
# 
# The license plate might have the same letter occurring multiple times. For example, given a # "licensePlate" 
# of "PP", the word "pair" does not complete the "licensePlate", but the word "supper" does.
# 
# EXAMPLES:
# INPUT:                                                          OUTPUT:
# licensePlate = "1s3 PSt",                                       steps
# words = ["step", "steps", "stripe", "stepple"]
# EXPLANATION: The smallest length word that contains the letters "S", "P", "S", and "T".
# Note that the answer is not "step", because the letter "s" must occur in the word twice.
# Also note that we ignored case for the purposes of comparing whether a letter exists in the word.
# 
# INPUT:                                                          OUTPUT:
# licensePlate = "1s3 456",                                       pest
# words = ["looks", "pest", "stew", "show"]
# EXPLANATION: There are 3 smallest length words that contains the letters "s".
# We return the one that occurred first.
# 
# NOTE:
# "licensePlate" will be a string with length in range [1, 7].
# "licensePlate" will contain digits, spaces, or letters (uppercase or lowercase).
# words will have a length in the range [10, 1000].
# Every words[i] will consist of lowercase letters, and have length in range [1, 15].


from collections import Counter

class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        res, res_len = "", 1000
        lp = licensePlate.lower()
        
        for word in words:
            found = True
            word_counter = Counter(word)
            for i in lp:
                if i.isalpha():
                    if i in word_counter and word_counter[i] != 0:
                        word_counter[i] -= 1
                    else:
                        found = False
                        break

            if found and res_len > len(word):
                res = word
                res_len = len(word)
                
        return res
            
        