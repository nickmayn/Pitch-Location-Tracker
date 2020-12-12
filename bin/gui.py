import tkinter as tk
from pandastable import Table
import pandas as pd

pitch_result = 'strike'
pitch_type = 'fastball'
pitch = None
ball_color = 'Red'
pitches = {}
pitch_idx = 1
current_idx = 1



df = pd.DataFrame(columns = ["x", "y", "pitch_type"])

base = tk.Tk()

# Set the parameters
height = 800
width = 800
margin = 200
radius = 10
rows = 3
cols = 3



# Build the basic gui
C = tk.Canvas(base, bg='#0d1524', height =height, width=width)
C.create_text(width/2,30,fill="white",font="Times 20 bold",
                        text="Strikezone Grid")



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
        C.create_rectangle(x1,y1, x1+(xadd*(val+1)), y1+(yadd*(val2+1)), outline='#bdbdbd')



#C2 = tk.Canvas(base, bg='White', height =height, width=width)
#pt = Table(C2, dataframe=df, showtoolbar=True, showstatusbar=True)
#pt.show()

C.pack()


def recordClick(event):
    global df
    global pitch
    global ball_color
    global pitches
    global pitch_idx
    if pitch is not None:
        C.delete(pitch)
    x, y = event.x, event.y

    pitch = C.create_oval(x-radius, y-radius, x+radius, y+radius, outline='black', fill=ball_color)

    pitches[pitch_idx] = C.coords(pitch)
    pitch_idx+=1
    current_idx+=1
    #print(C.coords(pitch))
    #print(C.coords(pitches[1]))
    print(pitches)

def changeBall(event):
    global pitch_result
    global ball_color
    pitch_result = 'ball'
    ball_color = 'blue'

def changeStrike(event):
    global pitch_result
    global ball_color
    pitch_result = 'strike'
    ball_color = 'red'

def setBallColor(pitch_result)
    if pitch_result

def backPitch(event):
    global current_idx
    global pitches
    global pitch_result

    current_idx -= 1

    
    C.create_oval(pitches[current_idx], fill=)




    
    

base.bind('<Button-1>', recordClick)
base.bind('<w>', changeStrike)
base.bind('<e>', changeBall)

base.mainloop()



