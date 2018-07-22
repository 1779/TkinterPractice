import tkinter as tk

window = tk.Tk()
window.title('fifth window')
window.geometry('200x200')

l = tk.Label(window,bg='yellow',width=20,text='')
l.pack()

def print_selection():
    if (var1.get()==1)&(var2.get()==0):
        l.config(text='I love only boys!')
    elif (var1.get()==0)&(var2.get()==1):
        l.config(text='I love only girls!')
    elif (var1.get()==0)&(var2.get()==0):
        l.config(text='I don`t love either!')
    else:
        l.config(text='I love Both!!')

var1 = tk.IntVar()
var2 = tk.IntVar()
##对val1进行赋值，如果选择了为1，否则为0
c1 = tk.Checkbutton(window,text='Boys ',variable=var1,
                    onvalue=1,offvalue=0,command=print_selection)
c1.pack()
c2 = tk.Checkbutton(window,text='Girls',variable=var2,
                    onvalue=1,offvalue=0,command=print_selection)
c2.pack()

window.mainloop()
