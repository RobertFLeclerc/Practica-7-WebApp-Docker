
from flask import Flask
import mysql.connector
import os

app = Flask(__name__)

@app.route("/")
def inicio():
    try:
        conexion = mysql.connector.connect(
            host=os.getenv("DB_HOST", "db"),
            user=os.getenv("DB_USER", "appuser"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME", "practica7")
        )

        cursor = conexion.cursor()
        cursor.execute("SELECT DATABASE()")
        resultado = cursor.fetchone()

        cursor.close()
        conexion.close()

        return f"""
        <h1>Hola Mundo</h1>
        <h2>Practica 7 - Docker Compose</h2>
        <p>Conexion exitosa con MySQL.</p>
        <p>Base de datos: {resultado[0]}</p>
        """

    except mysql.connector.Error as error:
        return f"""
        <h1>Hola Mundo</h1>
        <h2>Error de conexion con MySQL</h2>
        <p>No se pudo conectar a la base de datos.</p>
        """, 503

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
