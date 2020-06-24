from tkinter import *
from PIL import ImageTk,Image
import tkinter.messagebox

root=Tk()
root.title('tic tac toe')
root.iconbitmap('C:/Users/User/gui/logo.ico')


player1turn=True

def bclick(button):
	global player1turn
	if button['text']=='' and player1turn==True:
		button['text']='X'
		checkforwin()
		player1turn=False

	elif button['text']=='' and player1turn!=True:
		button['text']='O'
		checkforwin()
		player1turn=True
	elif button['text']!='':
		tkinter.messagebox.showerror(title='Tic Tac Toe',message='Please choose another box')
def checkforwin():
	if box1['text']==box2['text'] and box1['text']==box3['text'] and box1['text']!='' and box2['text']!='' and box3['text']!='':
		tkinter.messagebox.showinfo(title="Tic Tac Toe",message='Congrats we have a winner')
	if box4['text']==box5['text'] and box5['text']==box6['text'] and box4['text']!='' and box5['text']!='' and box6['text']!='':
		tkinter.messagebox.showinfo(title="Tic Tac Toe",message='Congrats we have a winner')	
	if box7['text']==box8['text'] and box9['text']==box3['text'] and box7['text']!='' and box8['text']!='' and box9['text']!='':
		tkinter.messagebox.showinfo(title="Tic Tac Toe",message='Congrats we have a winner')
	if box1['text']==box5['text'] and box9['text']==box1['text'] and box1['text']!='' and box5['text']!='' and box9['text']!='':
		tkinter.messagebox.showinfo(title="Tic Tac Toe",message='Congrats we have a winner')
	if box3['text']==box5['text'] and box7['text']==box3['text'] and box3['text']!='' and box5['text']!='' and box7['text']!='':
		tkinter.messagebox.showinfo(title="Tic Tac Toe",message='Congrats we have a winner')
	if box1['text']==box4['text'] and box7['text']==box1['text'] and box1['text']!='' and box4['text']!='' and box7['text']!='':
		tkinter.messagebox.showinfo(title="Tic Tac Toe",message='Congrats we have a winner')
	if box2['text']==box5['text'] and box8['text']==box2['text'] and box2['text']!='' and box5['text']!='' and box8['text']!='':
		tkinter.messagebox.showinfo(title="Tic Tac Toe",message='Congrats we have a winner')
	if box3['text']==box6['text'] and box9['text']==box3['text'] and box3['text']!='' and box6['text']!='' and box9['text']!='':
		tkinter.messagebox.showinfo(title="Tic Tac Toe",message='Congrats we have a winner')
box1=Button(root,text='',padx=30,pady=10,relief=GROOVE,command=lambda: bclick(box1))
box2=Button(root,text='',padx=30,pady=10,relief=GROOVE,command=lambda: bclick(box2))
box3=Button(root,text='',padx=30,pady=10,relief=GROOVE,command=lambda: bclick(box3))
box4=Button(root,text='',padx=30,pady=10,relief=GROOVE,command=lambda: bclick(box4))
box5=Button(root,text='',padx=30,pady=10,relief=GROOVE,command=lambda: bclick(box5))
box6=Button(root,text='',padx=30,pady=10,relief=GROOVE,command=lambda: bclick(box6))
box7=Button(root,text='',padx=30,pady=10,relief=GROOVE,command=lambda: bclick(box7))
box8=Button(root,text='',padx=30,pady=10,relief=GROOVE,command=lambda: bclick(box8))
box9=Button(root,text='',padx=30,pady=10,relief=GROOVE,command=lambda: bclick(box9))

player1label=Label(root,text='Player 1:')
player1entry=Entry(root)
player2label=Label(root,text='Player 2:')
player2entry=Entry(root)

box1.grid(row=3,column=1)
box2.grid(row=3,column=2)
box3.grid(row=3,column=3)
box4.grid(row=4,column=1)
box5.grid(row=4,column=2)
box6.grid(row=4,column=3)
box7.grid(row=5,column=1)
box8.grid(row=5,column=2)
box9.grid(row=5,column=3)

player1label.grid(row=1,column=1)
player1entry.grid(row=1,column=2,columnspan=2)
player2label.grid(row=2,column=1)
player2entry.grid(row=2,column=2,columnspan=2)

root.mainloop()