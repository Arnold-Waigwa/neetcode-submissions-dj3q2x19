class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split("/")
        print(path)
        stack = []

        for st in path:
            if st == "" or st == ".":
                continue

            elif st == "..":
                if stack:
                    stack.pop()
                else:
                    continue
            
            else:
                stack.append(st)

        return "/" + "/".join(stack)

