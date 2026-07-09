class Solution:

    def encode(self, strs: List[str]) -> str:
        """
        4#nee#4#code
        """
        s = ""
        for string in strs:
            s += str(len(string)) + "#" + string
        return s

    def decode(self, s: str) -> List[str]:
        i = 0
        output = []
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1

            length = int(s[i:j])
            i = j + 1
            j += (length + 1)
            output.append(s[i:j])
            i = j
        return output





