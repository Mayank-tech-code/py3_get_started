import psycopg2

connection = psycopg2.connect(user = "postgres",
                              password = "root",
                              host = "127.0.0.1",
                              port = "5432",
                              database = "College")

cursor = connection.cursor()

name = 'DY Patil'
address = 'Pune'
cursor.execute('insert into college(name, address) values(%s, %s)',(name, address))

name = 'Wadia'
address = 'Pune'
cursor.execute('insert into college(name, address) values(%s, %s)',(name, address))

connection.commit()

cursor.execute('select * from college')
rows = cursor.fetchall()
for row in rows:
    print(row)


cursor.close()