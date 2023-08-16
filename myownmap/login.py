import webbrowser
from tkinter import *
import pymysql


def hide():
    openeye.config(file='CE.png')
    passwordEntry.config(show='*')
    eyeButton.config(command=show)

def show():
    openeye.config(file='OE.png')
    passwordEntry.config(show='')
    eyeButton.config(command=hide)




def user_enter(event):
    if usernameEntry.get()=='Username':
        usernameEntry.delete(0,END)

def password_enter(event):
    if passwordEntry.get() == 'Password':
        passwordEntry.delete(0, END)

def reset_password():
    login_window.destroy()
    import password

def create_account():
    login_window.destroy()
    import account

login_window=Tk()
login_window.title('Login')
login_window.geometry('990x660+50+50')
login_window.resizable(0,0)
bgImage=PhotoImage(file='login.png')

bgLabel=Label(login_window,image=bgImage)
bgLabel.place(x=0,y=0)

heading=Label(login_window,text='LOGIN',font=('Microsoft Yahei Ui Light',25,'bold'),bg='white',fg='firebrick1')
heading.place(x=660,y=80)

usernameEntry=Entry(login_window,width=25,font=('Microsoft Yahei Ui Light',15,'bold'),bd='0',fg='firebrick1')
usernameEntry.place(x=580,y=200)
usernameEntry.insert(0,'Username')

usernameEntry.bind('<FocusIn>',user_enter)

frame1=Frame(login_window,width=250,height=2,bg='firebrick1')
frame1.place(x=580,y=226)

passwordEntry=Entry(login_window,width=25,font=('Microsoft Yahei Ui Light',15,'bold'),bd='0',fg='firebrick1')
passwordEntry.place(x=580,y=260)
passwordEntry.insert(0,'Password')

passwordEntry.bind('<FocusIn>',password_enter)

frame2=Frame(login_window,width=250,height=2,bg='firebrick1')
frame2.place(x=580,y=286)
openeye=PhotoImage(file='OE.png')
eyeButton=Button(login_window,image=openeye,bd=0,bg='white',activebackground='white',cursor='hand2',command=hide)
eyeButton.place(x=800,y=250)

forgetButton=Button(login_window,text='Forgot Password?',bd=0,bg='white',activebackground='white',cursor='hand2',font=('Microsoft Yahei Ui Light',9,'bold'),
                    fg='firebrick1',activeforeground='firebrick1',command=reset_password)
forgetButton.place(x=715,y=300)
def open_browser():
    webbrowser.open_new("framerohan.html")
loginButton=Button(login_window,text='Login',bd=0,bg='firebrick1',activebackground='firebrick1',cursor='hand2',font=('Open Sans',16,'bold'),
                   fg='white',activeforeground='white',width=19,command=open_browser)
loginButton.place(x=578,y=400)

signupLabel=Label(login_window,text="Don't have an account?",font=('Open Sans',11,'bold'),fg='firebrick1',bg='white' )
signupLabel.place(x=550,y=500)

newaccountButton=Button(login_window,text='Create new account',bd=0,bg='white',activebackground='white',cursor='hand2',font=('Open Sans',9,'bold underline'),
                   fg='blue',activeforeground='blue',command=create_account)
newaccountButton.place(x=727,y=500)


login_window.mainloop()