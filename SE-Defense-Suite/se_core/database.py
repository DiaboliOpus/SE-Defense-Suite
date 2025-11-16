import sqlite3
def get_connection(): return sqlite3.connect("se_core/suite.db")
