import pygame
import mysql.connector
from leaderboard import leaders
def abc(s1,s2,s3,s4,s5,k1,k2,k3,k4,k5,valp1,valp2,valp3,valp4,valp5,valo1,valo2,valo3,valo4,valo5):
    s=pygame.display.set_mode([1450,800])
    pygame.init()
    fontdef3=pygame.font.get_fonts()[0]
    winfont2=pygame.font.SysFont(fontdef3,30)
    wincenter2=(560,125)
    fontdef2=pygame.font.get_fonts()[3]
    winfont=pygame.font.SysFont(fontdef2,90)
    wincenter=(560,25)
    scoresh=pygame.font.SysFont(fontdef2,40)
    cardfont=pygame.font.SysFont(fontdef2,30)
    cardcenter=(200,150)
    rfontdef=pygame.font.get_fonts()[30]
    rfont=pygame.font.SysFont(rfontdef,30)
    rcenter=(555,215)
    r2center=(600,270)
    gfont=pygame.font.SysFont(rfontdef,20)
    gcenter=(670,300)
    lfont=pygame.font.SysFont(fontdef3,30)
    rtext="Results of your last 5 games"
    r2font=pygame.font.SysFont(rfontdef,15)
    r2text="Game 5 refers to the 5th game before this"
    ltext="Press L to see the leaderboard"
    img1=pygame.image.load(str(valp1[5])).convert()
    img2=pygame.image.load(str(valp2[5])).convert()
    img3=pygame.image.load(str(valp3[5])).convert()
    img4=pygame.image.load(str(valp4[5])).convert()
    img5=pygame.image.load(str(valp5[5])).convert()
    COURT=pygame.image.load("Courtn2.png").convert()
    icon=pygame.image.load("icon2.jpeg").convert()
    pygame.display.set_icon(icon)
    if s1+s2+s3+s4+s5>k1+k2+k3+k4+k5:
        r=True
    else:
        r=False
    db=mysql.connector.connect(host='localhost',database='project',user='root',password='Agasthya0112')
    cur=db.cursor()
    sql1="select * from results"
    cur.execute(sql1)
    res=cur.fetchall()
    nonetext="Not played"
    g1text="Game 1 -"+nonetext
    g2text="Game 2 -"+nonetext
    g3text="Game 3 -"+nonetext
    g4text="Game 4 -"+nonetext
    g5text="Game 5 -"+nonetext
    lcenter=(1000,395)
    if res != []:
        g1text="Game 1 - "+ res[0][0]
        if res[0][1]!=None:
            g2text="Game 2 - "+res[0][1]
        if res[0][2]!=None:
            g3text="Game 3 -"+res[0][2]
        if res[0][3]!=None:
            g4text="Game 4 -"+res[0][3]
        if res[0][4]!=None:
            g5text="Game 5 -"+res[0][4]
    
    if r:
        wintext= "YOU WIN"
        pygame.mixer.music.load("CHA.mp3")
        pygame.mixer.music.play(start=39)
        if res==[]:
            sql2='insert into results(Game_1) value("W")'
            cur.execute(sql2)
            db.commit()
        elif res[0][1]==None:
            sql2='update  results set Game_2 = "W"'
            cur.execute(sql2)
            db.commit()
        elif res[0][2]==None:
            sql2='update  results set Game_3 = "W"'
            cur.execute(sql2)
            db.commit()
        elif res[0][3]==None:
            sql2='update  results set Game_4 = "W"'
            cur.execute(sql2)
            db.commit()
        elif res[0][4]==None:
            sql2='update  results set Game_5 = "W"'
            cur.execute(sql2)
            db.commit()
        else:
            sql1='update results set Game_5 = %s'
            sql2='update results set Game_4 = %s'
            sql3='update results set Game_3 = %s'
            sql4='update results set Game_2 = %s'
            sql5='update results set Game_1="W"'
            cur.execute(sql1,(res[0][3],))
            cur.execute(sql2,(res[0][2],))
            cur.execute(sql3,(res[0][1],))
            cur.execute(sql4,(res[0][0],))
            cur.execute(sql5)
            
            
            db.commit()
            
            
    else:
        wintext= "YOU LOSE"
        pygame.mixer.music.load("SOS.mp3")
        pygame.mixer.music.play(start=0)
        
        if res==[]:
            sql2='insert into results(Game_1) value("L")'
            cur.execute(sql2)
            db.commit()
        elif res[0][1]==None:
            sql2='update  results set Game_2 = "L"'
            cur.execute(sql2)
            db.commit()
        elif res[0][2]==None:
            sql2='update  results set Game_3 = "L"'
            cur.execute(sql2)
            db.commit()
        elif res[0][3]==None:
            sql2='update  results set Game_4 = "L"'
            cur.execute(sql2)
            db.commit()
        elif res[0][4]==None:
            sql2='update  results set Game_5 = "L"'
            cur.execute(sql2)
            db.commit()
        else:
            sql1='update results set Game_5 = %s'
            sql2='update results set Game_4 = %s'
            sql3='update results set Game_3 = %s'
            sql4='update results set Game_2 = %s'
            sql5='update results set Game_1="L"'
            cur.execute(sql1,(res[0][3],))
            cur.execute(sql2,(res[0][2],))
            cur.execute(sql3,(res[0][1],))
            cur.execute(sql4,(res[0][0],))
            cur.execute(sql5)
            
            
            db.commit()
    sql3="update players set points = points+%s where Name = %s"
    val=(s1,valp1[0])
    val2=(s2,valp2[0])
    val3=(s3,valp3[0])
    val4=(s4,valp4[0])
    val5=(s5,valp5[0])
    val6=(k1,valo1[0])
    val7=(k2,valo2[0])
    val8=(k3,valo3[0])
    val9=(k4,valo4[0])
    val10=(k5,valo5[0])
    cur.execute(sql3,val)
    cur.execute(sql3,val2)
    cur.execute(sql3,val3)
    cur.execute(sql3,val4)
    cur.execute(sql3,val5)
    cur.execute(sql3,val6)
    cur.execute(sql3,val7)
    cur.execute(sql3,val8)
    cur.execute(sql3,val9)
    cur.execute(sql3,val10)
    
    db.commit()
    wintext2="Exit window to close game"
    Playsc="PLAYER SCORECARD"
    Oppsc="OPPONENT SCORECARD"
    sL1=valp1[0]+" -  "+str(s1)
    sL2=valp2[0]+" -  "+str(s2)
    sL3=valp3[0]+" -  "+str(s3)
    sL4=valp4[0]+" -  "+str(s4)
    sL5=valp5[0]+" - "+str(s5)
    sM5=valo5[0]+" -  "+str(k1)
    sM4=valo4[0]+" -  "+str(k2)
    sM3=valo3[0]+" -  "+str(k3)
    sM2=valo2[0]+" -  "+str(k4)
    sM1=valo1[0]+" - "+str(k5)
    winblit2=winfont2.render(wintext2,True,[0,0,0],[155,0,0])
    winblit = winfont.render(wintext,True, [0,0,0], [155,0,0])
    splblit=scoresh.render(Playsc,True,[0,0,0],[155,0,0])
    sopblit=scoresh.render(Oppsc,True,[0,0,0],[155,0,0])
    sblit1=cardfont.render(sL1,True,[0,0,0],[155,0,0])
    sblit2=cardfont.render(sL2,True,[0,0,0],[155,0,0])
    sblit3=cardfont.render(sL3,True,[0,0,0],[155,0,0])
    sblit4=cardfont.render(sL4,True,[0,0,0],[155,0,0])
    sblit5=cardfont.render(sL5,True,[0,0,0],[155,0,0])
    opblit1=cardfont.render(sM1,True,[0,0,0],[155,0,0])
    opblit2=cardfont.render(sM2,True,[0,0,0],[155,0,0])
    opblit3=cardfont.render(sM3,True,[0,0,0],[155,0,0])
    opblit4=cardfont.render(sM4,True,[0,0,0],[155,0,0])
    opblit5=cardfont.render(sM5,True,[0,0,0],[155,0,0])
    gblit=gfont.render(g1text,True,[0,0,0],[155,0,0])
    g2blit=gfont.render(g2text,True,[0,0,0],[155,0,0])
    g3blit=gfont.render(g3text,True,[0,0,0],[155,0,0])
    g4blit=gfont.render(g4text,True,[0,0,0],[155,0,0])
    g5blit=gfont.render(g5text,True,[0,0,0],[155,0,0])
    rblit=rfont.render(rtext,True,[0,0,0],[155,0,0])
    r2blit=r2font.render(r2text,True,[0,0,0],[155,0,0])
    lblit=lfont.render(ltext,True,[0,0,0],[155,0,0])
    i=True
    while i:
        s.fill([0,0,0])
        s.blit(COURT,(0,0))
        s.blit(img1,(0,520))
        s.blit(img2,(312,520))
        s.blit(img3,(624,520))
        s.blit(img4,(936,520))
        s.blit(img5,(1250,520))
        s.blit(splblit,(cardcenter[0]-80,cardcenter[1]-60))
        s.blit(sblit1,cardcenter)
        s.blit(sblit2,(cardcenter[0],cardcenter[1]+40))
        s.blit(sblit3,(cardcenter[0],cardcenter[1]+80))
        s.blit(sblit4,(cardcenter[0],cardcenter[1]+120))
        s.blit(sblit5,(cardcenter[0],cardcenter[1]+160))
        s.blit(gblit,gcenter)
        s.blit(g2blit,(gcenter[0],gcenter[1]+30))
        s.blit(g3blit,(gcenter[0],gcenter[1]+60))
        s.blit(g4blit,(gcenter[0],gcenter[1]+90))
        s.blit(g5blit,(gcenter[0],gcenter[1]+120))
        s.blit(sopblit,(1000,90))
        s.blit(opblit1,(1100,150))
        s.blit(opblit2,(1100,190))
        s.blit(opblit3,(1100,230))
        s.blit(opblit4,(1100,270))
        s.blit(opblit5,(1100,310))
        s.blit(winblit,wincenter)
        s.blit(winblit2,wincenter2)
        s.blit(rblit,rcenter)
        s.blit(r2blit,r2center)
        s.blit(lblit,lcenter)
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_l:
                        leaders()
        pygame.display.update()
db=mysql.connector.connect(host='localhost',database='project',user='root',password='Agasthya0112')
cur=db.cursor()
sql1="select * from results"
cur.execute(sql1)

