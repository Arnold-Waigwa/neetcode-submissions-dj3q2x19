class Solution:
    def tribonacci(self, n: int) -> int:
        """
        n = tn-1 + tn-2 + tn-3
        3 = t2 + t1 + t0
            1.    1.   0 = 3
        [0, 1, 1, 3, 4, 5,...n]
        dp[i] value of the ith dp where dp[i] = dp[i -1] + dp[i - 2] + dp[i3]
        val0 = 1, val1 = 2, val2 = 2
        val3 = val1 + val2 + val3
        """
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1
            
        val0, val1, val2 = 0, 1, 1
        for i in range(3, n + 1):
            prev = val2
            val2 += val1 + val0
            val0, val1 = val1, prev
        
        return val2

