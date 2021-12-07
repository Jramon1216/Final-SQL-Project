import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Visions1216!",
  database="Menagerie"
 
)

mycursor = mydb.cursor()

#mycursor.execute("CREATE TABLE pet (name VARCHAR(20), owner VARCHAR(20), species VARCHAR(20), sex CHAR(1), birth DATE, death DATE)")
#mycursor.execute("SHOW DATABASES")
#mycursor.execute("DROP DATABASE Menagerie")
#mycursor.execute("DESCRIBE pet")
#mycursor.execute("LOAD DATA LOCAL INFILE 'C:/Users/Jonathan/Desktop/YUNY/CIS/Module_2/CIS_402/Final_Project/pet.txt' INTO TABLE pet")
#mycursor.execute("SELECT * FROM pet WHERE species = 'dog' AND sex = 'f'")
#mycursor.execute("SELECT name, birth FROM pet")
#mycursor.execute("SELECT owner, COUNT(*) FROM pet GROUP BY owner")

mycursor.execute("SELECT name, birth, MONTH(birth) FROM pet")

for x in mycursor:
  print(x) 

