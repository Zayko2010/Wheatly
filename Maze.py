import random
from Cell import Cell
from PIL import Image


class Maze:

    def __init__(self):
        self.x = random.randrange(25, 100)
        self.y = self.x
        self.startPos = None
        self.endPos = None
        self.poke = random.randrange(5, 20)
        self.pokeLocations = [()]
        self.grid = self.createGrid(self.createMaze(self.x, self.y))

    def createMaze(self, mx, my):
        maze = [[0 for x in range(mx)] for y in range(my)]
        # 4 directions to move in the maze
        dx = [0, 1, 0, -1]
        dy = [-1, 0, 1, 0]
        # start the maze from a random cell
        cx = random.randint(0, mx - 1)
        cy = random.randint(0, my - 1)
        maze[cy][cx] = 1
        stack = [(cx, cy, 0)] # stack element: (x, y, direction)

        while len(stack) > 0:
            (cx, cy, cd) = stack[-1]
            # to prevent zigzags:
            # if changed direction in the last move then cannot change again
            if len(stack) > 2:
                if cd != stack[-2][2]:
                    dirRange = [cd]
                else:
                    dirRange = range(4)
            else:
                dirRange = range(4)

            # find a new cell to add
            nlst = [] # list of available neighbors
            for i in dirRange:
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


    def createGrid(self, maze):
        grid = [[Cell(i, j, bool(maze[j][i]), False) for i in range(self.x)] for j in range(self.y)]
        freeCells = []

        for row in range(0, len(maze)):
            for cell in range(0, len(maze[row])):
                if not maze[row][cell]:
                    freeCells.append((row, cell))

        self.pokeLocations = random.sample(freeCells, self.poke)

        for location in self.pokeLocations:
            grid[location[0]][location[1]].hasPoke = True

        stillFree = random.sample([item for item in freeCells if item not in self.pokeLocations], 2)
        self.startPos = stillFree[0]
        self.endPos = stillFree[1]

        return grid

    def paintMaze(self):
        imgx = self.x * 100
        imgy = self.y * 100
        image = Image.new("RGB", (imgx, imgy))
        pixels = image.load()
        for ky in range(imgy):
            for kx in range(imgx):
                y = self.y * ky / imgy
                x = self.x * kx / imgx
                cell = self.grid[self.y * ky / imgy][self.x * kx / imgx]
                if (x == self.startPos[0] and y == self.startPos[1]):
                    pixels[kx, ky] = (21, 39, 198)
                    continue
                if (x == self.endPos[0] and y == self.endPos[1]):
                    pixels[kx, ky] = (167, 186, 1)
                    continue
                if cell.isWall:
                    pixels[kx, ky] = (255, 255, 255)
                else:
                    if cell.hasPoke:
                        pixels[kx, ky] = (255, 0, 0)
                    else:
                        pixels[kx, ky] = (0, 0, 0)
        image.save("Maze_" + str(self.x) + "x" + str(self.y) + ".png", "PNG")
        image.show("Maze.png")

test = Maze()
test.paintMaze()