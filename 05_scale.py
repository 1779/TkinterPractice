import tkinter as tk

window = tk.Tk()
window.title('fifth window')
window.geometry('200x200')

l = tk.Label(window,bg='yellow',width=20,text='')
l.pack()

def print_selection(v):
    l.config(text='you are on:'+v)


s = tk.Scale(window,label='try',from_=5,to=11,orient=tk.HORIZONTAL,
             length=200,showvalue=0,tickinterval=3,resolution=0.01,
             command=print_selection)
s.pack()

window.mainloop()
