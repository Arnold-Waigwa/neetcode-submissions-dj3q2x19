class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        #we'll keep indices to keep track of the window but underthehood use values for q
        q = deque()
        l = 0
        output = []

        for r in range(len(nums)):
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)
            #keep track of the window until k
            if l > q[0]:
                q.popleft()

            if (r+1) >= k:
                output.append(nums[q[0]])
                l += 1
        return output



        