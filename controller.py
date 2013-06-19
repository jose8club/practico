#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3
#from form import Ui_Dialog
#import view_form



def obtener_alumnos():
    con = conectar()
    c = con.cursor()
    query = "SELECT * FROM alumnos"
    resultado= c.execute(query)
    alumnos = resultado.fetchall()
    con.close()
    return alumnos

def obtener_alumno(rut):
    con = conectar()
    c = con.cursor()
    query = "SELECT * FROM alumnos WHERE rut = ?"
    resultado = c.execute(query, [rut])
    alumno = resultado.fetchone()
    con.close()
    return alumno

def obtener_cursos():
    con = conectar()
    c = con.cursor()
    query = "SELECT * FROM cursos"
    resultado= c.execute(query)
    alumnos = resultado.fetchall()
    con.close()
    return alumnos

def delete(rut):
    exito = False
    con = conectar()
    c = con.cursor()
    query = "DELETE FROM alumnos WHERE rut = ?"
    try:
        resultado = c.execute(query, [rut])
        con.commit()
        exito = True
    except sqlite3.Error as e:
        exito = False
        print "Error:", e.args[0]
    con.close()
    return exito

def create(rut, nombres, apellidos, correo):
    exito = False
    con = conectar()
    c = con.cursor()
    values = [rut, nombres, apellidos, correo]
    query = "INSERT INTO alumnos (rut, nombres, apellidos, correo) VALUES(?,?,?,?)"
    try:
        resultado = c.execute(query, values)
        con.commit()
        exito = True
    except sqlite3.Error as e:
        exito = False
        print "Error:", e.args[0]
    con.close()
    return exito

def edit(rut, nombres, apellidos, correo):
    exito = False
    con = conectar()
    c = con.cursor()
    try:
        data = obtener_alumno(rut)
        #c.execute("UPDATE FROM alumnos SET rut=? WHERE rut=?",(rut, data["rut"]))
        c.execute("UPDATE alumnos SET nombres=?, apellidos=?, correo=? WHERE rut = ?",(nombres, apellidos, correo, data["rut"]))
        con.commit()
        exito = True
    except sqlite3.Error as e:
        exito = False
        print "Error:", e.args[0]
    con.close()
    return exito
    
def cursos(id_curso):
    con = conectar()
    c = con.cursor()
    values = [id_curso]
    query = "SELECT * FROM alumnos WHERE id_curso = ?"
    resultado = c.execute(query, values)
    alumnos = resultado.fetchall()
    con.close()
    return alumnos


if __name__ == "__main__":

    alumnos = obtener_alumnos()
    for alumno in alumnos:
        print alumno["nombres"]
