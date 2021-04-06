"""
/*
Hope it will help you to understand :

    n = 0;     null
    count[0] = 1

    n = 1;      1
    count[1] = 1

    n = 2;    1__       			 __2
    		      \					/
    		     count[1]	   	count[1]
    count[2] = 1 + 1 = 2

    n = 3;    1__				      __2__	                   __3
    		      \		            /       \			      /
    		  count[2]		  count[1]    count[1]		count[2]
    count[3] = 2 + 1 + 2  = 5

    n = 4;    1__  					__2__					   ___3___
    		      \				 /        \					  /		  \
    		  count[3]		 count[1]    count[2]		  count[2]   count[1]

                 __4
               /
           count[3]
    count[4] = 5 + 2 + 2 + 5 = 14
And  so on...
*/
"""


class Solution:
    def numTrees(self, n: int) -> int:
        """
        https://youtu.be/GgP75HAvrlY?t=694
        """
        if n == 0 or n == 1:
            return 1
        count = 0
        for i in range(1, n + 1):
            count += self.numTrees(i - 1) * self.numTrees(n - i)
        return count

    def numTrees(self, n: int) -> int:
        """
        memoization
        """

        def helper(n, memo):
            if n in memo:
                return memo[n]
            count = 0
            for i in range(1, n + 1):
                count += helper(i - 1, memo) * helper(n - i, memo)
            memo[n] = count
            return count

        memo = {}
        memo[0] = 1
        memo[1] = 1
        helper(n, memo)
        return memo[n]
