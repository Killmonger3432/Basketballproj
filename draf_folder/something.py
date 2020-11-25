import mysql.connector
db=mysql.connector.connect(host='localhost',
                                         database='user',
                                         user='root',
                           password='mysqlpswrd4321')
cursor=db.cursor()
l=['Jayson Tatum','Kevin Love','Zion Williamson','Domantas Sabonis','Jaren Jackson Jr','John Collins','Blake Griffin','Antony Davis','Al Horford','Pascal Siakam','Danilo Gallinari']
for i in l:
    sql1="insert into pf (select * from players where Name like \'{}\')".format(i)
    sql2="delete from sf where Name like \'{}\'".format(i)
    cursor.execute(sql1)
    cursor.execute(sql2)

db.commit()
    
    
   
