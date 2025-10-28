class Solution:
    
       def isValidSudoku(self, board:list[list[str]]) -> bool:
 
        n: int = len(board)
        column_dicts: list[set[str]] = [set() for i in range(n)]
        row_dicts: list[set[str]] = [set() for i in range(n)]
        square_dicts: dict[tuple[int, int], set[str]] = {(x, y): set() for x in range(n // 3) for y in range(n // 3)}
        i: int = 0
        j: int = 0
        square_key: tuple[int, int] = (0, 0)
        for i in range(n):
            for j in range(n):
                if (value := board[i][j]) != ".":
                    square_key = (i // 3, j // 3)
                    if value in column_dicts[j] or value in row_dicts[i] or value in square_dicts[square_key]:
                        return False
                    column_dicts[j].add(value)
                    row_dicts[i].add(value)
                    square_dicts[square_key].add(value)
        return True        

