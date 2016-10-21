import random
from Cell import Cell
from PIL import Image


class Maze:

    def __init__(self):
        self.x = random.randrange(10, 11)
        self.y = self.x
        self.start_pos = None
        self.end_pos = None
        self.hatch_units = random.randint(3, self.x)
        self.poke = random.randrange(2, 5)
        self.poke_locations = [()]
        self.maze = self.create_maze(self.x, self.y)
        self.grid = self.create_grid(self.maze)

    def create_maze(self, mx, my):
        maze = [[0 for x in range(mx)] for y in range(my)]
        # 4 directions to move in the maze
        dx = [0, 1, 0, -1]
        dy = [-1, 0, 1, 0]
        # start the maze from a random cell
        cx = random.randint(0, mx - 1)
        cy = random.randint(0, my - 1)
        maze[cy][cx] = 1
        stack = [(cx, cy, 0)]  # stack element: (x, y, direction)

        while len(stack) > 0:
            (cx, cy, cd) = stack[-1]
            # to prevent zigzags:
            # if changed direction in the last move then cannot change again
            if len(stack) > 2:
                if cd != stack[-2][2]:
                    dir_range = [cd]
                else:
                    dir_range = range(4)
            else:
                dir_range = range(4)

            # find a new cell to add
            nlst = [] # list of available neighbors
            for i in dir_range:
                nx = cx + dx[i]
                ny = cy + dy[i]
                if nx >= 0 and nx < mx and ny >= 0 and ny < my:
                    if maze[ny][nx] == 0:
                        ctr = 0 # of occupied neighbors must be 1
                        for j in range(4):
                            ex = nx + dx[j]
                            ey = ny + dy[j]
                            if ex >= 0 and ex < mx and ey >= 0 and ey < my:
                                if maze[ey][ex] == 1:
                                    ctr += 1
                        if ctr == 1:
                            nlst.append(i)

            # if 1 or more neighbors available then randomly select one and move
            if len(nlst) > 0:
                ir = nlst[random.randint(0, len(nlst) - 1)]
                cx += dx[ir]
                cy += dy[ir]
                maze[cy][cx] = 1
                stack.append((cx, cy, ir))
            else:
                stack.pop()

        return maze

    def create_grid(self, maze):
        grid = [[Cell(i, j, bool(maze[j][i]), False) for i in range(self.x)] for j in range(self.y)]
        free_cells = []

        for row in range(0, len(maze)):
            for cell in range(0, len(maze[row])):
                if not maze[row][cell]:
                    free_cells.append((row, cell))

        self.poke_locations = free_cells #random.sample(free_cells, self.poke)

        for location in self.poke_locations:
            grid[location[0]][location[1]].has_poke = True
            # print("Grid test isWall and hasPoke: {0}".format(grid[location[0]][location[1]].is_wall))

        still_free = free_cells #random.sample([item for item in free_cells if item not in self.poke_locations], 2)
        self.start_pos = still_free[0]
        self.end_pos = still_free[1]

        return grid

    def paint_maze(self):
        img_x = self.x * 10
        img_y = self.y * 10
        image = Image.new("RGB", (img_x, img_y))
        pixels = image.load()
        for ky in range(img_y):
            for kx in range(img_x):
                y = self.y * ky / img_y
                x = self.x * kx / img_x
                cell = self.grid[self.y * ky / img_y][self.x * kx / img_x]
                if x == self.start_pos[0] and y == self.start_pos[1]:
                    pixels[kx, ky] = (21, 39, 198)
                    continue
                if x == self.end_pos[0] and y == self.end_pos[1]:
                    pixels[kx, ky] = (167, 186, 1)
                    continue
                if cell.is_wall:
                    pixels[kx, ky] = (255, 255, 255)
                else:
                    if cell.has_poke:
                        pixels[kx, ky] = (255, 0, 0)
                    else:
                        pixels[kx, ky] = (0, 0, 0)
        image.save("Maze_" + str(self.x) + "x" + str(self.y) + ".png", "PNG")
        # image.show("Maze.png")

    # toString function
    def print_grid(self):
        print_matrix = [[]for y in range(self.grid.__len__())]
        for i in range(self.grid.__len__()):
            for j in range(self.grid[i].__len__()):
                if self.grid[i][j].is_wall:
                    print_matrix[i].append(1)

                if not self.grid[i][j].is_wall and not self.grid[i][j].has_poke:
                    print_matrix[i].append(0)

                if self.grid[i][j].has_poke:
                    print_matrix[i].append(8)

                if i == self.start_pos[0] and j == self.start_pos[1]:
                    print_matrix[i][j] = 5

                if i == self.end_pos[0] and j == self.end_pos[1]:
                    print_matrix[i][j] = 3
        return print_matrix
test = Maze()
test.paint_maze()