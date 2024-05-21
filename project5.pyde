a = 1
b = 1
c = 1
grid_size = 20
cols = 30
rows = 15
grid = [[False for _ in range(cols)] for _ in range(rows)]
changed_pixels = [[False for _ in range(cols)] for _ in range(rows)]
original_colors = [[color(255) for _ in range(cols)] for _ in range(rows)]
colors = [[color(255) for _ in range(cols)] for _ in range(rows)]

def setup():
    size(cols * grid_size, rows * grid_size)

def draw():
    global grid, changed_pixels, a, b, c, original_colors
    background(255)
    for i in range(rows):
        for j in range(cols):
            x = j * grid_size
            y = i * grid_size
            if grid[i][j]:
                fill(colors[i][j])
            else:
                fill(255)
            rect(x, y, grid_size, grid_size)
    rect(0, 0, 100, 400)
    fill(1, 1, 1)
    rect(17, 20, 70, 30)
    fill(255, 0, 0)
    rect(17, 70, 70, 30)
    fill (0,255,0)
    rect (17,120,70,30)
    fill (0,0,255)
    rect (17,170,70,30)
    fill (255,255,255)
    rect (17,250,70,30)
    fill (0,255,0)

    if mousePressed:
        col = mouseX // grid_size
        row = mouseY // grid_size
        if not changed_pixels[row][col]:
            grid[row][col] = not grid[row][col]
            changed_pixels[row][col] = True
            colors[row][col] = color(a, b, c)
    fill (255)
    text (u"Чёрный",25,40)
    text (u"Красный",25,90)
    text (u"Зелёный",25,140)
    text (u"Синий",25,190)
    fill (1)
    text (u"Очистить",25,270)

def mouseClicked():
    global a, b, c, changed_pixels, colors
    if mouseX > 20 and mouseX < 80 and mouseY > 20 and mouseY < 50:
        a, b, c = 1, 0, 0
    if mouseX > 20 and mouseX < 80 and mouseY > 70 and mouseY < 100:
        a, b, c = 255, 0, 0
    if mouseX > 20 and mouseX < 80 and mouseY > 120 and mouseY < 150:
        a, b ,c = 0, 255, 0
    if mouseX > 20 and mouseX < 80 and mouseY > 170 and mouseY < 200:
        a, b ,c = 0, 0, 255
    if mouseX > 20 and mouseX < 80 and mouseY > 250 and mouseY < 280:
        for i in range(rows):
            for j in range(cols):
                changed_pixels[i][j] = False
                colors[i][j] = original_colors[i][j]
                grid[i][j] = False
                
