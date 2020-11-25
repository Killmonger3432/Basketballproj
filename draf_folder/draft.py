import mysql.connector
from tkinter import *
root=Tk()
root.title('select employees')
root.geometry("300x300")
db=mysql.connector.connect(host='localhost',
                                         database='user',
                                         user='root',
                           password='mysqlpswrd4321')

cur=db.cursor()
def select():
    selectlabel.config(text=mylistbox.get(ANCHOR)+" is in your team")
def selectall():
    res=''
    for i in mylistbox.curselection():
        res+=mylistbox.get(i)+"\n"
    selectlabel.config(text=res)

def delete():
    mylistbox.delete(ANCHOR)
cursor=db.cursor()
scrollbar = Scrollbar(root)
scrollbar.pack( side = RIGHT, fill = Y)
def disable():
    if disable["state"] == "normal":
        disable["state"] = "disabled"
def addteam():
    l=[]
    for i in mylistbox.curselection():
        x=mylistbox.get(i)

        if x not in l:
            l.append(x)
        if len(l)>=5:
            if addteam["state"] == "normal":
                addteam["state"] = "disabled"
        if len(l)==5:
            print(l)
            for i in l:
                sql="select * from players where Name = \'{}\'".format(i)
                print(sql)














    


mylistbox=Listbox(root, selectmode=MULTIPLE)
mylistbox.pack(pady=10)
sql="select * from players"
cursor.execute(sql)
result=cursor.fetchall()
for i in result:
    mylistbox.insert(END,i[1])
scrollbar.config(command=mylistbox.yview)
#deletebtn=Button(root,text="delete",command=delete)
#deletebtn.pack(pady=10)
#selectbtn=Button(root,text="select players for your team",command=select)
#selectbtn.pack(pady=10)
selectlabel=Label(root,text='')
selectlabel.pack(pady=5)
selectall=Button(root,text='select all',command=selectall)
selectall.pack(pady=10)
delete_all=Button(root,text='delete all')
delete_all.pack(pady=10)
disable=Button(root,text='disable',command=disable)
disable.pack(pady=10)
addteam=Button(root,text='add to team',command=addteam)
addteam.pack(pady=10)



root.mainloop()