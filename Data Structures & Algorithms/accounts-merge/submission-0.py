class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        graph = defaultdict(set)
        email_to_name = {}

        for account in accounts:
            name = account[0]
            first_email = account[1]

            email_to_name[first_email] = name
            graph[first_email]  # make sure single-email accounts exist

            for email in account[2:]:
                email_to_name[email] = name

                graph[first_email].add(email)
                graph[email].add(first_email)

        visited = set()

        def dfs(email, arr):
            if email in visited:
                return

            visited.add(email)
            arr.append(email)

            for nei in graph[email]:
                dfs(nei, arr)

        res = []

        for email in graph:
            if email not in visited:
                emails = []
                dfs(email, emails)

                name = email_to_name[email]
                res.append([name] + sorted(emails))

        return res