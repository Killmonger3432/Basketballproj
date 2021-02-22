import mysql.connector
import re
a=input("Enter your MySQL user name (usually root)")
b=input("Enter your MySQL host (usually localhost)")
c=input("Enter your MySQL remote Password(No security risk)")
try:
    db=mysql.connector.connect(user=a, host=b,passwd=c,auth_plugin="mysql_native_password")
    cur=db.cursor()
    cur.execute("Create DATABASE if not exists project_swisheroo")
    db.commit()
    cur.close()
    db.close()
    db=mysql.connector.connect(user=a, host=b,passwd=c,auth_plugin="mysql_native_password",database="project_swisheroo")
    cur=db.cursor()
except:
    print("connection error, check your details")
    print("User Name entered=",a,"Host=",b,"Password=",c)

def exec_sql_file(cursor, sql_file):
    statement = ""

    for line in open(sql_file):
        if re.match(r'--', line):  # ignore sql comment lines
            continue
        if not re.search(r';$', line):  # keep appending lines that don't end in ';'
            statement = statement + line
        else:  # when you get a line ending in ';' then exec statement and reset for next statement
            statement = statement + line
            #print "\n\n[DEBUG] Executing SQL statement:\n%s" % (statement)
            cursor.execute(statement)

            statement = ""
try:
    exec_sql_file(cur,'/Users/agasthya/Pygame_BasketballGame/mysql_tables/project_myteam.sql')
    exec_sql_file(cur,'/Users/agasthya/Pygame_BasketballGame/mysql_tables/project_players.sql')
    exec_sql_file(cur,'/Users/agasthya/Pygame_BasketballGame/mysql_tables/project_results.sql')
except:
    pass
def create_det():
    global c,a,b
    sql_pwd=c
    sql_user=a
    sql_host=b
    return sql_host,sql_pwd,sql_user
