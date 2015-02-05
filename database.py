#!/usr/bin/python3

"""
Functions for interacting with the database.
"""
import sqlite3 as lite
import sys

PATH_DB = "../db/budbee.db"

con = None # Database connection
cur = None # Database cursor


def connect():
    """
    Establish database connection.
    """
    global con, cur

    try:
        con = lite.connect(PATH_DB)
        cur = con.cursor()

    except lite.Error as e:
        print("Database error: %s" % e.args[0])
        if con: con.close()
        sys.exit(1)

def close():
    """
    Close database connection.
    """
    if con: con.close()

def test_db():
    """
    Test database connection.
    """

    try:
        cur.execute('SELECT SQLITE_VERSION()')
        data = cur.fetchone()

        print("SQLite version: %s" % data)

    except lite.Error as e:
        print("Database error: %s" % e.args[0])
        sys.exit(1)

def get_positions():
    """
    Queries the database and returns all the stored positions.
    """

    data = None
    try:
        cur.execute('SELECT * FROM positions ORDER BY datetime(created) ASC')
        data = cur.fetchall()

    except lite.Error as e:
        print("Database error: %s" % e.args[0])
        if con: con.close()
        sys.exit(1)

    return data
