#!/usr/bin/python3

import calc as cl
import database as db


if __name__ == "__main__":
    db.connect()
    db.test_db()

    data = db.get_positions()
    print(data[0])

    db.close()
