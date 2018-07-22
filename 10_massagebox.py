import tkinter as tk
from tkinter import messagebox
import time

window = tk.Tk()
window.title('message')
window.geometry('200x200')

time_now = time.ctime()


def hitting():
    # tk.messagebox.showinfo(title='Hi',message=time_now)
    # tk.messagebox.showwarning(title='Hi',message=time_now)
    # tk.messagebox.showerror(title='Hi',message=time_now)
    # print(tk.messagebox.askquestion(title='Hi',message=time_now))
                    # return yes | no
    
    tk.messagebox.askyesno(title='Hi',message=time_now)
                    # return Ture | False
    ### tk.messagebox.asktrycancel(title='Hi',message=time_now)
                    # return True | false
    tk.messagebox.askokcancel(title='Hi',message=time_now)
                    # return True | False
    
tk.Button(window,text='hit',command=hitting).pack()


window.mainloop()
