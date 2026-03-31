class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        Use a two pointer approach; One loop to go over every element and one more for the two pointer
        1). Sort the nums array to remove the duplicates
            create empty array for storing result
        2). Go through every index, element in the array:
                    check for duplicates and move to the next element
                    create left and right pointer that to work in the remaining elements
                    left = i + 1, len(nums) - 1
                    if the value + nums[left] + nums[right] > 0, r -= 1
                    if the value + nums[left] + nums[right] < 0, l += 1
                    if its 0, res.append(the three numbers in array)
                    update the left pointer: and check if the left pointer has a duplicate next to it
        """
        nums.sort()
        res = []

        for i, v in enumerate(nums):
            if i > 0 and v == nums[i - 1]:
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = v + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([v, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return res
                     
        