from logger_base import log
# import psycopg2 as bd
from psycopg2 import pool
import sys
import platform

myOs = platform.system()
print(f'Mi os = {myOs}')


class Conexion:
    # Atributos de clase
    _DATABASE = 'test_db'
    _USERNAME = 'postgres'
    if myOs == "Windows":
        _PASSWORD = 'postgres'
        _HOST = '192.168.1.133'
    else:
        _PASSWORD = 'N3570r$b'
        _HOST = 'localhost'
    _DB_PORT = '5432'
    _MIN_CON = 1
    _MAX_CON = 5
    _pool = None

    # _conexion = None
    # _cursor = None

    @classmethod
    def obtenerPool(cls):
        if cls._pool is None:
            try:
                cls._pool = pool.SimpleConnectionPool(cls._MIN_CON,
                                                      cls._MAX_CON,
                                                      host=cls._HOST,
                                                      user=cls._USERNAME,
                                                      password=cls._PASSWORD,
                                                      port=cls._DB_PORT,
                                                      database=cls._DATABASE
                                                      )
                log.debug(f'Creacion del Pool Exitosa, {cls._pool}')
                return cls._pool
            except Exception as e:
                log.error(f'Ocurrio un error al obtener el poool, {e}')
                sys.exit()
        else:
            return cls._pool

    @classmethod
    def obtenerConexion(cls):
        conexion = cls.obtenerPool().getconn()
        log.debug(f'Conexion Obtenida del Pool {conexion}')
        return conexion

    @classmethod
    def liberarConexion(cls, conexion):
        cls.obtenerPool().putconn(conexion)
        log.debug(f'Regresamos la conexion al pool: {conexion}')

    @classmethod
    def cerrarConexiones(cls):
        cls.obtenerPool().closeall()


if __name__ == '__main__':
    # Conexion.obtenerConexion()
    # Conexion.obtenerCursor()

    conexion1 = Conexion.obtenerConexion()
    Conexion.liberarConexion(conexion1)
    # conexion2 = Conexion.obtenerConexion()
    # conexion3 = Conexion.obtenerConexion()
    # conexion4 = Conexion.obtenerConexion()
    # conexion5 = Conexion.obtenerConexion()
