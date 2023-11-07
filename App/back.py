import sqlite3

dbase = sqlite3.connect('records.db')
c = dbase.cursor()
dbase.execute('''CREATE TABLE IF NOT EXISTS records(
              ID INT PRIMARY KEY NOT NULL,
              NAME TEXT NOT NULL
)''')

#aplica as mudanças na nossa database
dbase.commit()

def write(ID, NAME):
    c.execute(''' INSERT into records(ID, NAME) VALUES(?,?)''', (ID, NAME))
    dbase.commit()


def delete(x):
    c.execute('''delete from records where NAME=?''', x)
    dbase.commit()

def read_task():
    c = dbase.cursor()
    c.execute('''SELECT NAME from records''')
    data = c.fetchall()
    dbase.commit()
    return data
