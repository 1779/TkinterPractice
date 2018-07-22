import tkinter as tk
import pickle
from tkinter import messagebox
from PIL import Image

im = Image.open('welcome.jpg')
im.save('welcome2.gif')

window = tk.Tk()
window.title('place')
window.geometry('600x400')


# welcom image
canvas = tk.Canvas(window,height=200,width=600)
image_file = tk.PhotoImage(file='welcome2.gif')
image = canvas.create_image(0,0,anchor='nw',image=image_file)
canvas.pack(side='top')

# user information
tk.Label(window,text='User name:').place(x=150,y=250)
tk.Label(window,text=' Password:').place(x=150,y=290)

var_usr_name = tk.StringVar()
var_usr_name.set('example@python.com')
var_usr_pwd = tk.StringVar()
entry_usr_name = tk.Entry(window,textvariable=var_usr_name)
entry_usr_name.place(x=250,y=250)
entry_usr_pwd = tk.Entry(window,textvariable=var_usr_pwd,show='*')
entry_usr_pwd.place(x=250,y=290)

# login and sign up button
def usr_login():
    usr_name = var_usr_name.get()
    usr_pwd = var_usr_pwd.get()
    try:
        with open('usrs_info.pickle','rb') as usrs_file:
            usrs_info = pickle.load(usrs_file)
    except FileNotFoundError:
        with open('usrs_info.pickle','wb') as usr_file:
            usrs_info = {'admin':'admin'}
            pickle.dump(usrs_info,usrs_file)
    if usr_name in usrs_info:
        if usr_pwd == usrs_info[usr_name]:
            tk.messagebox.showinfo(message='Welcome '+usr_name)
        else:
            tk.messagebox.showerror(message='Error,your passward is wrong')
    else:
        is_sign_up = tk.messagebox.askyesno(message='You have not signed up yet,sign up?')
        if is_sign_up:
            usr_sign_up()

        
def usr_sign_up():
    def sign_to():
        np = new_pwd.get()
        npf = new_pwd_confirm.get()
        nn = new_name.get()
        with open('usrs_info.pickle','rb') as usr_file:
            exist_usr_info = pickle.load(usr_file)
        if np != npf:
            tk.messagebox.showerror('Error','Passward and the confirm passward must be the same!')
        elif nn in exist_usr_info:
            tk.messagebox.showerror('Error','This user has been already signed up')
        else:
            exist_usr_info[nn] = np
            with open('usrs_info.pickle','wb') as usr_file:
                pickle.dump(exist_usr_info,usr_file)
            tk.messagebox.showinfo(message='Wlcome you have successfully signed up!')
            window_sign_up.destroy()
            
    window_sign_up = tk.Toplevel(window)
    window_sign_up.geometry('350x200')
    window_sign_up.title('sign up')

    new_name = tk.StringVar()
    new_name.set('example@python.com')
    tk.Label(window_sign_up,text='User name').place(x=10,y=10)
    entry_new_name = tk.Entry(window_sign_up,textvariable=new_name)
    entry_new_name.place(x=150,y=10)

    new_pwd = tk.StringVar()
    tk.Label(window_sign_up,text='Passward:').place(x=10,y=50)
    entry_usr_pwd = tk.Entry(window_sign_up,textvariable=new_pwd,show='*')
    entry_usr_pwd.place(x=150,y=50)

    new_pwd_confirm = tk.StringVar()
    tk.Label(window_sign_up,text='comfirm passward:').place(x=10,y=90)
    entry_usr_pwd_confirm = tk.Entry(window_sign_up,textvariable=new_pwd_confirm,show='*')
    entry_usr_pwd_confirm.place(x=150,y=90)

    btn_confirm_sign_up = tk.Button(window_sign_up,text='Sign up',command=sign_to)
    btn_confirm_sign_up.place(x=150,y=130)

# login and sign up button
btn_login = tk.Button(window,text= 'Login',command=usr_login)
btn_login.place(x=250,y=320)
btn_sign_up = tk.Button(window,text= 'Sign up',command=usr_sign_up)
btn_sign_up.place(x=330,y=320)

window.mainloop()
