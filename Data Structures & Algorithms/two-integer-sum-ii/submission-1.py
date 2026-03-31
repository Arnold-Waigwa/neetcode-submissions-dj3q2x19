class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #start from the start and end
        #if the sum is bigger, r -=1
        #if its smaller, l+=1
        l, r = 0, len(numbers)-1
        while l < r:
            if numbers[l] + numbers[r] > target:
                r -= 1
            elif numbers[l] + numbers[r] < target:
                l += 1
            else:
                return [l+1,r+1]