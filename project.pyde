x = 0
y = 0
a = 0
b = 0
c = 0
def collidePointRect(pointX, pointY, x, y, xW, yW):
    if (pointX >= x) and (pointX <= x + xW) and (pointY >= y) and (pointY <= y + yW): 
        return True
    return False

def setup ():
    size (700,400)
def draw ():
    global x, y, a, b, c
    for x in range (100,700,20):
        for y in range (0,400,20):
            rect (x,y,20,20)
            if collidePointRect(mouseX, mouseY, x, y, 20, 20):
                fill(a,b,c)
                rect (x,y,20,20)
                fill (255)
            else:
                fill(255)
    strokeWeight (1)
    point (mouseX,mouseY)
    strokeWeight (1)
    fill (255)
    rect (0,0,100,400)
    fill (1)
    rect (20,20,60,30)
    fill (255)
    rect (20,70,60,30)
    fill (255,0,0)
    rect (20,120,60,30)
    fill (255)
def mouseClicked ():
    global a ,b ,c
    if mouseX>20 and mouseX <80 and mouseY >20 and mouseY <50:
        a = 1
        b = 0
        c = 0
    if mouseX >20 and mouseX < 80 and mouseY >70 and mouseY <100:
        a = 255
        b = 255
        c = 255
    if mouseX > 20 and mouseX <80 and mouseY >120 and mouseY <170:
        a = 255
        b = 0
        c = 0
        
    
