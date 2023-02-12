bg = 0
dg = 0
def setup():
    size(600,600)
    
    
    
    
def draw():
    global bg, dg
    clear
    text(dg,500,100)
    rect(50,50,150,50)
    rect(250,50,150,50)
    rect(250,150,150,50)
    rect(250,250,150,50)
    rect(50,150,150,50)
    
    push()
    strokeWeight(dg)
    stroke(bg)
    line(mouseX, mouseY, pmouseX, pmouseY)
    pop()
def mouseClicked():
    global bg, dg
    
    if mouseX > 250 and mouseX < 400 and mouseY > 250 and mouseY < 300:
        
        dg += 5
    if mouseX > 50 and mouseX < 200 and mouseY > 50 and mouseY < 200:
        dg -= 5
    
    
    
    
    
    
    
    
