import pathlib
a=pathlib.Path(__file__).absolute()
print(a)
f=open(a)
import os
b=os.path.dirname(os.path.abspath("project_myteam.sql"))
print("S",b)
print("N",os.path.abspath(os.getcwd()))
print(os.path.abspath("mysql_tables/project_myteam.sql"))