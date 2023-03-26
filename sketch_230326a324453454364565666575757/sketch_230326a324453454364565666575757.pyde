y = 0


def setup():
    size(600,600)
    frameRate(10)
    
def draw():
    t = 300
    global y
    x = 0
    if keyPressed:
        if key == 'w' :
            y = 255
        if key == 's' :
            y = 0
        if key == 'a' :
            y = 140
    for i in range(10):
        fill(y,y,y)
        rect(300,300,t,t)
        #y = y + 1
        t = t - 10
        #y = y + 1
    
