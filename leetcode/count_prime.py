# PROBLEM DESCRIPTION:
# Count the number of prime numbers less than a non-negative number, n.
# 
# EXAMPLE:
# INPUT                                                     OUTPUT:
# 10                                                        4
# 
# EXPLANATION: 
# There are 4 prime numbers less than 10, they are 2, 3, 5, 7.

class Solution:    
    def countPrimes(self, n: int) -> int:
        if n < 3: return 0
        
        def prime(num):
            # print("prime for:", num)
            res = True
            for i in range(2, num):
                # print("i:", i)
                if num % i == 0:
                    return False

            return res
        
        primes_list = list()
        num = 2
        while num < n:
            if prime(num): 
                primes_list.append(num)
            num += 1
            
        return len(primes_list)


# NOTE: This solution takes a very long execution time for very number as input. To optimise this use `Sieve of Eratosthenes`
# REFER: https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes