import tkinter as tk
from tkinter import font as tkFont
import random

class Main(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.geometry("950x900+0+0")
        self.theCanvas = tk.Canvas(self,width=800, height=900, bg="#ddddff")
        self.theCanvas.grid(row=0, column=0)
        self.buttonfont = tkFont.Font(family="Consolas", weight="bold")

        self.button1 = tk.Button(self, text="Normal Button", font=self.buttonfont, command = self.buttonClicked)
        self.button1.grid(row=0, column=1)

        self.theCanvas.bind("<Motion>", self.mouseMoved)
        self.theCanvas.bind("<Button-1>", self.mouseClicked)

        self.buttonPic = tk.PhotoImage(file="button.png")
        self.clicked = tk.PhotoImage(file="click.png")
        
        self.canvasbutton = self.theCanvas.create_image(200,800,image = self.buttonPic)
        self.theCanvas.tag_bind(self.canvasbutton, "<Button-1>", self.canvasButtonClicked)
        
        self.chipPic = tk.PhotoImage(file="chip.png")
        self.piles = [7,5,3,1]
        
        

        self.NewGameButton = tk.PhotoImage(file="NewGameButton.png")
        self.theCanvas.create_image(200,850,image = self.NewGameButton)

        self.PCMoveButton = tk.PhotoImage(file="PCMove.png")
        self.theCanvas.create_image(600,850,image = self.PCMoveButton)

        

        self.chipPics = []


        self.pileChosen = None

        self.movetext=None
        self.clickText = None
        self.buttonText = None
        self.drawPiles()
        self.mainloop()




    def buttonClicked(self):
        x = random.randint(100,700)
        y = random.randint(100,700)
        self.theCanvas.delete(self.buttonText)
        self.buttonText = self.theCanvas.create_text(x,y,text="tkinter Button clicked")

    def mouseMoved(self,e):
        self.theCanvas.delete(self.movetext)
        self.movetext = self.theCanvas.create_text(20,20, text=f"moved to {e.x}, {e.y}", anchor="nw")

    def mouseClicked(self,e):
        self.theCanvas.delete(self.clickText)
        self.clickText = self.theCanvas.create_text(750,20, text=f"Clicked at {e.x}, {e.y}", anchor="ne")
        row = 3-(e.y // 200)
        print(row)
        if self.pileChosen is None:
            self.pileChosen = row
        if row != self.pileChosen and row != -1:
            print("Only one row")
            return
        if row == 0:
            self.piles[0] = self.piles[0] - 1 
            self.drawPiles()
        elif row == 1:
            self.piles[1] = self.piles[1] - 1 
            self.drawPiles()
        elif row == 2:
            self.piles[2] = self.piles[2] - 1 
            self.drawPiles()
        elif row == 3:
            self.piles[3] = self.piles[3] - 1 
            self.drawPiles()     

        if 530 < e.x < 670 and 830 < e.y < 870:
            self.computerMove()
            
        if 130 < e.x < 270 and 830 < e.y < 870:
            self.resetGame()    
            print("new game")
            
        
        print(self.piles)
            



    def canvasButtonClicked(self,e):
        self.theCanvas.itemconfigure(self.canvasbutton,image=self.clicked )
        self.after(1000,self.restorebutton)

    def restorebutton(self):
        self.theCanvas.itemconfigure(self.canvasbutton,image=self.buttonPic )

    def drawPiles(self):
        for chip in self.chipPics:
            self.theCanvas.delete(chip)
        x1 = 100
        y1 = 700
        for i in range(self.piles[0]):
            self.chipPics.append(self.theCanvas.create_image(x1,y1,image = self.chipPic))
            x1 = x1+100

        x2 = 200
        y2 = 500
        for i in range(self.piles[1]):
            self.chipPics.append(self.theCanvas.create_image(x2,y2,image = self.chipPic))
            x2 = x2+100   

        x3 = 300
        y3 = 300
        for i in range(self.piles[2]):
            self.chipPics.append(self.theCanvas.create_image(x3,y3,image = self.chipPic))
            x3 = x3+100    

        x4 = 400
        y4 = 100
        for i in range(self.piles[3]):
            self.chipPics.append(self.theCanvas.create_image(x4,y4,image = self.chipPic))
            x4 = x4+100  

    def resetGame(self):
        self.piles = [7,5,3,1]
        self.drawPiles()
        self.pileChosen = None

    def computerMove(self):
        self.pileChosen = None

app = Main()


        
