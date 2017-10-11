import os.path as Path
import sqlite3

SQL_SELECT_ALL = """
    SELECT id, task_name, task_description, created, finish_time
    FROM dairy
"""
