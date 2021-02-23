#!/usr/bin/env python
'''
SQL Introducción [Python]
Ejercicios de práctica
---------------------------
Autor: Inove Coding School
Version: 1.1

Descripcion:
Programa creado para poner a prueba los conocimientos
adquiridos durante la clase
'''

__author__ = "Pedro Luis Lugo Garcia"
__email__ = "pllugo@gmail.com"
__version__ = "1.1"

import sqlite3

# https://extendsclass.com/sqlite-browser.html


def create_schema():

    # Conectarnos a la base de datos
    # En caso de que no exista el archivo se genera
    # como una base de datos vacia
    conn = sqlite3.connect('secundaria.db')

    # Crear el cursor para poder ejecutar las querys
    c = conn.cursor()

    # Ejecutar una query
    c.execute("""
                DROP TABLE IF EXISTS secundaria;
            """)

    # Ejecutar una query
    c.execute("""
            CREATE TABLE secundaria(
                [id] INTEGER PRIMARY KEY AUTOINCREMENT,
                [name] TEXT NOT NULL,
                [age] INTEGER NOT NULL,
                [grade] INTEGER,
                [tutor] TEXT
            );
            """)

    # Para salvar los cambios realizados en la DB debemos
    # ejecutar el commit, NO olvidarse de este paso!
    conn.commit()

    # Cerrar la conexión con la base de datos
    conn.close()


def fill():
    print('Completemos esta tablita!')
    # Llenar la tabla de la secundaria con al menos 5 estudiantes
    # Cada estudiante tiene los posibles campos:
    # id --> este campo es auto incremental por lo que no deberá completarlo
    # name --> El nombre del estudiante (puede ser solo nombre sin apellido)
    # age --> cuantos años tiene el estudiante
    # grade --> en que año de la secundaria se encuentra (1-6)
    # tutor --> nombre de su tutor

    # Se debe utilizar la sentencia INSERT.
    # Observar que hay campos como "grade" y "tutor" que no son obligatorios
    # en el schema creado, puede obivar en algunos casos completar esos campos
    conn = sqlite3.connect('secundaria.db')
    c = conn.cursor()
    insert('Pedro', 35, 6, 'Maria')
    insert('Carolina', 28, 3, 'Luis')
    insert('Juana', 20, 3, 'Roberto')
    insert('Diego', 19, 1, 'Alejandro')
    conn.commit()
     # Cerrar la conexión con la base de datos
    conn.close()


def fetch():
    print('Comprovemos su contenido, ¿qué hay en la tabla?')
    # Utilizar la sentencia SELECT para imprimir en pantalla
    # todas las filas con todas sus columnas
    # Utilizar fetchone para imprimir de una fila a la vez
     # Conectarse a la base de datos
    conn = sqlite3.connect('secundaria.db')
    c = conn.cursor()

    # Leer todas las filas y obtener todos los datos juntos
    c.execute('SELECT * FROM secundaria')
    data = c.fetchall()
    print(data)

    # Leer todas las filas y obtener los datos de a uno
    c.execute('SELECT * FROM secundaria')
    print('Recorrer los datos desde el cursor')
    while True:
        row = c.fetchone()
        if row is None:
            break
        print(row)
    # Cerrar la conexión con la base de datos
    conn.close()

def search_by_grade(grade):
    print('Operación búsqueda!')
    # Utilizar la sentencia SELECT para imprimir en pantalla
    # aquellos estudiantes que se encuentra en en año "grade"

    # De la lista de esos estudiantes el SELECT solo debe traer
    # las siguientes columnas por fila encontrada:
    # id / name / age
    conn = sqlite3.connect('secundaria.db')
    c = conn.cursor()
    print('Recorrer los datos directamente de la query')
    for row in c.execute('SELECT * FROM secundaria WHERE grade =?', (grade,)):
        print(row)
    # Cerrar la conexión con la base de datos
    conn.close()


def insert(name, age, grade='', tutor=''):
    print('Nuevos ingresos!')
    # Utilizar la sentencia INSERT para ingresar nuevos estudiantes
    # a la secundaria
    conn = sqlite3.connect('secundaria.db')
    c = conn.cursor()

    values = [name, age, grade, tutor]

    c.execute("""
        INSERT INTO secundaria (name, age, grade, tutor)
        VALUES (?,?,?,?);""", values)

    conn.commit()
    # Cerrar la conexión con la base de datos
    conn.close()


def modify(id, name):
    print('Modificando la tabla')
    # Utilizar la sentencia UPDATE para modificar aquella fila (estudiante)
    # cuyo id sea el "id" pasado como parámetro,
    # modificar su nombre por "name" pasado como parámetro
     # Conectarse a la base de datos
    conn = sqlite3.connect('secundaria.db')
    c = conn.cursor()

    rowcount = c.execute("UPDATE secundaria SET id =? WHERE name =?",
                         (id, name)).rowcount

    print('Filas actualizadas:', rowcount)

    # Save
    conn.commit()
    # Cerrar la conexión con la base de datos
    conn.close()

def show():
    # Conectarse a la base de datos
    conn = sqlite3.connect('secundaria.db')
    c = conn.cursor()
    # Leer todas las filas y obtener todos los datos juntos
    c.execute('SELECT * FROM secundaria')
    data = c.fetchall()
    print(data)
    # Cerrar la conexión con la base de datos
    conn.close()


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    create_schema()   # create and reset database (DB)
   
    fill()
    fetch()

    show()

    grade = 3
    search_by_grade(grade)

    show()

    new_student = ['Francisco', 16]
    insert(new_student[0], new_student[1])

    show()

    name = '¿Inove?'
    id = 2
    modify(id, name)

    show()
