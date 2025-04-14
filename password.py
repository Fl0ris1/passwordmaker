from tkinter import *
from clear_screen import clear
from tkinter.font import Font
from pswd_maker import passwordmaker

clear()
def show():
    clear()
    passw=passwordmaker()
    password_lbl.config(text=f"     PASSWORD:    {passw}")
    print(f"PASSWORD: {passw}")

root=Tk()

font1=Font(family="consolas",weight="bold")
root.geometry("500x250")
root.config(background="#7FC6A4")
root.title("Password Generator")

head_lbl=Label(root,text="PASSWORD GENERATOR",font=(font1,13),fg="#454B66",bg="#7FC6A4")
head_lbl.place(x=0,y=0)

gen_button=Button(root,text="GENERATE!",font=(font1,13),fg="#454B66",bg="#88A09E",command=show)
gen_button.place(x=200,y=150)

password_lbl=Label(root,text="Press The Button To Generate A Password",font=(font1,13),fg="#454B66",bg="#7FC6A4")
password_lbl.place(x=100,y=80)

root.mainloop()