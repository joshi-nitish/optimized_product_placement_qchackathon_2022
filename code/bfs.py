# reference - https://www.geeksforgeeks.org/shortest-distance-two-cells-matrix-grid/

class QItem:
    def __init__(self, row, col, dist):
        self.row = row
        self.col = col
        self.dist = dist

def minDistance(layout_obj, src, dst):

    source = QItem(src[0], src[1], 0)

    # To maintain location visit status
    grid = layout_obj.layout_mat
    visited = [[False for _ in range(grid.shape[1])] for _ in range(grid.shape[0])]

    # applying BFS on matrix cells starting from source
    queue = []
    queue.append(source)
    visited[source.row][source.col] = True
    while len(queue) != 0:
        source = queue.pop(0)

        # Destination found;
        if (source.row == dst[0] and source.col == dst[1]):
            return source.dist

        # moving up
        if isValid(source.row - 1, source.col, grid, visited):
            queue.append(QItem(source.row - 1, source.col, source.dist + 1))
            visited[source.row - 1][source.col] = True

        # moving down
        if isValid(source.row + 1, source.col, grid, visited):
            queue.append(QItem(source.row + 1, source.col, source.dist + 1))
            visited[source.row + 1][source.col] = True

        # moving left
        if isValid(source.row, source.col - 1, grid, visited):
            queue.append(QItem(source.row, source.col - 1, source.dist + 1))
            visited[source.row][source.col - 1] = True

        # moving right
        if isValid(source.row, source.col + 1, grid, visited):
            queue.append(QItem(source.row, source.col + 1, source.dist + 1))
            visited[source.row][source.col + 1] = True

    return -1


# checking where move is valid or not
def isValid(x, y, grid, visited):
    if ((x >= 0 and y >= 0) and (x < grid.shape[0] and y < grid.shape[1])) and ((grid[x,y] == 0) and (visited[x][y] == False)):
        return True
    return False