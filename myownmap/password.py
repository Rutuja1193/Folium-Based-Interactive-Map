from tkinter import *

def login_page():
    password_window.destroy()
    import login



password_window=Tk()
password_window.title('reset password')
password_window.geometry('990x660+50+50')
password_window.resizable(False,False)
bgImage=PhotoImage(file='password.png')

bgLabel=Label(password_window,image=bgImage)
bgLabel.grid()


frame=Frame(password_window)
frame.place(x=520,y=130)

heading=Label(frame,text='RESET PASSWORD',font=('Microsoft Yahei Ui Light',25,'bold'),bg='white',fg='firebrick1')
heading.grid(row=0,column=0)

usernameLabel=Label(frame,text='Username',font=('Microsoft Yahei Ui Light',15,'bold'),bg='white',fg='firebrick1')
usernameLabel.grid(row=1,column=0,sticky='w',padx=25,pady=(10,0))

usernameEntry=Entry(frame,width=30,font=('Microsoft Yahei Ui Light',15,'bold'),fg='white',bg='firebrick1')
usernameEntry.grid(row=2,column=0,sticky='w',padx=25)


newLabel=Label(frame,text='New Password',font=('Microsoft Yahei Ui Light',15,'bold'),bg='white',fg='firebrick1')
newLabel.grid(row=3,column=0,sticky='w',padx=25,pady=(10,0))

newEntry=Entry(frame,width=30,font=('Microsoft Yahei Ui Light',15,'bold'),fg='white',bg='firebrick1')
newEntry.grid(row=4,column=0,sticky='w',padx=25)

confirmLabel=Label(frame,text='Confirm Password',font=('Microsoft Yahei Ui Light',15,'bold'),bg='white',fg='firebrick1')
confirmLabel.grid(row=5,column=0,sticky='w',padx=25,pady=(10,0))

confirmEntry=Entry(frame,width=30,font=('Microsoft Yahei Ui Light',15,'bold'),fg='white',bg='firebrick1')
confirmEntry.grid(row=6,column=0,sticky='w',padx=25)

freeLabel=Label(frame)
freeLabel.grid(row=7,column=0,sticky='w',padx=25,pady=(10,0))

freeLabel=Label(frame)
freeLabel.grid(row=8,column=0,sticky='w',padx=25,pady=(10,0))


submitButton=Button(frame,text='Submit',font=('Open Sans',15,'bold'),bd=0,fg='white',bg='firebrick1',activeforeground='white'
                    ,activebackground='firebrick1',width=17,command=login_page)
submitButton.grid(row=9,column=0,padx=10)



password_window.mainloop()
