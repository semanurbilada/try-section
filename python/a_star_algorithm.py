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
    
    def make_start(self):
        return self.color == ORANGE
    
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
    
    print("Class done!\n")

def h(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    p2 = (1,9)
    return abs(x1 - x2) + abs(y1 - y2)
print("Func h done!\n")

def make_grid(rows, width):
    grid = []
    gap = width // rows
    for i in range(rows):
        grid.append([])
        for j in range(rows):
            spot = Spot(i, j, gap, rows)
            grid[i].append(spot)

    return grid
print("Func make grid done!\n")

def draw_grid(win, rows, width):
    gap = width // rows
    for i in range(rows):
        pygame.draw.line(win, GREY, (0, i * gap), (width, i * gap))
        for j in range(rows):
            pygame.draw.line(win, GREY, (j * gap, 0), (j * gap, width))
    # # Alternative
    # for i in range(rows):
    #     pygame.draw.line(win, GREY, (i * gap, 0), (i * gap, width))
    #     pygame.draw.line(win, GREY, (0, i * gap), (width, i * gap))
print("Func draw grid done!\n")

def draw(win, grid, rows, width):
    win.fill(WHITE)

    for row in grid:
        for spot in row:
            spot.draw(win)

    draw_grid(win, rows, width)
    pygame.display.update()
print("Func draw done!\n")

def get_clicked_pos(pos, rows, width):
    gap = width // rows
    y, x = pos
    
    row = y // gap
    col = x // gap
    return row, col
print("Func get clicked pos done!\n")

def main(win, width):
    ROWS = 50
    grid = make_grid(ROWS, width)

    start = None
    end = None

    run = True
    started = False
    while run:
        draw(win, grid, ROWS, width)
        print("Draw?!\n")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if started:
                continue

            if pygame.mouse.get_pressed()[0]: # left mouse button
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(pos, ROWS, width)
                spot = grid[row][col]
                if not start:
                    start = spot
                    start.make_start()

                elif not end:
                    end = spot
                    end.make_end()

                elif spot != end and spot != start:
                    spot.make_barrier()
            
            elif pygame.mouse.get_pressed()[2]: # right mouse button
                pass
            
    pygame.quit()

main(WIN, WIDTH)