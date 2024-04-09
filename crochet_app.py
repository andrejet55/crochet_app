#Crochet app for counting rows

from tkinter import *

root = Tk()

# Welcome to the app
root.title("Crochet app")
title = Label(root, text="Wellcome to the Crochet app", 
              font=("Arial", 20,"bold"))

info = Label(root, text="You can count your crochet rows as you develop a project",
             font=("Arial", 15))

imagen = PhotoImage(file="images/crochet.png")
knit_img = Label(root, image=imagen, bd=0)

# Variable for counting rows

n_rows=0

# Label that shows current row

rows_label = Label(root, text="You are in the row: " + str(n_rows), font=("Arial",20))


# Functions to add and substract rows

def add_rows():
    global n_rows
    n_rows+=1
    rows_label.config(text="You are in the row: " + str(n_rows))
    
def substract_rows():
    global n_rows
    if n_rows >0:
        n_rows-=1
    rows_label.config(text="You are in the row: " + str(n_rows))

# Button for increase and decrease number of rows    

addRows_bt = Button(root,text="+", font=(25), padx=25,pady=25, command=add_rows)
substractRows_bt = Button(root, text="-", font=(25),padx=25,pady=25, command=substract_rows)

# Placement of the elements in the app

title.grid(row=0,column=0)
info.grid(row=1,column=0)
knit_img.grid(row=2, column=0)
addRows_bt.grid(row=3, column=0)
substractRows_bt.grid(row=5, column=0)
rows_label.grid(row=4, column=0)
root.mainloop()