class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #want to find the min number
        #we can make an auxiliary function that returns
        #number of hours for a given k
        #we know the highest number is max of piles and lowest 1
        #do binary search one by one and test if the numbers 
        # returned works
        #if it does, we store the lowest and do binary search on the lower
        #half. If it doesn't, do binary on the upper half
        #when the pointers cross return answer
        def hour(k):
            hours = 0
            for val in piles:
                hours += (val + k - 1) // k
            return hours

        lowest_k = max(piles)
        l, r = 1, max(piles)
        while l <= r:
            mid = (l + r) // 2
            if hour(mid) <= h:
                lowest_k = min(lowest_k, mid)
                r = mid - 1
            else:
                l = mid + 1
        return lowest_k

        