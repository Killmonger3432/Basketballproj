import mysql.connector
import re
db=mysql.connector.connect(user="root", host="localhost",passwd="Killmonger3432",auth_plugin="mysql_native_password",database="project")
c=db.cursor()
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
exec_sql_file(c,'/Users/agasthya/Pygame_BasketballGame/mysql_tables/project_myteam.sql')
exec_sql_file(c,'/Users/agasthya/Pygame_BasketballGame/mysql_tables/project_players.sql')
exec_sql_file(c,'/Users/agasthya/Pygame_BasketballGame/mysql_tables/project_results.sql')