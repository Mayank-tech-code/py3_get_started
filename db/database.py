import psycopg2

connection = psycopg2.connect(user = "postgres",
                              password = "root",
                              host = "127.0.0.1",
                              port = "5432",
                              database = "College")

cursor = connection.cursor()

cursor.execute("truncate college cascade")
connection.commit()

name = 'DY Patil'
address = 'Pune'
cursor.execute('insert into college(name, address) values(%s, %s)',(name, address))

name = 'Wadia'
address = 'Pune'
cursor.execute('insert into college(name, address) values(%s, %s)',(name, address))

connection.commit()

cursor.execute('select * from college')
rows = cursor.fetchall()
college_ids = []
for row in rows:
    print(row)
    college_ids.append(row[0])

name = 'prakash'
college_id = college_ids[0]
cursor.execute('insert into student(name, college_id) values(%s, %s)',(name, college_id))

name = 'nisar'
college_id = college_ids[1]
cursor.execute('insert into student(name, college_id) values(%s, %s)',(name, college_id))

connection.commit()

cursor.execute('select * from college c inner join student s on c.id = s.college_id')
rows = cursor.fetchall()
college_ids = []
for row in rows:
    print(row)


cursor.close()