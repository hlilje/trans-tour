#!/usr/bin/python3

import calc as cl
import database as db


if __name__ == "__main__":
    db.connect()
    db.test_db()

    pos = db.get_positions()
    start_addr = db.get_start_address()

    print(cl.total_distance(pos))
    print(start_addr)

    db.close()
