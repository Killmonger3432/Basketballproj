import pathlib
import os
b=os.path.dirname(os.path.abspath("project_myteam.sql"))
print("S",b)
print("N",os.path.abspath(os.getcwd()))
k=os.path.abspath("mysql_tables/project_myteam.sql")
f=open(k,"r")
print(f.read(

))