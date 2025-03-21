import pygame_functions as pg

pg.screenSize(900,900,50,50)
pg.setBackgroundColour("lightgreen")
pg.setAutoUpdate(False)

# put screen elements here, so they are global
infoLabel = pg.makeLabel("Info here",40,50,50,"black","Consolas")
pg.showLabel(infoLabel)
button = pg.makeSprite("button.png")
pg.moveSprite(button,600,100,centre=True)
pg.showSprite(button)

def drawScreen():
    # code to draw the stones
    pass

def setupGame():
    # create the data structure for a new game
    pass


def playerMove():
    # code to track mouse movements and do actions, then return their move
    moveMade = False
    while not moveMade:
        if pg.spriteClicked(button):
            pg.changeLabel(infoLabel, f"Button clicked")
        elif pg.mousePressed():
            pg.changeLabel(infoLabel, f"Clicked at {pg.mouseX()} , {pg.mouseY()}")

        pg.updateDisplay()
        pg.tick(50)
    return 1

# main game
setupGame()
gameRunning = True
while gameRunning:
    move = playerMove()
