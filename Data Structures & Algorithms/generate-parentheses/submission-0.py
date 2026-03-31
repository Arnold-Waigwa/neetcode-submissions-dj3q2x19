class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        #just using dfs and backtracking
        res = []
        def dfs(openN, closedN, s):
            #base case
            if openN == closedN and openN + closedN == n*2:
                res.append(s)
                return

            if openN < n:
                dfs(openN + 1, closedN, s + "(")

            if closedN < openN:
                dfs(openN, closedN + 1, s + ")")

        dfs(0,0,"")
        return res




        