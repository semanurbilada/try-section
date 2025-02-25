import math
import pygame
from queue import PriorityQueue

WIDTH = 800
WIN = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("A* Path Finding Algorithm")

RED = (255, 0, 0) # already visited
GREEN = (0, 255, 0)
BLUE = (0, 255, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255) # square: not looked at, could be visited
BLACK = (0, 0, 0) # barrier: should be avoid
PURPLE = (128, 0, 128) # path
ORANGE = (255, 165, 0) # start Node
GREY = (128, 128, 128)
TURQUOISE = (64, 224, 208)

# class Node:
class Spot:
    def __init__(self, row, col, widht, total_rows):
        self.row = row
        self.col = col
        self.x = row * widht
        self.y = col * widht
        self.color = WHITE
        self.neighbors = []
        self.width = widht
        self.total_rows = total_rows

    def get_pos(self):
        return self.row, self.col
    
    def is_closed(self):
        return self.color == RED

    def is_open(self):
        return self.color == GREEN

    def is_barrier(self):
        return self.color == BLACK
    
    def is_start(self):
        return self.color == ORANGE
    
    def is_end(self):
        return self.color == TURQUOISE
    
    def reset(self):
        return self.color == WHITE
    
    def make_closed(self):
        return self.color == RED
    
    def make_open(self):
        return self.color == GREEN
    
    def make_barrier(self):
        return self.color == BLACK
    
    # def make_start(self):
    #     return self.color == ORANGE
    
    def make_end(self):
        return self.color == TURQUOISE
    
    def make_path(self):
        return self.color == PURPLE
    
    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.width))

    def update_neightbors(self, grid):
        pass

    def __lt__(self, other):
        return False

def h(p1, p2):
    pass 

# # This draw_grid will take less time to execute
# def draw_grid(win, rows, width):
# 	gap = width // rows
# 	for i in range(rows):
# 		pygame.draw.line(win, GREY, (0, i * gap), (width, i * gap))
# 		pygame.draw.line(win, GREY, (i * gap, 0), (i * gap, width))