y=500
x=500
d=1000
b=500
r=1000
e=500
u=1000
o=500
h=1000
l=500
k=100
def setup():
    size(1000,1000)
def draw():
    global y, x, d, b, r, e, u, o, h, l, k
    fill(0)
    background(255)
    ellipse(x,y,50,50)
    if keyPressed:
        if key == 'w':
            y=y-5
        if key == 's':
            y=y+5
        if key == 'a':
            x=x-5
        if key == 'd':
            x=x+5
   
    textSize(20)
    text(k,20,30)
        
    rect(d,b,200,100)
    
    d = d - random(1,20)
    if d <= 0:
        d = 1000
        b = random(0,900)
    if x > d and y > b and x > d + 200 and y > b + 100:
        k-=1
        

    rect(r,e,200,100)
    r = r - random(1,20)
    if r <= 0:
        r = 1000
        e = random(0,900)
    if x > r and y > e and x > r + 200 and y > e + 100:
        k-=1

    rect(u,o,200,100)
    
    u = u - random(1,20)
    if u <= 0:
        u = 1000
        o = random(0,900)
    if x > d and y > b and x > d + 200 and y > b + 100:
        k-=1
    
    rect(h,l,200,100)
    
    h = h - random(1,20)
    if h <= 0:
        h = 1000
        l = random(0,900)
    if x > d and y > b and x > d + 200 and y > b + 100:
        k-=1
    
