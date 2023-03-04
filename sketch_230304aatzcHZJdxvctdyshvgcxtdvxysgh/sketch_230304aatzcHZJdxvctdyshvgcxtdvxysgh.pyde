bg = 1
dg = 0
sg = 0
cg = False
wg = False
clicked = False

def setup():
    size(600,600)
    
    
    
    
def draw():
    global bg, sg, dg, clicked, cg, wg
    clear()
    text(sg,500,100)
    rect(50,50,150,50)
    rect(250,150,150,50)
    rect(250,250,150,50)
    rect(50,150,150,50)
    sg = sg + 1
    if clicked == 1:
        text("banzai",500,200)
        rect(500,400,100,30)
        rect(540,460,20,-200)
    if cg == 1:
        text("la la la",100,450)
        triangle(100,300,0,400,200,400)
        ellipse(100,250,100,100)
    if wg == 1:
        text("rrrrr",300,450)
        rect(300,500,100,150)   
        
def mouseClicked():
    global bg, dg, sg, clicked, cg, wg

    if mouseX > 250 and mouseX < 400 and mouseY > 250 and mouseY < 300:
        text("sds",500,200)
        clicked = not(clicked)
        print(clicked)
    if mouseX > 50 and mouseX < 200 and mouseY > 150 and mouseY < 200:
        text("ля ля ля",500,200)
        cg = not(cg)
        print(cg)
        
        
    if mouseX > 50 and mouseX < 200 and mouseY > 50 and mouseY < 100:
        wg = not(wg)
        print(wg)
    #if mouseX > 250 and mouseX < 400 and mouseY > 150 and mouseY < 200:
