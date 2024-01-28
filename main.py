from utils import *

n_of_cells = 100
screen_width = 800
screen_height = 800
cell_size = screen_width//n_of_cells
window = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("sand simulation")
running = True
grid = Grid(n_of_cells, n_of_cells, cell_size)
while running:
    pygame.time.Clock().tick(60)
    window.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break
    if pygame.mouse.get_pressed()[0]:
        x, y = pygame.mouse.get_pos()
        col, row = convert(x, y, cell_size)
        grid.convert_to_water(row, col)
    if pygame.mouse.get_pressed()[2]:
        x, y = pygame.mouse.get_pos()
        col, row = convert(x, y, cell_size)
        grid.convert_to_hole(row, col)
    if pygame.mouse.get_pressed()[1]:
        x, y = pygame.mouse.get_pos()
        col, row = convert(x, y, cell_size)
        grid.convert_to_wall(row, col)
    grid.update()
    grid.draw(window)
    pygame.display.flip()

pygame.quit()