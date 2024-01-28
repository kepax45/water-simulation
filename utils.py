import pygame
import random

WATER_COLOR = (0, 0, 255)
WALL_COLOR = (180, 180, 180)


def convert(x, y, cell_size):
    return (x//cell_size, y//cell_size)
def draw_water(row, col, window, cell_size):
    pygame.draw.rect(window, WATER_COLOR, pygame.Rect(col * cell_size, row * cell_size, cell_size, cell_size))
def draw_wall(row, col, window, cell_size):
    pygame.draw.rect(window, WALL_COLOR, pygame.Rect(col * cell_size, row * cell_size, cell_size, cell_size))

class Grid():
    def __init__(self, w, h, cell_size):
        self.height = h
        self.width = w
        self.cell_size = cell_size
        self.grid = [[0 for i in range(w)] for j in range(h)]
        self.functional_particles = []
        self.walls = []
    def draw(self, window):
        for el in self.functional_particles:
            r, c = el
            draw_water(r, c, window, self.cell_size)
        for wall in self.walls:
            r, c = wall
            draw_wall(r, c, window, self.cell_size)
    def convert_to_water(self, i, j):
        self.grid[i][j] = 1
        if(i, j) not in self.functional_particles:
            self.functional_particles.append((i, j))
        if (i, j) in self.walls:
            self.grid[i][j] = 1
            self.walls.remove((i, j))
    def convert_to_hole(self, i, j):
        self.grid[i][j] = 0
        if (i, j) in self.functional_particles:
            self.functional_particles.remove((i, j))
        if (i, j) in self.walls:
            self.grid[i][j] = 0
            self.walls.remove((i, j))
    def convert_to_wall(self, i, j):
        self.grid[i][j] = 2
        if (i, j) in self.functional_particles:
            self.functional_particles.remove((i, j))
        if (i, j) not in self.walls:
            self.walls.append((i, j))
    def update(self):
        for i in range(len(self.functional_particles)):
            particle = self.functional_particles[i]
            row, col = particle
            if row+1 >= self.height or self.grid[row+1][col] != 0:
                choices = []
                if col-1 >= 0 and self.grid[row][col-1] == 0:
                    choices.append((row, col-1))
                if col+1 < self.width and self.grid[row][col+1] == 0:
                    choices.append((row, col+1))
                if choices:
                    self.grid[row][col] = 0
                    r, c = choices[random.randint(0, len(choices)-1)]
                    self.grid[row][col] = 0
                    self.grid[r][c] = 1
                    self.functional_particles[i] = (r, c)
                continue
            self.grid[row][col] = 0
            self.grid[row+1][col] = 1
            self.functional_particles[i] = (row+1, col)