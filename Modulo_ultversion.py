import sqlite3

class Modulo:
     def __init__(self):
        self.bd = sqlite3.connect("club.sqlite")
        self.cursor = self.bd.cursor()

# Importa un módulo para interactuar con SQLite para conectarse con el archivo de BD y se define un cursor para recorrer la BD. Clase madre.

