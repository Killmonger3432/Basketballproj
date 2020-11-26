import pygame
import mysql.connector
def abc(s1,s2,s3,s4,s5,k1,k2,k3,k4,k5):
    s=pygame.display.set_mode([1450,800])
    pygame.init()
    pygame.display.set_caption("Swisheroo")
    con=mysql.connector.connect(host='localhost',database='project',user='root',password='Agasthya0112')
    cursor=con.cursor(buffered=True)
    sql1="Select Name,Shooting_Outside,Shooting_Inside,Defense_Outside,Defense_Inside,image from myteam where position = 'PG' "
    sql2="Select Name,Shooting_Outside,Shooting_Inside,Defense_Outside,Defense_Inside,image from myteam where position = 'SG' "
    sql3="Select Name,Shooting_Outside,Shooting_Inside,Defense_Outside,Defense_Inside,image from myteam where position = 'SF' "
    sql4="Select Name,Shooting_Outside,Shooting_Inside,Defense_Outside,Defense_Inside,image from myteam where position = 'PF' "
    sql5="Select Name,Shooting_Outside,Shooting_Inside,Defense_Outside,Defense_Inside,image from myteam where position = 'C'"
    sql6="""select Name,Shooting_Outside,Shooting_Inside,Defense_Outside,Defense_Inside from players where Name not like %s and position = "PG" """
    sql7="""select Name,Shooting_Outside,Shooting_Inside,Defense_Outside,Defense_Inside from players where Name not like %s and position = "SG" """
    sql8="""select Name,Shooting_Outside,Shooting_Inside,Defense_Outside,Defense_Inside from players where Name not like %s and position = "SF" """
    sql9="""select Name,Shooting_Outside,Shooting_Inside,Defense_Outside,Defense_Inside from players where Name not like %s and position = "PF" """
    sql10="""select Name,Shooting_Outside,Shooting_Inside,Defense_Outside,Defense_Inside from players where Name not like %s and position = "C" """
    cursor.execute(sql1)
    fontdef3=pygame.font.get_fonts()[0]
    winfont2=pygame.font.SysFont(fontdef3,30)
    wincenter2=(560,270)
    fontdef2=pygame.font.get_fonts()[3]
    winfont=pygame.font.SysFont(fontdef2,90)
    wincenter=(560,160)
    scoresh=pygame.font.SysFont(fontdef2,40)
    cardfont=pygame.font.SysFont(fontdef2,30)
    cardcenter=(200,150)
    valp1=cursor.fetchall()[0]
    img1=pygame.image.load(str(valp1[5])).convert()
    cursor.execute(sql2)
    valp2=cursor.fetchall()[0]
    img2=pygame.image.load(str(valp2[5])).convert()
    cursor.execute(sql3)
    valp3=cursor.fetchall()[0]
    img3=pygame.image.load(str(valp3[5])).convert()
    cursor.execute(sql4)
    valp4=cursor.fetchall()[0]
    img4=pygame.image.load(str(valp4[5])).convert()
    cursor.execute(sql5)
    valp5=cursor.fetchall()[0]
    img5=pygame.image.load(str(valp5[5])).convert()
    cursor.execute(sql6,(valp1[0],))
    valo1=cursor.fetchall()[0]
    cursor.execute(sql7,(valp2[0],))
    valo2=cursor.fetchall()[0]
    cursor.execute(sql8,(valp3[0],))
    valo3=cursor.fetchall()[0]
    cursor.execute(sql9,(valp4[0],))
    valo4=cursor.fetchall()[0]
    cursor.execute(sql10,(valp5[0],))
    valo5=cursor.fetchall()[0]
    COURT=pygame.image.load("Courtn2.png").convert()
    icon=pygame.image.load("icon2.jpeg").convert()
    pygame.display.set_icon(icon)
    l1=pygame.image.load("chrispaul.png").convert()
    l2=pygame.image.load("klaythompson.png").convert()
    l3=pygame.image.load("kawhileonard.png").convert()
    l4=pygame.image.load("danilogallinari.png").convert()
    l5=pygame.image.load("kristapsporzingis.png").convert()
    if s1+s2+s3+s4+s5>k1+k2+k3+k4+k5:
        r=True
    else:
        r=False
    if r:
        wintext= "YOU WIN"
    else:
        wintext= "YOU LOSE"
    wintext2="Exit window to close game"
    Playsc="PLAYER SCORECARD"
    Oppsc="OPPONENT SCORECARD"
    sL1=valp1[0]+" -  "+str(s1)
    sL2=valp2[0]+" -  "+str(s2)
    sL3=valp3[0]+" -  "+str(s3)
    sL4=valp4[0]+" -  "+str(s4)
    sL5=valp5[0]+" - "+str(s5)
    sM5=valo5[0]+" -  "+str(k5)
    sM4=valo4[0]+" -  "+str(k4)
    sM3=valo3[0]+" -  "+str(k3)
    sM2=valo2[0]+" -  "+str(k2)
    sM1=valo1[0]+" - "+str(k1)
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
    if r:
        pygame.mixer.music.load("CHA.mp3")
        pygame.mixer.music.play(start=39)
    else:
        pygame.mixer.music.load("SOS.mp3")
        pygame.mixer.music.play(start=0)
    i=True
    while i:
        s.fill([0,0,0])
        s.blit(COURT,(0,0))
        s.blit(l1,(0,520))
        s.blit(l2,(312,520))
        s.blit(l3,(624,520))
        s.blit(l4,(936,520))
        s.blit(l5,(1250,520))
        s.blit(splblit,(cardcenter[0]-80,cardcenter[1]-60))
        s.blit(sblit1,cardcenter)
        s.blit(sblit2,(cardcenter[0],cardcenter[1]+40))
        s.blit(sblit3,(cardcenter[0],cardcenter[1]+80))
        s.blit(sblit4,(cardcenter[0],cardcenter[1]+120))
        s.blit(sblit5,(cardcenter[0],cardcenter[1]+160))
        s.blit(sopblit,(1000,90))
        s.blit(opblit1,(1100,150))
        s.blit(opblit2,(1100,190))
        s.blit(opblit3,(1100,230))
        s.blit(opblit4,(1100,270))
        s.blit(opblit5,(1100,310))
        s.blit(winblit,wincenter)
        s.blit(winblit2,wincenter2)
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
        pygame.display.update()

