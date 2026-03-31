class Solution:
    def solve(self, board: List[List[str]]) -> None:
        #launch a multisource bfs
        #loop through the edges and look for "O"s and store
        #them in a queue
        #perform a bfs to check if any of its neighbors(connected)
        #are O's as well. any found O is modified to an A
        #when the queue is empty, we've found all invalid Os
        #which are now A's
        #initiate another loop to go through the board, and 
        #change all remaining Os which are assumed to be valid into X's and A's back into Os
        rows, cols = len(board), len(board[0])
        directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]
        q = deque()
        for row in range(rows):
            for col in range(cols):
                if (row == 0 or row == rows - 1 
                or col == 0 or col == cols - 1
                ):
                    if board[row][col] == "O":
                        board[row][col] = "A"
                        q.append((row, col))
        
        while q:
            row, col = q.popleft()
            board[row][col] = "A"
            for dr, dc in directions:
                nr, nc = row + dr, col + dc
                if (
                    nr in range(rows) and nc in range(cols)
                    and board[nr][nc] == "O"
                ):
                    q.append((nr, nc))
        
        for row in range(rows):
            for col in range(cols):
                if board[row][col] == "O":
                    board[row][col] = "X"
                if board[row][col] == "A":
                    board[row][col] = "O"





                


        