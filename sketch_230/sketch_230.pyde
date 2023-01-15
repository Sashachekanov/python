x = 0

def setup():
    size(600,600)
    frameRate (100)
    
def draw():
    clear()
    global x
    translate(300,300)
    rotate(radians(x))
    triangle(0,-300,200,200,-200,200)
    x = x + 1
