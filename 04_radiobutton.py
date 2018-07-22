import tkinter as tk

window = tk.Tk()
window.title('forth window')
window.geometry('200x200')

var = tk.StringVar()
l = tk.Label(window,bg="yellow",width=15,text='empty')
l.pack()

def print_selection():
    l.config(text='you have select:'+var.get())

tk.Radiobutton(window,text='OptionA',variable=var,
               value='A',command=print_selection).pack()
tk.Radiobutton(window,text='OptionB',variable=var,
               value='B',command=print_selection).pack()
tk.Radiobutton(window,text='OptionC',variable=var,
               value='C',command=print_selection).pack()

window.mainloop()
