from collections import defaultdict
class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefix = defaultdict(int)
        prefix[0] = 1
        res = total = 0

        for num in nums:
            total += num
            if total % k in prefix:
                res += prefix[total % k]

            prefix[total % k] += 1
        
        return res

