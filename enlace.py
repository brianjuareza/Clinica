from bd import obtener_conexion


def insertar_datos(Nombres, Apellidos, Fecha_de_nacimiento, Direccion, Telefono, Gmail):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("INSERT INTO datos(Nombres, Apellidos, Fecha_de_nacimiento, Direccion, Telefono, Gmail) VALUES (%s, %s, %s, %s, %s, %s)",
                       (Nombres, Apellidos, Fecha_de_nacimiento, Direccion, Telefono, Gmail))
    conexion.commit()
    conexion.close()


def obtener_datos():
    conexion = obtener_conexion()
    datos = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT id, Nombres, Apellidos, Fecha_de_nacimiento, Direccion, Telefono, Gmail FROM datos")
        datos = cursor.fetchall()
    conexion.close()
    return datos


def eliminar_datos(id):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("DELETE FROM datos WHERE id = %s", (id,))
    conexion.commit()
    conexion.close()


def obtener_datos_por_id(id):
    conexion = obtener_conexion()
    dato = None
    with conexion.cursor() as cursor:
        cursor.execute(
            "SELECT id, Nombres, Apellidos, Fecha_de_nacimiento, Direccion, Telefono, Gmail FROM datos WHERE id = %s", (id))
        dato = cursor.fetchone()
    conexion.close()
    return dato


def actualizar_datos(Nombres, Apellidos, Fecha_de_nacimiento, Direccion, Telefono, Gmail, id):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("UPDATE datos SET Nombres=%s, Apellidos=%s, Fecha_de_nacimiento=%s, Direccion=%s, Telefono=%s, Gmail=%s WHERE id = %s",
                       (Nombres, Apellidos, Fecha_de_nacimiento, Direccion, Telefono, Gmail, id))
    conexion.commit()
    conexion.close()

def insertar_cita(Folio, Nombres, Apellidos, Telefono, Direccion, Fecha, Menu, Gmail):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("INSERT INTO cita(Folio, Nombres, Apellidos, Telefono, Direccion, Fecha, Menu, Gmail) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
                       (Folio, Nombres, Apellidos, Telefono, Direccion, Fecha, Menu, Gmail))
    conexion.commit()
    conexion.close()
