import os.path as Path
import sqlite3

SQL_SELECT_ALL = """
    SELECT id, task_name, task_description, task_status,
            task_craeted, task_realizer, task_time
    FROM dairy
"""

SQL_SELECT_TASK_BY_DATE = SQL_SELECT_ALL + " WHERE task_time=?"
SQL_INSERT_TASK = """
    INSERT INTO dairy(task_name) VALUES(?)
"""
SQL_SELECT_TASK_BY_STATUS = SQL_SELECT_ALL + " WHERE task_status=?"
SQL_UPDATE_TASK_ADD = """
    UPDATE dairy SET task_name = ?, task_description = ?, task_status = ?,
                     task_realizer = ?, task_time = ?
                    WHERE id = ?
"""
SQL_UPDATE_STATUS_EDIT = """
    UPDATE dairy SET task_status = ? WHERE id = ?
"""



def dict_factory(cursor, row):
    d = {}
    #print('==>> Row', row)
    #print('==>>', cursor.description)


    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]



    return d



def connect(db_name = None):
    if db_name is None:
        db_name = ':memory'

    conn = sqlite3.connect(db_name)
    conn.row_factory = dict_factory

    return conn


def initialize(conn, creation_schema):
    with conn, open(creation_schema) as f:
        conn.executescript(f.read())


def find_task_by_date(conn, date):
    #Возвращает список задач с текущей датой
    with conn:
        cursor = conn.execute(SQL_SELECT_TASK_BY_DATE, (date,))
        return cursor.fetchall()


def add_task(conn, name_new, description, realizer, date):
    """ Сохраняет задачу в базу """
    if not name_new:
        #Должна быть ошибка
        print('Name can not be empty!')
        return

    with conn:
        cursor = conn.execute(SQL_INSERT_TASK,(name_new,))
        pk = cursor.lastrowid

        conn.execute(SQL_UPDATE_TASK_ADD,(name_new, description,
                                         'working', realizer, date, pk))


def edit_task(conn, name_new, description, status, realizer, date, pk):
    """ Перезапись задачи """
    with conn:
        conn.execute(SQL_UPDATE_TASK_ADD,(name_new, description,
                                         status, realizer, date, pk))



def find_task_by_status(conn, status):
    with conn:
        cursor = conn.execute(SQL_SELECT_TASK_BY_STATUS,(status,))

        return cursor.fetchall()

def change_status(conn, pk, new_status):
    with conn:
        conn.execute(SQL_UPDATE_STATUS_EDIT, (new_status, pk))

def find_all(conn):
    with conn:
        cursor = conn.execute(SQL_SELECT_ALL)
        return cursor.fetchall()
