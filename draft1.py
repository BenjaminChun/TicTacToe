from tkinter import *
root=Tk()

root.title("Tic Tac Toe")

#stored values
p1=StringVar()
p2=StringVar()


#commands
def disableplayername():
	button2=Button(root,text='Confirm',padx=5,pady=3,state=DISABLED)
	button1=Button(root,text='Confirm',padx=5,pady=3,state=DISABLED)
	button1.grid(row=1,column=4)
	button2.grid(row=2,column=4)

def enablebutton2():
	button2=Button(root,text='Confirm',padx=5,pady=3,state=NORMAL,command=disableplayername)
	button2.grid(row=2,column=4)
	button1=Button(root,text='Confirm',padx=5,pady=3,state=DISABLED)
	button1.grid(row=1,column=4)

#creating widget
Player1=Entry(root,textvariable=p1)
Player2=Entry(root,textvariable=p2)
button1=Button(root,text='Confirm',padx=5,pady=3,command=enablebutton2)
button2=Button(root,text='Confirm',padx=5,pady=3,state=DISABLED)

box1=Button(root,padx=30,pady=10,relief=GROOVE)
box2=Button(root,padx=30,pady=10,relief=GROOVE)
box3=Button(root,padx=30,pady=10,relief=GROOVE)
box4=Button(root,padx=30,pady=10,relief=GROOVE)
box5=Button(root,padx=30,pady=10,relief=GROOVE)
box6=Button(root,padx=30,pady=10,relief=GROOVE)
box7=Button(root,padx=30,pady=10,relief=GROOVE)
box8=Button(root,padx=30,pady=10,relief=GROOVE)
box9=Button(root,padx=30,pady=10,relief=GROOVE)

#positioning widget
Player1.grid(row=1,column=1, columnspan=2)
Player2.grid(row=2,column=1, columnspan=2)
button1.grid(row=1,column=3)
button2.grid(row=2,column=3)
box1.grid(row=3,column=1,sticky=N)
box2.grid(row=3,column=2,sticky=N)
box3.grid(row=3,column=3,sticky=N)
box4.grid(row=4,column=1)
box5.grid(row=4,column=2)
box6.grid(row=4,column=3)
box7.grid(row=5,column=1,sticky=S)
box8.grid(row=5,column=2,sticky=S)
box9.grid(row=5,column=3,sticky=S)





root.mainloop()