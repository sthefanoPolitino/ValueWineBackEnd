from ..Services.dbUsuarioService import get_db
from ..Resources.createTablas import createTablaUsuario, createTablaVino


def createSchema():
    DB, c = get_db()
    if DB == False:
        return str(c)

    c.execute("SHOW TABLES")
    tablas = []
    for x in c:
        tablas.append(x['Tables_in_valuewine'])

    try:
        tablas.index('Usuario')
    except:
        c.execute(createTablaUsuario)
        print('creacion tabla usuario')

    try:
        tablas.index('Vino')
    except:
        c.execute(createTablaVino)
        print('creacion tabla vino')
    c.close()
    DB.close()
    return print('Tablas Listas')
