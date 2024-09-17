from tkinter import *
from tkinter import messagebox
import base64
import os

def decrypt():
    password=code.get()

    if password=="1234":
       screen2=Toplevel(screen)
       screen2.title("Decryption")
       screen2.geometry("200x200")
       screen2.configure(bg="#00bd56")

       message=text1.get(1.0, END)
       encode_message=message.encode("ascii")
       base64_bytes=base64.b64decode(encode_message)
       encrypt=base64_bytes.decode("ascii")

       Label(screen2, text="ENCRYPTED MESSAGE", font="arial", fg="white", bg="#00bd56").place(x=20, y=0)
       text2=Text(screen2,font="arial", bg="white", relief=GROOVE, wrap=WORD, bd=0)
       text2.place(x=10, y=40, width=180, height=150)

       text2.insert(END, encrypt)

    elif password=="":
       messagebox.showerror("encryption","Input Password")
       
    elif password !="1234":
       messagebox.showerror("encryption","Invalid Password")




def encrypt():
    password=code.get()

    if password=="1234":
       screen1=Toplevel(screen)
       screen1.title("Encryption")
       screen1.geometry("200x200")
       screen1.configure(bg="#00bd56")

       message=text1.get(1.0, END)
       encode_message=message.encode("ascii")
       base64_bytes=base64.b64encode(encode_message)
       encrypt=base64_bytes.decode("ascii")

       Label(screen1, text="ENCRYPTED MESSAGE", font="arial", fg="white", bg="#00bd56").place(x=20, y=0)
       text2=Text(screen1,font="arial", bg="white", relief=GROOVE, wrap=WORD, bd=0)
       text2.place(x=10, y=40, width=180, height=150)

       text2.insert(END, encrypt)

    elif password=="":
       messagebox.showerror("encryption","Input Password")
       
    elif password !="1234":
       messagebox.showerror("encryption","Invalid Password")
    


def main_screen():

    global screen   
    global code
    global text1


    screen = Tk()
    screen.geometry("375x398")

    # icon
    # image_icon=PhotoImage(file="keys.png")
    # screen.iconphoto(False, image_icon)
    # use this to add image icon
    
    def reset():
        code.set("")
        text1.delete(1.0, END)

    screen.title("Message Encryption App")

    Label(text="Enter text to encrypt and decrypt", fg="black", font=("Calibri", 13)).place(x=10, y=10)
    text1 = Text(font=("Roboto", 20), bg="white", relief=GROOVE, wrap=WORD, bd=0)
    text1.place(x=10, y=50, height=100, width=355)

    Label(text="Enter secret key for encryption", fg="black", font=("Calibri", 13)).place(x=10, y=170)

    code=StringVar()
    Entry(textvariable=code, width=19, bd=0, font=("Calibri", 25),show="*").place(x=10, y=190)

    Button(text="Encrypt", height="2", width="23", bg="#ed3833", fg="white", bd=0, command=encrypt).place(x=10, y=250)
    Button(text="Decrypt", height="2", width="23", bg="#00bd56", fg="white", bd=0, command=decrypt).place(x=200, y=250)
    Button(text="Reset", height="2", width="50", bg="#99CC32", fg="white", bd=0, command=reset).place(x=10, y=300)

    screen.mainloop()

main_screen()