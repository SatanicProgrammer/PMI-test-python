"""Funciones para el programa 'reloj fuera de tiempo'"""
from datetime import datetime


def año_actual():
    return datetime.now().year


def mes_actual():
    return datetime.now().month


def dia_actual():
    return datetime.now().day


def hora_actual():
    return datetime.now().hour


def minuto_actual():
    return datetime.now().minute


def segundo_actual():
    return datetime.now().second
