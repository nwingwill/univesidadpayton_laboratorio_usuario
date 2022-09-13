from conexion import Conexion
from logger_base import log


class CursordelPool:
    def __int__(self):
        self._conexion = None
        self._cursor = None

    def __enter__(self):
        log.debug('Inicio del metodo with __enter__ ')
        self._conexion = Conexion.obtenerConexion()
        self._cursor = self._conexion.cursor()
        return self._cursor

    def __exit__(self, tipoExcepcion, valorExcepcion, detalleExcepcion):
        log.debug('Se ejecuta metodo ___exit__')
        if valorExcepcion:
            self._conexion.rollback()
            log.error(f'Ocurrio una excepcion, se hace rollback: {tipoExcepcion} - {valorExcepcion} - {detalleExcepcion}')
        else:
            self._conexion.commit()
            log.debug(f'Commit de la transaccion.')
        self._cursor.close()
        Conexion.liberarConexion(self._conexion)

#
if __name__ == '__main__':
    with CursordelPool() as cursor:
        log.debug(f'Dentro del bloque With')
        cursor.execute('SELECT * FROM usuario')
        log.debug(cursor.fetchall())
