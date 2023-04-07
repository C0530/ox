import tkinter as tk
import random

win=tk.Tk()
color = random.choice(("lightgreen","lightblue"))
check=0
def again():
	global color
	play.won.destroy()
	play.retry.destroy()
	play.newgame.destroy()
	play.b1.config(bg="#d9d9d9")
	play.b2.config(bg="#d9d9d9")
	play.b3.config(bg="#d9d9d9")
	color= random.choice(("lightgreen","lightblue"))
	frame.config(bg=color)
	for i in range(9):
		x[i].config(state="normal",text="")

def newgame():
	global color
	play.won.destroy()
	play.retry.destroy()
	play.newgame.destroy()
	color= random.choice(("lightgreen","lightblue"))
	frame.config(bg=color)
	for i in range(9):
		x[i].config(state="normal",text="",bg="#d9d9d9")	
	l1.config(text="0")
	l2.config(text="0")
	
	
def drawagain():
	global color
	play.newgame.destroy()
	play.won.destroy()
	play.retry.destroy()
	color= random.choice(("lightgreen","lightblue"))
	frame.config(bg=color)
	for i in range(9):
		x[i].config(state="normal",text="")

			
def donegreen(b1,b2,b3):
	global check
	play.b1.config(bg="lightgreen")
	play.b2.config(bg="lightgreen")
	play.b3.config(bg="lightgreen")
	frame.config(bg="lightgreen")
	score=int(l2['text'])+1
	l2.config(text=score)
	for i in range(9):
		x[i].config(state="disabled")
	play.won=tk.Label(win,text="O won",bg="lightgreen", height=3,width=40)
	play.won.place(x=0,y=150)
	play.retry=tk.Button(win,text="PLAY AGAIN",height=2,width=15)			
	play.retry.place(x=0,y=1000)
	play.retry.config(command=again)
	play.newgame=tk.Button(win,text="NEW GAME",height=2,width=15)
	play.newgame.place(x=370,y=1000)
	play.newgame.config(command=newgame)
	check=0
	
def doneblue(b1,b2,b3):
	global check
	play.b1.config(bg="lightblue")
	play.b2.config(bg="lightblue")
	play.b3.config(bg="lightblue")
	frame.config(bg="lightblue")
	score=int(l1['text'])+1
	l1.config(text=score)
	for i in range(9):
		x[i].config(state="disabled")
	play.won=tk.Label(win,text="X won",bg="lightblue", height=3,width=40)
	play.won.place(x=0,y=150)
	play.retry=tk.Button(win,text="PLAY AGAIN",height=2,width=15)			
	play.retry.place(x=0,y=1000)
	play.retry.config(command=again)
	play.newgame=tk.Button(win,text="NEW GAME",height=2,width=15)
	play.newgame.place(x=370,y=1000)
	play.newgame.config(command=newgame)
	check=0


def play(z):
	global color
	play.b1=0
	play.b2=0
	play.b3=0
	txt=x[z]['text']
	if txt =="":
		if color == "lightgreen":
			x[z].config(text="O")
			color="lightblue"
			frame.config(bg=color)		
		elif color == "lightblue":
			x[z].config(text="X")
			color="lightgreen"
			frame.config(bg=color)

# O row			
		if x[0]['text'] =="O" and x[1]['text'] == "O" and x[2]['text'] == "O":
			play.b1=x[0]
			play.b2=x[1]
			play.b3=x[2]
			donegreen(play.b1,play.b2,play.b3)
		elif x[3]['text'] =="O" and x[4]['text'] =="O" and x[5]['text'] =="O":
			play.b1=x[3]
			play.b2=x[4]
			play.b3=x[5]
			donegreen(play.b1,play.b2,play.b3)
		elif x[6]['text'] =="O" and x[7]['text'] =="O" and x[8]['text'] =="O":
			play.b1=x[6]
			play.b2=x[7]
			play.b3=x[8]
			donegreen(play.b1,play.b2,play.b3)
#O column
		elif x[0]['text'] =="O" and x[3]['text'] =="O" and x[6]['text'] =="O":
			play.b1=x[0]
			play.b2=x[3]
			play.b3=x[6]
			donegreen(play.b1,play.b2,play.b3)
			
		elif x[1]['text'] =="O" and x[4]['text'] =="O" and x[7]['text'] =="O":
			play.b1=x[1]
			play.b2=x[4]
			play.b3=x[7]
			donegreen(play.b1,play.b2,play.b3)
					
		elif x[2]['text'] =="O" and x[5]['text'] =="O" and x[8]['text'] =="O":
			play.b1=x[2]
			play.b2=x[5]
			play.b3=x[8]
			donegreen(play.b1,play.b2,play.b3)	
# O cross							
		elif x[0]['text'] =="O" and x[4]['text'] =="O" and x[8]['text'] =="O":
			play.b1=x[0]
			play.b2=x[4]
			play.b3=x[8]
			donegreen(play.b1,play.b2,play.b3)
			
		elif x[2]['text'] =="O" and x[4]['text'] =="O" and x[6]['text'] =="O":
			play.b1=x[2]
			play.b2=x[4]
			play.b3=x[6]
			donegreen(play.b1,play.b2,play.b3)			
# X row
		elif x[0]['text'] =="X" and x[1]['text'] =="X" and x[2]['text'] =="X":
			play.b1=x[0]
			play.b2=x[1]
			play.b3=x[2]
			doneblue(play.b1,play.b2,play.b3)

		elif x[3]['text'] =="X" and x[4]['text'] =="X" and x[5]['text'] =="X":
			play.b1=x[3]
			play.b2=x[4]
			play.b3=x[5]
			doneblue(play.b1,play.b2,play.b3)

		elif x[6]['text'] =="X" and x[7]['text'] =="X" and x[8]['text'] =="X":
			play.b1=x[6]
			play.b2=x[7]
			play.b3=x[8]
			doneblue(play.b1,play.b2,play.b3)
# X column		
		elif x[0]['text'] =="X" and x[3]['text'] =="X" and x[6]['text'] =="X":
			play.b1=x[0]
			play.b2=x[3]
			play.b3=x[6]
			doneblue(play.b1,play.b2,play.b3)
		
		elif x[1]['text'] =="X" and x[4]['text'] =="X" and x[7]['text'] =="X":
			play.b1=x[1]
			play.b2=x[4]
			play.b3=x[7]
			doneblue(play.b1,play.b2,play.b3)

		elif x[2]['text'] =="X" and x[5]['text'] =="X" and x[8]['text'] =="X":
			play.b1=x[2]
			play.b2=x[5]
			play.b3=x[8]
			doneblue(play.b1,play.b2,play.b3)
# X cross
		elif x[0]['text'] =="X" and x[4]['text'] =="X" and x[8]['text'] =="X":
			play.b1=x[0]
			play.b2=x[4]
			play.b3=x[8]
			doneblue(play.b1,play.b2,play.b3)
		
		elif x[2]['text'] =="X" and x[4]['text'] =="X" and x[6]['text'] =="X":
			play.b1=x[2]
			play.b2=x[4]
			play.b3=x[6]
			doneblue(play.b1,play.b2,play.b3)
#draw
		else:
			global check			
			check+=1
			if check==9:
				check=0
				play.won=tk.Label(win,text="Draw",bg="orange", height=3,width=40)
				play.won.place(x=0,y=150)
				play.retry=tk.Button(win,text="PLAY AGAIN",height=2,width=15)
				play.retry.place(x=0,y=1000)
				play.retry.config(command=drawagain)
				play.newgame=tk.Button(win,text="NEW GAME",height=2,width=15)
				play.newgame.place(x=370,y=1000)
				play.newgame.config(command=newgame)



l1=tk.Label(win,text="0",bg="lightblue",width=20,height=3)
l1.place(x=0,y=0)
l2=tk.Label(win,text="0",bg="lightgreen",width=20,height=3)
l2.place(x=370,y=0)

frame=tk.Frame(win,bg = color,width=600,height=550)
frame.place(x=55,y=330)

b00=tk.Button(win,text="",height=3,width=5,command=lambda z=0 : play(z))
b00.place(x=80,y=360)

b01=tk.Button(win,text="",height=3,width=5,command=lambda z=1 : play(z))
b01.place(x=270,y=360)

b02=tk.Button(win,text="",height=3,width=5,command=lambda z=2 : play(z))
b02.place(x=460,y=360)


b10=tk.Button(win,text="",height=3,width=5,command=lambda z=3 : play(z))
b10.place(x=80,y=530)

b11=tk.Button(win,text="",height=3,width=5,command=lambda z=4 : play(z))
b11.place(x=270,y=530)

b12=tk.Button(win,text="",height=3,width=5,command=lambda z=5 : play(z))
b12.place(x=460,y=530)


b20=tk.Button(win,text="",height=3,width=5,command=lambda z=6 : play(z))
b20.place(x=80,y=700)

b21=tk.Button(win,text="",height=3,width=5,command=lambda z=7 : play(z))
b21.place(x=270,y=700)

b22=tk.Button(win,text="",height=3,width=5,command=lambda z=8 : play(z))
b22.place(x=460,y=700)

x=[b00,b01,b02,b10,b11,b12,b20,b21,b22]		
win.mainloop()
