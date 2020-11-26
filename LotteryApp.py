from tkinter import *
from tkinter import messagebox
from random import sample
import random

#Creating a Window
window = Tk()
window.title("Gou Kyk™ Lottery!!!")
window.resizable(1000, 2000)

def check_prize():
    winning_num1 = gnrtd1.get()
    winning_num2 = gnrtd2.get()
    winning_num3 = gnrtd3.get()
    winning_num4 = gnrtd4.get()
    winning_num5 = gnrtd5.get()
    winning_bonusNum = gnrtd_bonus.get()

    winning_list = [winning_num1, winning_num2, winning_num3, winning_num4, winning_num5, winning_bonusNum]
    winning_list.sort()

    gnrtd = sorted(winning_list)

    if len(gnrtd) == len(winning_list):
        evn = set(gnrtd).intersection(set(winning_list))

        if len(evn) == 6:
            messagebox.showinfo("6 Matched!", "You Win R10 000 000")
        elif len(evn) == 5:
            messagebox.showinfo("5 Matched!", "You Win R8584")
        elif len(evn) == 4:
            messagebox.showinfo("4 Matched!", "You Win R2384")
        elif len(evn) == 3:
            messagebox.showinfo("3 Matched!", "You Win R100.50")
        elif len(evn) == 2:
            messagebox.showinfo("2 Matched!", "You Win R20")
        elif len(evn) == 1:
            messagebox.showinfo("1 Matched!.", "You Lost.")
        elif len(evn) == 0:
            messagebox.showinfo("0 Matched!", "You Lost.")
        
gnrtd1 = IntVar()
gnrtd2 = IntVar()
gnrtd3 = IntVar()
gnrtd4 = IntVar()
gnrtd5 = IntVar()
gnrtd_bonus = IntVar()

class ntrs:
    #creating the Entry Boxes for the User's Numbers
    num1_ntr = Entry(window, textvariable = gnrtd1, relief = 'groove', width = 5, bd = 4, text = "", fg = 'black', bg = 'cyan')
    num1_ntr.grid(row = 1, column = 4, padx = 5, pady = 7)
    num2_ntr = Entry(window, textvariable = gnrtd2, relief = 'groove', width = 5, bd = 4, text = "", fg = 'black', bg = 'yellow')
    num2_ntr.grid(row = 1, column = 5, padx = 5, pady = 7)
    num3_ntr = Entry(window, textvariable = gnrtd3, relief = 'groove', width = 5, bd = 4, text = "", fg = 'black', bg = 'red')
    num3_ntr.grid(row = 1, column = 6, padx = 5, pady = 7)
    num4_ntr = Entry(window, textvariable = gnrtd4, relief = 'groove', width = 5, bd = 4, text = "", fg= 'black', bg = 'orange')
    num4_ntr.grid(row = 1, column = 7, padx = 5, pady = 7)
    num5_ntr = Entry(window, textvariable = gnrtd5, relief = 'groove', width = 5, bd = 4, text = "", fg = 'black', bg = 'white')
    num5_ntr.grid(row = 1, column = 8, padx = 5, pady = 7)
    bonusNum_ntr = Entry(window, textvariable = gnrtd_bonus, relief = 'groove', width = 5, bd = 4, text = "", fg = 'black', bg = '#238652')
    bonusNum_ntr.grid(row = 1, column = 10, padx = 5, pady = 7)

class lbls:
    #Creating the Labels for Winning Numbers
    num1 = Label(window, relief = 'groove', width = 5, bd = 4, text = "0", fg = 'black', bg = 'cyan')
    num1.grid(row = 4, column = 4, padx = 5, pady = 7)
    num2 = Label(window, relief = 'groove', width = 5, bd = 4, text = "0", fg = 'black', bg = 'yellow')
    num2.grid(row = 4, column = 5, padx = 5, pady = 7)
    num3 = Label(window, relief = 'groove', width = 5, bd = 4, text = "0", fg = 'black', bg = 'red')
    num3.grid(row = 4, column = 6, padx = 5, pady = 7)
    num4 = Label(window, relief = 'groove', width = 5, bd = 4, text = "0", fg = 'black', bg = 'orange')
    num4.grid(row = 4, column = 7, padx = 5, pady = 7)
    num5 = Label(window, relief = 'groove', width = 5, bd = 4, text = "0", fg = 'black', bg = 'white')
    num5.grid(row = 4, column = 8, padx = 5, pady = 7)
    bonus_num = Label(window, relief = 'groove', width = 5, bd = 4, text = "0", fg = 'black', bg = '#238652')
    bonus_num.grid(row = 4, column = 10, padx = 5, pady = 7)

def winningNumbs():
        lbls.num1.configure(text = str(random.sample(range(1, 49), 1)))
        lbls.num2.configure(text = str(random.sample(range(1, 49), 1)))
        lbls.num3.configure(text = str(random.sample(range(1, 49), 1)))
        lbls.num4.configure(text = str(random.sample(range(1, 49), 1)))
        lbls.num5.configure(text = str(random.sample(range(1, 49), 1)))
        lbls.bonus_num.configure(text = str(random.sample(range(1, 49), 1)))

def do_over():
    gnrtd1.delete(0,END)
    gnrtd2.delete(0,END)
    gnrtd3.delete(0,END)
    gnrtd4.delete(0,END)
    gnrtd5.delete(0,END)
    gnrtd_bonus.delete(0, END)
    num1.configure(text = str(0))
    num2.configure(text = str(0))
    num3.configure(text = str(0))
    num4.configure(text = str(0))
    num5.configure(text = str(0))
    bonus_num.configure(text = str(0))

#Button to Close the App
closeApp = Button(window)
closeApp.configure(text = "CLOSE", fg = 'black', bg = '#ff0000')
closeApp.grid(row = 7, column = 1, columnspan = 6, pady = 7)

#See Winning Numbers
see_numbers = Button(window, width=20, text="See Numbers", command=winningNumbs)
see_numbers.configure(fg = "black" ,bg = "Green")
see_numbers.grid(row = 6, column = 1, padx = 5, pady = 7)

#See Prize Won
prize = Button(window, width=20, text="Check Prize", command=check_prize)
prize.configure(fg = "black" ,bg = "Green")
prize.grid(row = 6, column = 3, padx = 5, pady = 7)

#Reset and Play Again
reset = Button(window, width=10, text="Play Again", command =do_over)
reset.configure(fg = "black" ,bg = "Green")
reset.grid(row = 6, column = 2, padx = 5, pady = 7)

#Defining a Function to Close the App
def close():
    quit()



#Attaching the "close" Function to the "close" Button
closeApp.configure(command = close)

#This is the Line That Runs the Program Until You Exit
window.mainloop()