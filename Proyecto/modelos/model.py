import sqlite3
from sqlite3 import Connection

class Pais:
    """ Tabla PAIS: id, name """
    
    def create_table(self, con: Connection):
        query = """
            CREATE TABLE IF NOT EXISTS PAIS (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name VARCHAR(50) NOT NULL
            );
        """
        cursor = con.cursor()
        cursor.execute(query)
        con.commit()


class PostalCode:
    """ Tabla CODIGO POSTAL: id, code, pais, ciudad  y estado """ 
    def create_table(self, con: Connection):
        query = """
            CREATE TABLE IF NOT EXISTS POSTALCODE (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                code VARCHAR(50) NOT NULL,
                pais VARCHAR(50) NOT NULL,
                state VARCHAR(50) NOT NULL
            );
        """
        cursor = con.cursor()
        cursor.execute(query)
        con.commit()        

class Categorias:
    """ Tabla CATEGORIAS: id, name, subcategory """

    def create_table(self, con: Connection):
        query = """
            CREATE TABLE IF NOT EXISTS CATEGORIAS (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name VARCHAR(50) NOT NULL,
                subcategory VARCHAR(50) NOT NULL
            );
        """
        cursor = con.cursor()
        cursor.execute(query)
        con.commit()

class Productos:
    """ Tabla PRODUCTOS: id, name, product_id, subcategory_id """

    def create_table(self, con: Connection):
        query = """
            CREATE TABLE IF NOT EXISTS PRODUCTOS (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name VARCHAR(50) NOT NULL,
                product_id INTEGER NOT NULL,
                category_id INTEGER NOT NULL
            );
        """
        cursor = con.cursor()
        cursor.execute(query)
        con.commit()

## Agregar clase catálogo
class VentasPorCategoria:
    """ Clase para calcular ventas por categoría """
    
    def __init__(self, con: sqlite3.Connection):
        self.con = con

    def obtener_ventas_por_categoria(self):
        """Obtiene la cantidad de ventas y el total vendido por categoría"""
        query = """
            SELECT 
                c.name AS categoria,
                COUNT(v.id) AS total_ventas,
                SUM(v.sales_amount) AS total_ingresos
            FROM VENTAS v
            JOIN PRODUCTOS p ON v.product_id = p.product_id
            JOIN CATEGORIAS c ON p.category_id = c.id
            GROUP BY c.name
            ORDER BY total_ingresos DESC;
        """
        cursor = self.con.cursor()
        cursor.execute(query)
        return cursor.fetchall()

class Ventas:
    """ Tabla VENTAS con múltiples relaciones """

#Nuevo atributo añadido: 
    def create_table(self, con: Connection):
        query = """
            CREATE TABLE IF NOT EXISTS VENTAS (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                order_id VARCHAR(20) NOT NULL,
                postal_code VARCHAR(20),
                product_id INTEGER NOT NULL,
                sales_amount REAL NOT NULL,
                quantity INTEGER NOT NULL,
                discount REAL NOT NULL,
                profit REAL NOT NULL,
                shipping_cost REAL NOT NULL,
                order_priority VARCHAR(20) NOT NULL,
                order_date DATE NOT NULL
            );
        """
        cursor = con.cursor()
        cursor.execute(query)
        con.commit()

