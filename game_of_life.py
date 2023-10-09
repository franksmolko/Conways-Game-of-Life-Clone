import pygame as pg

pg.init()

pg.display.set_caption("Game of Life")

icon = pg.image.load()

W = 1000

H = 1000

G = 20

R = H // G

C = W // G

WHITE = (227,28,121)#(255, 255, 255) 

BLACK = (50, 205, 50)#(0, 0, 0)

class Cell:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.x = col * G
        self.y = row * G 
        self.width = G
        self.height = G 
        self.life = False
        self.color = WHITE
    def draw(self, window):
        pg.Rect(self.x, self.y, self.width, self.height)
        pg.draw.rect(window, self.color, (self.x, self.y, self.width, self.height))

def draw_grid(window):
    for x in range(0, W, G):
        pg.draw.line(window, BLACK, (x, 0), (x, H))
    for y in range(0, H, G):
        pg.draw.line(window, BLACK, (0, y), (W, y))

def click(mouseX, mouseY):
    for row in grid:
        for cell in row:
            if cell.x <= mouseX < cell.x + cell.width and cell.y <= mouseY < cell.y + cell.height:
                if cell.life == False:
                    cell.color = BLACK
                    cell.life = True
                elif cell.life == True:
                    cell.color = WHITE
                    cell.life = False

def status(grid):
    rows = len(grid)
    cols = len(grid[0])


    for row in range(rows):
        for col in range(cols):
            weight = 0
            if col + 1 < cols:
                if grid[row][col+1].life:
                    weight += 1
                if row + 1 < rows:
                    if grid[row+1][col+1].life:
                        weight += 1
                if row - 1 >= 0:
                    if grid[row-1][col+1].life:
                        weight += 1
                
            if col - 1 >= 0:
                if grid[row][col-1].life:
                    weight += 1
                if row + 1 < rows:
                    if grid[row+1][col-1].life:
                        weight += 1
                if row - 1 >= 0:
                    if grid[row-1][col-1].life:
                        weight += 1
            
            if row + 1 < rows:
                if grid[row+1][col].life:
                    weight += 1
            
            if row - 1 >= 0:
                if grid[row-1][col].life:
                    weight += 1

            if weight == 3:
                grid[row][col].color = BLACK
                grid[row][col].life = True
            if weight > 3:
                grid[row][col].color = WHITE
                grid[row][col].life = False
            if weight < 3:
                grid[row][col].color = WHITE
                grid[row][col].life = False




window = pg.display.set_mode((W, H))

running = True

clock = pg.time.Clock()

grid = [[Cell(row, col) for col in range(C)] for row in range(R)]


start = False

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        
        if event.type == pg.MOUSEBUTTONDOWN and not start:
            mouseX, mouseY = pg.mouse.get_pos()
            click(mouseX, mouseY)

        if event.type == pg.KEYDOWN:
            if event.key == pg.K_RETURN:
                start = True
        
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_BACKSPACE:
                start = False
    
    window.fill(BLACK)
    
    if start:
        status(grid)
        pg.time.delay(100)

    for row in grid:
        for cell in row:
            cell.draw(window)
    
    draw_grid(window)

    pg.display.update()
    
    clock.tick(10)

pg.quit()