import mysql.connector

db=mysql.connector.connect(
    host='localhost',
    user='root',
    password='2312'
)
cursor= db.cursor()

cursor.execute('use steams')
cursor.execute('''CREATE TABLE login(
               id int AUTO_INCREMENT primary key,
               name varchar(250) NOT NULL,
               password VARCHAR(255) NOT NULL)''')

db.commit()
cursor.close()
db.close()