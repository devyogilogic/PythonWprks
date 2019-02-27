import tkinter as tk
import  tkinter.messagebox
import time

import mysql
import mysql.connector as myc
myobj=myc.connect(user="root",password="",database="guidb")
cusrorobj=myobj.cursor()
window=tk.Tk()
start_time = ''
loginid=tk.StringVar()

loginpass=tk.StringVar()
def logintime():

    sec = '%.f' % (time.time() - start_time)

    sec = int(sec)
    a = time.strftime('%H:%M:%S', time.gmtime(sec))

    tkinter.messagebox.showinfo("Time", a)
    arg = (str(a),loginid.get(), loginpass.get())
    cusrorobj.execute("update users set time=%s where  userid=%s and password= %s", arg)
    cusrorobj.execute("commit")
    print(a)
    exit()

def newwindow():
     global start_time
     start_time = time.time()
     window2 = tk.Tk()
     tk.Button(window2, text="log out", command=logintime).pack()
def inserttoddb():
    try:
        arg=(loginid.get(),loginpass.get())
        print(arg)
        cusrorobj.execute("insert into  users(userid,password)values (%s,%s)",arg)
        cusrorobj.execute("commit")
        tkinter.messagebox.showinfo("Info", "User added successfully")

    except myc.errors.IntegrityError:
        tkinter.messagebox.showinfo("Info", "User already exsits")


def logincheck():
    try:

        arg = (loginid.get(), loginpass.get())
        print(arg)
        cusrorobj.execute("select * from users where userid=%s and password=%s", arg)
        for i in cusrorobj:
            li=[]
            li.append(i)
            print(len(tuple(li[0])))

        a=len(tuple(li[0]))
        if(a==4):
            start_time = time.time()
            newwindow()
    except UnboundLocalError :
        tkinter.messagebox.showinfo("Info", "Wrong Crendials")




tk.Label(window,text="Enter your id").grid(row=0,column=3)
tk.Entry(window,textvariable=loginid,bd=5).grid(row=0,column=5)
tk.Label(window,text="Enter your password").grid(row=1,column=3)
tk.Entry(window,textvariable=loginpass,bd=5).grid(row=1,column=5)
tk.Button(window,text="Signup",command=lambda:inserttoddb()).grid(row=3,column=4)
tk.Button(window,text="Login" ,command=lambda :logincheck()).grid(row=5,column=4)

window.mainloop()







