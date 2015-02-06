#!/usr/bin/python3

"""
Functions for interacting with the database.
"""
import sqlite3 as lite
import sys

# Database names
PATH_DB        = "../db/budbee.db"
TBL_START      = "start_addresses"
TBL_ADDRESSES  = "addresses"
TBL_POSITIONS  = "positions"
COL_CITY       = "city"
COL_CREATED    = "created"
COL_LATITUDE   = "latitude"
COL_LONGITUDE  = "longitude"
COL_STREETNAME = "street_name"
COL_STREETNO   = "street_no"
COL_ZIPCODE    = "zipcode"

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
        if con: con.close()
        sys.exit(1)

def get_start_address():
    """
    Queries the database and returns the start address.
    """

    data = None
    try:
        cur.execute('SELECT ' + COL_STREETNAME + ', ' + COL_STREETNO + ', ' +
                COL_ZIPCODE + ', ' + COL_CITY + ', ' + COL_LATITUDE + ', ' +
                COL_LONGITUDE + ' FROM ' + TBL_START + ' LIMIT 1')
        data = cur.fetchall()

    except lite.Error as e:
        print("Database error: %s" % e.args[0])
        if con: con.close()
        sys.exit(1)

    return data

def get_all_addresses():
    """
    Queries the database and returns all the stored addresses.
    Does not return the start address.
    """

    data = None
    try:
        cur.execute('SELECT ' + COL_STREETNAME + ', ' + COL_ZIPCODE + ', ' +
                COL_CITY + ', ' + COL_LATITUDE + ', ' + COL_LONGITUDE + ' FROM ' +
                TBL_ADDRESSES + ' ORDER BY datetime(' + COL_STREETNAME + ') ASC')
        data = cur.fetchall()

    except lite.Error as e:
        print("Database error: %s" % e.args[0])
        if con: con.close()
        sys.exit(1)

    return data

def get_all_positions():
    """
    Queries the database and returns all the stored positions.
    """

    data = None
    try:
        cur.execute('SELECT ' + COL_LATITUDE + ', ' + COL_LONGITUDE + ' FROM ' +
                TBL_POSITIONS + ' ORDER BY datetime(' + COL_CREATED + ') ASC')
        data = cur.fetchall()

    except lite.Error as e:
        print("Database error: %s" % e.args[0])
        if con: con.close()
        sys.exit(1)

    return data

def get_unique_positions():
    """
    Queries the database and returns all the stored positions without
    redundant position data.
    """

    data = None
    try:
        cur.execute('SELECT ' + COL_LATITUDE + ', ' + COL_LONGITUDE + ' FROM '
                + TBL_POSITIONS + ' ORDER BY datetime(' + COL_CREATED + ') ASC')
        data = cur.fetchall()
        # Remove adjacent duplicates, 'not' needed to get last element
        # TODO Might be a smart way to do it in SQL directly
        data = [a for a, b in zip(data, data[1:] + [not data[-1]]) if a != b]

    except lite.Error as e:
        print("Database error: %s" % e.args[0])
        if con: con.close()
        sys.exit(1)

    return data
