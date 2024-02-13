import random

class DisjointSet:
    def __init__(self, size):
        self.parent = list(range(size))
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            self.parent[rootY] = rootX

def generate_maze(width, height):
    cells = width * height
    ds = DisjointSet(cells)
    
    # Initialize all walls
    vertical_walls = [[True for _ in range(width - 1)] for _ in range(height)]
    horizontal_walls = [[True for _ in range(width)] for _ in range(height - 1)]
    
    wall_list = []

    for x in range(width):
        for y in range(height):
            if x < width - 1:
                wall_list.append(('v', x, y))
            if y < height - 1:
                wall_list.append(('h', x, y))
    
    random.shuffle(wall_list)

    while wall_list:
        wall = wall_list.pop()
        wall_type, x, y = wall
        
        if wall_type == 'v':
            cell1 = y * width + x
            cell2 = y * width + (x + 1)
        else:  # wall_type == 'h'
            cell1 = y * width + x
            cell2 = (y + 1) * width + x
        
        if ds.find(cell1) != ds.find(cell2):
            ds.union(cell1, cell2)
            if wall_type == 'v':
                vertical_walls[y][x] = False
            else:  # wall_type == 'h'
                horizontal_walls[y][x] = False
    
    return vertical_walls, horizontal_walls

def print_maze(vertical_walls, horizontal_walls):
    width = len(horizontal_walls[0])
    height = len(vertical_walls)

    # Print the top border
    print(' _' * width)

    for y in range(height):
        print('|', end='')
        for x in range(width):
            if x < width - 1 and not vertical_walls[y][x]:
                print(' ', end='')
            else:
                print('|', end='')
            if y < height - 1 and not horizontal_walls[y][x]:
                print(' ', end='')
            else:
                print('_', end='')
        print('')

if __name__ == "__main__":
    width, height = 10, 10  # You can change the size of the maze here
    vertical_walls, horizontal_walls = generate_maze(width, height)
    print_maze(vertical_walls, horizontal_walls)
