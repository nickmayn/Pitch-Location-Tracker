import tkinter as tk
from pandastable import Table
import pandas as pd



class Game:
    """
    The purpose of this class is to wrap the tkinter gui with the data storage backend.
    """
    def __init__(self, name):
        height = 800
        width = 800
        margin = 200
        radius = 10
        rows = 3
        cols = 3
        self.root = tk.Tk()
        self.pitch_coords = {}
        self.pitch_results = {}
        self.idx = 1
        self.canvas = tk.Canvas(self.root, bg='#0d1524', height=height, width=width)
        self.name = name

    def forward_pitch(self):
        """
        When this method is called the canvas will display the next pitch. If no pitch has been charted it will generate an empty charting grid.
        """
        self.idx += 1
        self.canvas.delete('all')
        self.build_base_canvas()

        try:
            pitch_coord = self.pitch_coords[self.idx]
            pitch_result = self.pitch_results[self.idx]
            ball_color = setBallColor(pitch_result)
            self.canvas.create_oval(pitch_coord, fill=ball_color)

        except:
            record_pitch()
            

    def backward_pitch(self):
        if self.idx > 1:
            self.idx -= 1
        self.canvas.delete('all')
        self.build_base_canvas()

        try:
            pitch_coord = self.pitch_coords[self.idx]
            pitch_result = self.pitch_results[self.idx]
            ball_color = setBallColor(pitch_result)
            self.canvas.create_oval(pitch_coord, fill=ball_color)

        except:
            print('reached first pitch')




    def build_base_canvas(self):
        """
        Build the basic background of the charting tool.
        """
        # Set the parameters
        height = 800
        width = 800
        margin = 200
        radius = 10
        rows = 3
        cols = 3



        self.canvas.create_text(width/2,30,fill="white",font="Times 20 bold", text="Strikezone Grid")
        self.canvas.create_text(width-80,30,fill="white",font="Times 16 bold", text="Pitch: "+ str(self.idx))
                        
        # Build the strike zone coordinates
        x1 = round(width/2) - margin
        x2 = round(width/2) + margin
        y1 = round(height/2) - margin
        y2 = round(height/2) + margin

        coord = x1, y1, x2, y2

        xdist = x2-x1
        ydist = y2-y1

        def calcDim(x, numcell=3):
            return(round(x/numcell))

        xadd = calcDim(xdist, numcell=rows)
        yadd = calcDim(ydist, numcell=cols)

        for val in range(rows):
            for val2 in range(cols):
                self.canvas.create_rectangle(x1,y1, x1+(xadd*(val+1)), y1+(yadd*(val2+1)), outline='#bdbdbd')

        self.canvas.pack()