from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
import mysql.connector
from PIL import ImageTk,Image
root=Tk()
root.title("Draft")

#img=ImageTk.PhotoImage(Image.open("C:/Users/Ritunjay Rao/Downloads/Blue and Red Ball Icon Basketball Logo.png"))
#root.iconphoto(img)
db=mysql.connector.connect(host='localhost',
                                         database='user',
                                         user='root',
                           password='mysqlpswrd4321')
mycur=db.cursor()


im1=ImageTk.PhotoImage(Image.open("C:/Users/Ritunjay Rao/Downloads/lillada01.png"))
im2=ImageTk.PhotoImage(Image.open("C:/Users/Ritunjay Rao/Downloads/foxde01.png"))
im3=ImageTk.PhotoImage(Image.open("C:/Users/Ritunjay Rao/Downloads/tatumja01.png"))
im4=ImageTk.PhotoImage(Image.open("C:/Users/Ritunjay Rao/Downloads/loveke01.png"))
im5=ImageTk.PhotoImage(Image.open("C:/Users/Ritunjay Rao/Downloads/westbru01.png"))
im6=ImageTk.PhotoImage(Image.open("C:/Users/Ritunjay Rao/Downloads/bookede01.png"))
im7=ImageTk.PhotoImage(Image.open("C:/Users/Ritunjay Rao/Downloads/isaacjo01.png"))

l3=[im1,im2,im3,im4,im5,im6,im7]
#r=IntVar
sql="select * from players"
mycur.execute(sql)
result=mycur.fetchall()
l=list(result)
l4=[]
for i in range(len(l)):
    l4.append("\'{}\'".format(l[i][1]))


l5=l4[:7]
list=[]
def clicked(value):

    sql2="select * from myteam"
    mycur.execute(sql2)
    res=mycur.fetchall()
    for i in res:
        list.append(i[1])

    try:



        sql="insert into myteam(select * from players where Name like {})".format(value)

        mycur.execute(sql)
        db.commit()
        messagebox.showinfo("new team member","{} is now in your team".format(value))
    except:
        messagebox.showerror("error","{} is already in your team".format(value))


    #mylabel=Label(root,text=value)
    #mylabel.grid(row=4,column=4)





r=StringVar()
bn=-1
l2=[]
for i in range(0,7):
    for j in range(0,7):
        bn+=1
        l2.append(Radiobutton(root,variable=r,value=l5[i],command=lambda : clicked(r.get()),image=l3[i]))
        l2[bn].grid(row=0,column=i)

#mylabel=Label(root,text=r.get())
#mylabel.grid(row=4,column=4)
#Radiobutton(root,text="hello", variable=r,value=1).pack()

#dl=PhotoImage(file="C:/Users/Ritunjay Rao/Downloads/lillada01.png")
#l=dl.subsample(4,4)
#tn3=Button(root,text="click me",image=Dl,command=disable,compound=LEFT).grid(row=0,column=3)

#ypic3=PhotoImage(file="C:/Users/Ritunjay Rao/Downloads/foxde01.png")
#ypic4=mypic3.subsample(4,4)
#btn2=Button(root,text="click me",image=mypic4,command=quit,compound=LEFT).grid(row=0,column=1)
messagebox.showinfo("selectplayer","click on a player to select in the team")



root.mainloop()