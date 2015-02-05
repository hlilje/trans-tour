#!/usr/bin/python3

import calc as cl
import database as db


if __name__ == "__main__":
    db.connect()

    pos = db.get_unique_positions()
    start_addr = db.get_start_address()
    tot_dist = cl.total_distance(pos)

    print("Start address:", start_addr)
    print("Total distance:", tot_dist, "km")

    db.close()
