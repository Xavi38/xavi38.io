

# Importando Libreria mysql.connector para conectar Python con MySQL
import mysql.connector


def connectionBD():
    print("ENTRO A LA CONEXION")
    try:
        # connection = mysql.connector.connect(
        connection = mysql.connector.connect(
            host="monorail.proxy.rlwy.net",
                #host="viaduct.proxy.rlwy.net",
            port=55239,
            user="root",
            passwd="c6FeghAF1fCG53B5hc-C22ABG5bhf46F",
                #passwd="-3GNBRLZpGgc9kPcWT8aBiVNxPPJVGuqLR3",
            database="railway",
                #database="crud_python",
            charset='utf8mb4',
            collation='utf8mb4_unicode_ci',
            raise_on_warnings=True

        )
        if connection.is_connected():
            print("Conexión exitosa a la BD")
            return connection

    except mysql.connector.Error as error:
        print(f"No se pudo conectar: {error}")


