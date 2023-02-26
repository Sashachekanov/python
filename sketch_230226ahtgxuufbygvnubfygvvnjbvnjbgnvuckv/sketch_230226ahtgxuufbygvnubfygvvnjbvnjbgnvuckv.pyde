bg = 1
dg = 0
sg = "levo"
def setup():
    size(600,600)




def draw():
    clear()
    global bg, dg, sg
    text(dg,500,100)
    rect(50,50,150,50)
    rect(250,150,150,50)
    rect(250,250,150,50)
    rect(50,150,150,50)


    translate(200,300)
    rotate(radians(dg))
    rect(250,50,150,50)
    if sg == "pravo":
        dg += bg
    if sg == "levo":
        dg -= bg
def mouseClicked():
    global bg, dg, sg

    if mouseX > 250 and mouseX < 400 and mouseY > 250 and mouseY < 300:

        bg += 5
    if mouseX > 50 and mouseX < 200 and mouseY > 50 and mouseY < 200:
        bg -= 5
    if mouseX > 50 and mouseX < 200 and mouseY > 50 and mouseY < 100:
        clear()
    if mouseX > 250 and mouseX < 400 and mouseY > 150 and mouseY < 200:
        if sg == "pravo":
            sg = "levo"
        else:
            sg = "pravo"
        
