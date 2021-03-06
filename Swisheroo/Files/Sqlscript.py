import mysql.connector
import re,os
def ask():
    a="root"
    b="localhost"
    c=input("Enter the password to your local MySQL server")
    return a,b,c
def auth():
    global cur,a,b,c
    try:
        a,b,c=ask()
        db=mysql.connector.connect(user=a, host=b,passwd=c,auth_plugin="mysql_native_password")
        cur=db.cursor()
        cur.execute("Create DATABASE if not exists project_swisheroo")
        db.commit()
        cur.execute("USE project_swisheroo")
        cur.close()
        db.close()
        
    except:
        print("connection error, check your details")
        print("User Name entered=",a,"Host=",b,"Password=",c)
        k=int(input("Enter 1 to try again,2 to exit"))
        if k==1:
            auth()
        else:
            return "DONE"
def exec_sql_file(cursor, sql_file):
    statement = ""

    for line in open(sql_file):
        if re.match(r'--', line):  
            continue
        if not re.search(r';$', line):  
            statement = statement + line
        else:  
            statement = statement + line
            cursor.execute(statement)
            statement = ""
k1=os.path.abspath("mysql_scripts/project_myteam.sql")
k2=os.path.abspath("mysql_scripts/project_players.sql")
k3=os.path.abspath("mysql_scripts/project_results.sql")  
x=auth()
if x=="DONE":
    xyz=False
else:
    db=mysql.connector.connect(user=a, host=b,passwd=c,auth_plugin="mysql_native_password",database="project_swisheroo")
    cur=db.cursor()
    exec_sql_file(cur,k1)
    exec_sql_file(cur,k2)
    exec_sql_file(cur,k3)
    xyz=True
def create_det():
    global c,a,b
    sql_pwd=c
    sql_user=a
    sql_host=b
    if xyz==True:
        return sql_host,sql_pwd,sql_user
    else:
        return 
