from tkinter import*
from tkinter import messagebox,simpledialog

import schedule
import time

root = Tk()


password_result=0

def quit1():
    label2=Label(root,text="2")
    label2.place(x=20,y=50)
    root.destroy()

def passwi():
    password_result=simpledialog.askstring('Password',"Enter ur L password")
    label1=Label(root,text=password_result)
    label1.place(x=10,y=50)
password_button = Button(root,text='Enter the password',command=passwi)

password_button.pack()


def shoroo_va_payan():
    def provide_password():
       user_result=simpledialog.askstring("title",'enter ur password')
       if user_result == password_result:
            quit1()
       else:
            label3=Label(root,text=user_result)
            label3.place(x=20,y=60)
            
            
            

    global root
    root.geometry('300x300')
    root.overrideredirect(True)#قفل کردن صفحه

    quit_button = Button(root,text='quit',command=provide_password)
    quit_button.pack()
    root.mainloop()


def block_off():
    global root
    root.overrideredirect(False)#باز کردن

schedule.every().day.at("20:45").do(shoroo_va_payan())
schedule.every().day.at("20:46").do(block_off())


while True:
   schedule.run_pending()
   time.sleep(1)
