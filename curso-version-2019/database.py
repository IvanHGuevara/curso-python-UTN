import json
import sqlite3

conn = sqlite3.connect('db.sqlite')
cur = conn.cursor()

cur.executescript('''
DROP TABLE IF EXISTS User;
CREATE TABLE User (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    nombre   TEXT UNIQUE,
    edad     INTEGER,
    materiasAprobadas   INTEGER
)
''')

archivoJSON = open('materias.json').read()
jsonData = json.loads(archivoJSON)
for entrada in jsonData:
    print(entrada['edad'])
    print(entrada['materiasAprobadas'])

    nombre = entrada['nombre']
    edad = entrada['edad']
    materiasAprobadas = entrada['materiasAprobadas']

    cur.execute('''INSERT OR REPLACE INTO User (nombre, edad, materiasAprobadas) 
        VALUES ( ?, ?, ? )''',
    ( nombre, edad, materiasAprobadas, ) )

    cur.execute('SELECT * FROM User')
    print(cur.fetchone())

