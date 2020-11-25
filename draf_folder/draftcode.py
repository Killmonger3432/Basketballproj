from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
import mysql.connector
from PIL import ImageTk,Image
root=Tk()
root.title("Draft")
#root.geometry("400x400")

width=400
height=400
im = ImageTk.PhotoImage(Image.open("C:/Users/Ritunjay Rao/Downloads/bballcourt.png"))
img = Image.open("C:/Users/Ritunjay Rao/Downloads/bballcourt.png")
img = img.resize((width,height), Image.ANTIALIAS)
Img =  ImageTk.PhotoImage(img)

labelframe1 = LabelFrame(root, text="pick a position")
labelframe1.pack(padx=10,pady=10,fill="both", expand="yes")
l=Label(labelframe1,image=Img).place(x=0,y=0)


#img=ImageTk.PhotoImage(Image.open("C:/Users/Ritunjay Rao/Downloads/Blue and Red Ball Icon Basketball Logo.png"))
#root.iconphoto(img)
db=mysql.connector.connect(host='localhost',
                                         database='user',
                                         user='root',
                           password='mysqlpswrd4321')
mycur=db.cursor()

new = Toplevel(root)
im1 = ImageTk.PhotoImage(Image.open("C:/Users/Ritunjay Rao/Downloads/curry.png"))
im2 = ImageTk.PhotoImage(Image.open("C:/Users/Ritunjay Rao/Downloads/westbrook.png"))
im3 = ImageTk.PhotoImage(Image.open("C:/Users/Ritunjay Rao/Downloads/kyr.png"))
im4 = ImageTk.PhotoImage(Image.open("C:/Users/Ritunjay Rao/Downloads/lillard.png"))
im5 = ImageTk.PhotoImage(Image.open("C:/Users/Ritunjay Rao/Downloads/chrispaul.png"))
im6 = ImageTk.PhotoImage(Image.open("C:/Users/Ritunjay Rao/Downloads/kembawalker.png"))
im7 = ImageTk.PhotoImage(Image.open("C:/Users/Ritunjay Rao/Downloads/trae.png"))
im8 = ImageTk.PhotoImage(Image.open("C:/Users/Ritunjay Rao/Downloads/bensimmons.png"))
im9 = ImageTk.PhotoImage(Image.open("C:/Users/Ritunjay Rao/Downloads/deaaronfox.png"))
im10 = ImageTk.PhotoImage(Image.open("C:/Users/Ritunjay Rao/Downloads/kylelowry.png"))
im11 = ImageTk.PhotoImage(Image.open("C:/Users/Ritunjay Rao/Downloads/jamorant.png"))

x=im1.height()
y=im1.width()
l3 = [im1, im2, im3, im4, im5, im6, im7, im8, im9, im10, im11]
i1 = ImageTk.PhotoImage(Image.open("C:/Users/Ritunjay Rao/Downloads/joelembid.png"))
i2 = ImageTk.PhotoImage(Image.open("C:/Users/Ritunjay Rao/Downloads/nikolajokic.png"))
i3 = ImageTk.PhotoImage(Image.open("C:/Users/Ritunjay Rao/Downloads/karlanthonytowns.png"))
i4 = ImageTk.PhotoImage(Image.open("C:/Users/Ritunjay Rao/Downloads/rudygobert.png"))
i5 = ImageTk.PhotoImage(Image.open("C:/Users/Ritunjay Rao/Downloads/hassanwhiteside.png"))
i6 = ImageTk.PhotoImage(Image.open("C:/Users/Ritunjay Rao/Downloads/kristapsporzingis.png"))
i7 = ImageTk.PhotoImage(Image.open("C:/Users/Ritunjay Rao/Downloads/bamadabeyo.png"))
i8 = ImageTk.PhotoImage(Image.open("C:/Users/Ritunjay Rao/Downloads/clintcapela.png"))
centerlist=[i1,i2,i3,i4,i5,i6,i7,i8]
sql = "select * from c order by Overall desc"
mycur.execute(sql)
result = mycur.fetchall()
l = list(result)
l4 = []
for i in range(len(l)):
    l4.append("\'{}\'".format(l[i][1]))

listc = l4[:8]
nlist=[]

#i9 = ImageTk.PhotoImage(Image.open("C:/Users/Ritunjay Rao/Downloads/deaaronfox.png"))
# r=IntVar
a1 = ImageTk.PhotoImage(Image.open('C:/Users/Ritunjay Rao/Downloads/jamesharden.png'))
a2 = ImageTk.PhotoImage(Image.open("C:/Users/Ritunjay Rao/Downloads/lukadoncic.png"))
a3 = ImageTk.PhotoImage(Image.open("C:/Users/Ritunjay Rao/Downloads/paulgeorge.png"))
a4 = ImageTk.PhotoImage(Image.open("C:/Users/Ritunjay Rao/Downloads/klaythompson.png"))
a5 = ImageTk.PhotoImage(Image.open("C:/Users/Ritunjay Rao/Downloads/bradleybeal.png"))
a6 = ImageTk.PhotoImage(Image.open("C:/Users/Ritunjay Rao/Downloads/devinbooker.png"))
a7 = ImageTk.PhotoImage(Image.open("C:/Users/Ritunjay Rao/Downloads/cjmcollum.png"))
a8 = ImageTk.PhotoImage(Image.open("C:/Users/Ritunjay Rao/Downloads/donovanmitchell.png"))
sglist=[a1,a2,a3,a4,a5,a6,a7,a8]
sql = "select * from sg order by Overall desc"
mycur.execute(sql)
result = mycur.fetchall()
l = list(result)
l4 = []
for i in range(len(l)):
    l4.append("\'{}\'".format(l[i][1]))

listsg = l4[:8]
nlist=[]
def myteam():
    new = Toplevel(root)
    new.title("MY TEAM")
    '''
    frame_container = Frame(new)

    canvas_container = Canvas(frame_container, height=800, width=1500)
    frame2 = Frame(canvas_container)
    myscrollbar = Scrollbar(frame_container, orient="vertical",
                            command=canvas_container.yview)  # will be visible if the frame2 is to to big for the canvas
    canvas_container.create_window((0, 0), window=frame2, anchor='nw')
    '''
    sql="select * from myteam"
    mycur.execute(sql)
    res=mycur.fetchall()
    name=[]
    index=[]


    for i in range(len(res)):
        name.append("\'{}\'".format(res[i][1]))
        index.append("\"{}\"".format(res[i][9]))

    print(index, "index")
    print(name, "name")
    imgs=[]
    l2 = []
    for i in index:

        l='\"{}\"'.format(i)
        print("\"{}\"".format(i))



        imgs.append(ImageTk.PhotoImage(Image.open(i)))
    print(index)

    r=StringVar()

    for i in range(0,4):

        l2.append(Radiobutton(new,image=imgs[i]))
    l2[0].grid(row=0,column=1)

    l2[1].grid(row=0, column=5)
    l2[2].grid(row=2, column=3)
    l2[3].grid(row=4, column=1)
    #l2[4].grid(row=4, column=5)

    '''
    frame2.update()
    canvas_container.configure(yscrollcommand=myscrollbar.set, scrollregion="0 0 0 %s" % frame2.winfo_height())
    canvas_container.pack(side=RIGHT)
    myscrollbar.pack(side=RIGHT, fill=Y)

    frame_container.pack()
    '''

def sg():
    new=Toplevel(root)
    new.title("Point Guard")
    frame_container = Frame(new)

    canvas_container = Canvas(frame_container,height=800,width=1500)
    frame2 = Frame(canvas_container)
    myscrollbar = Scrollbar(frame_container, orient="vertical",command=canvas_container.yview)  # will be visible if the frame2 is to to big for the canvas
    canvas_container.create_window((0, 0), window=frame2, anchor='nw')

    def clicked(value):

        sql2="select * from myteam"
        mycur.execute(sql2)
        res=mycur.fetchall()



        try:




            sql="insert into myteam(Jersey_number,Name,Position,Overall,Shooting_Outside,Shooting_inside,Defense_outside,Defense_inside,Passing,img) select * from sg where Name like {}".format(value)

            mycur.execute(sql)
            db.commit()
            messagebox.showinfo("new team member","{} is now in your team".format(value))







        except:
            messagebox.showerror("error","You already have a shooting guard")


        #mylabel=Label(root,text=value)
        #mylabel.grid(row=4,column=4)




    new.grab_set()
    #new.grab_release()
    r=StringVar()
    bn=-1
    l2=[]
    for i in range(0,8):

        l2.append(Radiobutton(frame2,variable=r,value=listsg[i],command=lambda : clicked(r.get()),image=sglist[i]))
    l2[0].grid(row=0,column=1)
    l2[1].grid(row=0,column=3)
    l2[2].grid(row=0, column=5)
    l2[3].grid(row=1, column=2)
    l2[4].grid(row=1, column=4)
    l2[5].grid(row=1, column=6)
    l2[6].grid(row=2, column=1)
    l2[7].grid(row=2, column=3)



    frame2.update()
    canvas_container.configure(yscrollcommand=myscrollbar.set,scrollregion="0 0 0 %s" % frame2.winfo_height())
    canvas_container.pack(side=RIGHT)
    myscrollbar.pack(side=RIGHT, fill=Y)

    frame_container.pack()



pf1 = ImageTk.PhotoImage(Image.open('C:/Users/Ritunjay Rao/Downloads/gantentokuonmpo.png'))
pf2 = ImageTk.PhotoImage(Image.open("C:/Users/Ritunjay Rao/Downloads/pascalsiakam.png"))
pf3 = ImageTk.PhotoImage(Image.open("C:/Users/Ritunjay Rao/Downloads/jaysontatum.png"))
pf4 = ImageTk.PhotoImage(Image.open("C:/Users/Ritunjay Rao/Downloads/johncollins.png"))
pf5 = ImageTk.PhotoImage(Image.open("C:/Users/Ritunjay Rao/Downloads/domantassabonis.png"))
pf6 = ImageTk.PhotoImage(Image.open("C:/Users/Ritunjay Rao/Downloads/blakegriffin.png"))
pf7 = ImageTk.PhotoImage(Image.open("C:/Users/Ritunjay Rao/Downloads/danilogallinari.png"))
pf8 = ImageTk.PhotoImage(Image.open("C:/Users/Ritunjay Rao/Downloads/jarenjacksonjr.png"))
pf9 = ImageTk.PhotoImage(Image.open("C:/Users/Ritunjay Rao/Downloads/kevinlove.png"))
pf10 = ImageTk.PhotoImage(Image.open("C:/Users/Ritunjay Rao/Downloads/alhorford.png"))

pflist=[pf1,pf2,pf3,pf4,pf5,pf6,pf7,pf8,pf9,pf10]
sql = "select * from pf order by Overall desc"
mycur.execute(sql)
result = mycur.fetchall()
l = list(result)
listpf = []
for i in range(len(l)):
    listpf.append("\'{}\'".format(l[i][1]))


nlist=[]
def pf():
    new=Toplevel(root)
    new.title("Small Forward")
    frame_container = Frame(new)

    canvas_container = Canvas(frame_container,height=800,width=1500)
    frame2 = Frame(canvas_container)
    myscrollbar = Scrollbar(frame_container, orient="vertical",command=canvas_container.yview)  # will be visible if the frame2 is to to big for the canvas
    canvas_container.create_window((0, 0), window=frame2, anchor='nw')

    def clicked(value):



        try:




            sql="insert into myteam(Jersey_number,Name,Position,Overall,Shooting_Outside,Shooting_inside,Defense_outside,Defense_inside,Passing,img) select * from sf where Name like {}".format(value)


            mycur.execute(sql)
            db.commit()
            messagebox.showinfo("new team member","{} is now in your team".format(value))


        except:
            messagebox.showerror("error", "You already have a power forward")



        #mylabel=Label(root,text=value)
        #mylabel.grid(row=4,column=4)




    #new.grab_set()
    #new.grab_release()
    r=StringVar()
    bn=-1
    l2=[]
    for i in range(0,10):

        l2.append(Radiobutton(frame2,variable=r,value=listpf[i],command=lambda : clicked(r.get()),image=pflist[i]))
    l2[0].grid(row=0,column=1)
    l2[1].grid(row=0,column=3)
    l2[2].grid(row=0, column=5)
    l2[3].grid(row=1, column=2)
    l2[4].grid(row=1, column=4)
    l2[5].grid(row=1, column=6)
    l2[6].grid(row=2, column=1)
    l2[7].grid(row=2, column=3)
    l2[8].grid(row=2, column=5)
    l2[9].grid(row=3, column=2)




    frame2.update()
    canvas_container.configure(yscrollcommand=myscrollbar.set,scrollregion="0 0 0 %s" % frame2.winfo_height())
    canvas_container.pack(side=RIGHT)
    myscrollbar.pack(side=RIGHT, fill=Y)

    frame_container.pack()

def center():
    new=Toplevel(root)
    new.title("Point Guard")
    frame_container = Frame(new)

    canvas_container = Canvas(frame_container,height=800,width=1500)
    frame2 = Frame(canvas_container)
    myscrollbar = Scrollbar(frame_container, orient="vertical",command=canvas_container.yview)  # will be visible if the frame2 is to to big for the canvas
    canvas_container.create_window((0, 0), window=frame2, anchor='nw')

    def clicked(value):

        sql2="select * from myteam"
        mycur.execute(sql2)
        res=mycur.fetchall()
        count=0
        for i in res:
            if res[0][2]=="C":
                count+=1
        if res==[]:
            count=0

        try:




            sql="insert into myteam(Jersey_number,Name,Position,Overall,Shooting_Outside,Shooting_inside,Defense_outside,Defense_inside,Passing,img) select * from c where Name like {}".format(value)


            mycur.execute(sql)
            db.commit()
            messagebox.showinfo("new team member","{} is now in your team".format(value))


        except:
            messagebox.showerror("error", "You already have a center")



        #mylabel=Label(root,text=value)
        #mylabel.grid(row=4,column=4)




    #new.grab_set()
    #new.grab_release()
    r=StringVar()
    bn=-1
    l2=[]
    for i in range(0,8):

        l2.append(Radiobutton(frame2,variable=r,value=listc[i],command=lambda : clicked(r.get()),image=centerlist[i]))
    l2[0].grid(row=0,column=1)
    l2[1].grid(row=0,column=3)
    l2[2].grid(row=0, column=5)
    l2[3].grid(row=1, column=2)
    l2[4].grid(row=1, column=4)
    l2[5].grid(row=1, column=6)
    l2[6].grid(row=2, column=1)
    l2[7].grid(row=2, column=3)



    frame2.update()
    canvas_container.configure(yscrollcommand=myscrollbar.set,scrollregion="0 0 0 %s" % frame2.winfo_height())
    canvas_container.pack(side=RIGHT)
    myscrollbar.pack(side=RIGHT, fill=Y)

    frame_container.pack()

ar1 = ImageTk.PhotoImage(Image.open('C:/Users/Ritunjay Rao/Downloads/lebronjames.png'))
ar2 = ImageTk.PhotoImage(Image.open("C:/Users/Ritunjay Rao/Downloads/kevindurant.png"))
ar3 = ImageTk.PhotoImage(Image.open("C:/Users/Ritunjay Rao/Downloads/kawhileaonard.png"))
ar4 = ImageTk.PhotoImage(Image.open("C:/Users/Ritunjay Rao/Downloads/anthonydavis.png"))
ar5 = ImageTk.PhotoImage(Image.open("C:/Users/Ritunjay Rao/Downloads/zionwilliamson.png"))
ar6 = ImageTk.PhotoImage(Image.open("C:/Users/Ritunjay Rao/Downloads/jimmybutler.png"))
#ar7 = ImageTk.PhotoImage(Image.open("C:/Users/Ritunjay Rao/Downloads/cjmcollum.png"))
#a8 = ImageTk.PhotoImage(Image.open("C:/Users/Ritunjay Rao/Downloads/donovanmitchell.png"))
sflist=[ar1,ar2,ar3,ar4,ar5,ar6]
sql = "select * from sf order by Overall desc"
mycur.execute(sql)
result = mycur.fetchall()
l = list(result)
l4 = []
for i in range(len(l)):
    l4.append("\'{}\'".format(l[i][1]))

listsf = l4[:6]
nlist=[]
def sf():
    new=Toplevel(root)
    new.title("Small Forward")
    frame_container = Frame(new)

    canvas_container = Canvas(frame_container,height=800,width=1500)
    frame2 = Frame(canvas_container)
    myscrollbar = Scrollbar(frame_container, orient="vertical",command=canvas_container.yview)  # will be visible if the frame2 is to to big for the canvas
    canvas_container.create_window((0, 0), window=frame2, anchor='nw')

    def clicked(value):



        try:




            sql="insert into myteam(Jersey_number,Name,Position,Overall,Shooting_Outside,Shooting_inside,Defense_outside,Defense_inside,Passing,img) select * from sf where Name like {}".format(value)


            mycur.execute(sql)
            db.commit()
            messagebox.showinfo("new team member","{} is now in your team".format(value))


        except:
            messagebox.showerror("error", "You already have a small forward")



        #mylabel=Label(root,text=value)
        #mylabel.grid(row=4,column=4)




    #new.grab_set()
    #new.grab_release()
    r=StringVar()
    bn=-1
    l2=[]
    for i in range(0,6):

        l2.append(Radiobutton(frame2,variable=r,value=listsf[i],command=lambda : clicked(r.get()),image=sflist[i]))
    l2[0].grid(row=0,column=1)
    l2[1].grid(row=0,column=3)
    l2[2].grid(row=0, column=5)
    l2[3].grid(row=1, column=2)
    l2[4].grid(row=1, column=4)
    l2[5].grid(row=1, column=6)




    frame2.update()
    canvas_container.configure(yscrollcommand=myscrollbar.set,scrollregion="0 0 0 %s" % frame2.winfo_height())
    canvas_container.pack(side=RIGHT)
    myscrollbar.pack(side=RIGHT, fill=Y)

    frame_container.pack()

sql = "select * from pg order by Overall desc"
mycur.execute(sql)
result = mycur.fetchall()
l = list(result)
l4 = []
for i in range(len(l)):
    l4.append("\'{}\'".format(l[i][1]))

l5 = l4[:11]
nlist=[]




def pg():
    new=Toplevel(root)
    new.title("Point Guard")
    frame_container = Frame(new)

    canvas_container = Canvas(frame_container,height=800,width=1500)
    frame2 = Frame(canvas_container)
    myscrollbar = Scrollbar(frame_container, orient="vertical",command=canvas_container.yview)  # will be visible if the frame2 is to to big for the canvas
    canvas_container.create_window((0, 0), window=frame2, anchor='nw')

    def clicked(value):

        sql2="select * from myteam"
        mycur.execute(sql2)
        res=mycur.fetchall()
        count=0
        for i in res:
            if res[0][2]=="PG":
                count+=1

        try:
            if count<=1:
                sql = "insert into myteam(Jersey_number,Name,Position,Overall,Shooting_Outside,Shooting_inside,Defense_outside,Defense_inside,Passing,img) select * from pg where Name like {}".format(
                    value)

                mycur.execute(sql)
                db.commit()
                messagebox.showinfo("new team member","{} is now in your team".format(value))
            else:
                messagebox.showerror("error", "You already have a point guard")
        except:
            messagebox.showerror("error","You already have a point guard")


        #mylabel=Label(root,text=value)
        #mylabel.grid(row=4,column=4)





    r=StringVar()
    bn=-1
    l2=[]
    for i in range(0,11):

        l2.append(Radiobutton(frame2,variable=r,value=l5[i],command=lambda : clicked(r.get()),image=l3[i]))
    l2[0].grid(row=0,column=1)
    l2[1].grid(row=0,column=3)
    l2[2].grid(row=0, column=5)
    l2[3].grid(row=1, column=2)
    l2[4].grid(row=1, column=4)
    l2[5].grid(row=1, column=6)
    l2[6].grid(row=2, column=1)
    l2[7].grid(row=2, column=3)
    l2[8].grid(row=2, column=5)
    l2[9].grid(row=3, column=2)
    l2[10].grid(row=3, column=4)


    frame2.update()
    canvas_container.configure(yscrollcommand=myscrollbar.set,scrollregion="0 0 0 %s" % frame2.winfo_height())
    canvas_container.pack(side=RIGHT)
    myscrollbar.pack(side=RIGHT, fill=Y)

    frame_container.pack()



messagebox.showinfo("selectplayer","click on a player to select in the team")
point = ImageTk.PhotoImage(Image.open("C:/Users/Ritunjay Rao/Downloads/pg_image.png"))

height=20
width=20
img = ImageTk.PhotoImage(Image.open("C:/Users/Ritunjay Rao/Downloads/pguard.png"))

pg=Button(labelframe1,text="pg", command=pg)
pg.grid(row=0,column=1)
center=Button(labelframe1,text="center",command=center)
center.grid(row=0,column=500)
sg=Button(labelframe1,text="sg", command=sg)
sg.grid(row=200,column=20)
sf=Button(labelframe1,text="sf", command=sf)
sf.grid(row=300,column=40)
pf=Button(labelframe1,text="pf", command=pf)
pf.grid(row=30,column=40)
MYTEAM=Button(labelframe1,text="MYTEAM", command=myteam)
MYTEAM.grid(row=500,column=500)

root.deiconify()





root.mainloop()
