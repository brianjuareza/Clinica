import pymysql
import mysql.connector
import os

def obtener_conexion():
    return pymysql.connect(host='localhost',
                                user='root',
                                password='Eduar18_12',
                                db='pacientes')

def connectionBD():
    mydb = mysql.connector.connect(
        host ="localhost",
        user ="root",
        passwd ="Eduar18_12",
        database = "pacientes"
        )
    return mydb
