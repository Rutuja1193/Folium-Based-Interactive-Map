from tkinter import *
from tkinter import messagebox
import pymysql
import _mysql_connector
import mysql.connector
connection = mysql.connector.connect(host='127.0.0.1', user='root', password='123456', database='user_data')
c = connection.cursor()

def insertData():

    email = emailEntry.get()
    username = usernameEntry.get()
    password = passwordEntry.get()

    insert_query = "INSERT INTO `login`( `email`, `username`, `password`) VALUES (%s,%s,%s)"
    vals = (email,username,password)
    c.execute(insert_query,vals)
    connection.commit()
    messagebox.showinfo('Success', 'Successfully Inserted')



def login_page():
    account_window.destroy()
    import login

def signup_page():
    account_window.destroy()
    import login




account_window=Tk()
account_window.title('Create account')
account_window.geometry('990x660+50+50')
account_window.resizable(False,False)
bgImage=PhotoImage(file='account.png')

bgLabel=Label(account_window,image=bgImage)
bgLabel.grid()



frame=Frame(account_window)
frame.place(x=510,y=90)



heading=Label(frame,text='CREATE ACCOUNT',font=('Microsoft Yahei Ui Light',25,'bold'),bg='white',fg='firebrick1')
heading.grid(row=0,column=0)

emailLabel=Label(frame,text='Email',font=('Microsoft Yahei Ui Light',15,'bold'),bg='white',fg='firebrick1')
emailLabel.grid(row=1,column=0,sticky='w',padx=25,pady=(10,0))

emailEntry=Entry(frame,width=30,font=('Microsoft Yahei Ui Light',15,'bold'),fg='white',bg='firebrick1')
emailEntry.grid(row=2,column=0,sticky='w',padx=25)

usernameLabel=Label(frame,text='Username',font=('Microsoft Yahei Ui Light',15,'bold'),bg='white',fg='firebrick1')
usernameLabel.grid(row=3,column=0,sticky='w',padx=25,pady=(10.0))

usernameEntry=Entry(frame,width=30,font=('Microsoft Yahei Ui Light',15,'bold'),fg='white',bg='firebrick1')
usernameEntry.grid(row=4,column=0,sticky='w',padx=25)

passwordLabel=Label(frame,text='Password',font=('Microsoft Yahei Ui Light',15,'bold'),bg='white',fg='firebrick1')
passwordLabel.grid(row=5,column=0,sticky='w',padx=25,pady=(10,0))

passwordEntry=Entry(frame,width=30,font=('Microsoft Yahei Ui Light',15,'bold'),fg='white',bg='firebrick1')
passwordEntry.grid(row=6,column=0,sticky='w',padx=25)

confirmpasswordLabel=Label(frame,text='Confirm Password',font=('Microsoft Yahei Ui Light',15,'bold'),bg='white',fg='firebrick1')
confirmpasswordLabel.grid(row=7,column=0,sticky='w',padx=25,pady=(10,0))

confirmpasswordEntry=Entry(frame,width=30,font=('Microsoft Yahei Ui Light',15,'bold'),fg='white',bg='firebrick1')
confirmpasswordEntry.grid(row=8,column=0,sticky='w',padx=25)

freeLabel=Label(frame)
freeLabel.grid(row=9,column=0,sticky='w',padx=25,pady=(10,0))

signupButton=Button(frame, text='Sign up', font=('Open Sans',15,'bold'), bd=0, fg='white', bg='firebrick1', activeforeground='white'
                    , activebackground='firebrick1', width=17, command=insertData)
signupButton.grid(row=10,column=0,padx=10)


signupLabel=Label(frame,text='Have an account?',font=('Open Sans',11,'bold'),fg='firebrick1',bg='white' )
signupLabel.grid(row=11,column=0,sticky='w',padx=25,pady=10)

loginButton=Button(frame,text='Login',bd=0,bg='white',activebackground='white',cursor='hand2',font=('Open Sans',11,'bold underline'),
                   fg='blue',activeforeground='blue',command=login_page)
loginButton.place(x=170,y=430)





account_window.mainloop()
