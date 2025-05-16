
def minesweeper_grid(grid):
    rows = len(grid)
    cols = len(grid[0])
    count_grid = [["0" for _ in range(cols)] for _ in range(rows)]
    
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == "#":  
                count_grid[i][j] = "#"
            else:
                count_grid[i][j] = str(count_mines(grid, i, j))
    
    return count_grid

def count_mines(grid, row, col):
    offsets = [(-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1)]
    count = 0
    for offset in offsets:
        offset_row = row + offset[0]  
        offset_col = col + offset[1]
         
      
        if 0 <= offset_row < len(grid) and 0 <= offset_col < len(grid[0]):
            if grid[offset_row][offset_col] == "#":
                count += 1
    return count


my_list = [
    ["-", "-", "-", "#", "#"],
    ["-", "#", "-", "-", "-"],
    ["-", "#", "#", "-", "-"],
    ["-", "-", "-", "-", "-"]
]

result_grid = minesweeper_grid(my_list)
for row in result_grid:
    print(row)