class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s2) < len(s1): return False
        #create two hashing arrays
        array1 = [0] * 26
        array2 = [0] * 26

        #populate them
        for i in range(len(s1)):
            array1[(ord(s1[i]) - ord('a'))] += 1
            array2[(ord(s2[i]) - ord('a'))] += 1

        l = 0
        for r in range(len(s1), len(s2)):
            if array1 == array2:
                return True

            array2[(ord(s2[r]) - ord('a'))] += 1
            array2[(ord(s2[l]) - ord('a'))] -= 1

            l += 1

        return array1 == array2



        