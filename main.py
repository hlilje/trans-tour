#!/usr/bin/python3

import calc as cl
import database as db


if __name__ == "__main__":
    db.connect()

    start_addr = db.get_start_address()
    addrs = db.get_all_addresses()
    pos = db.get_unique_positions()

    tot_dist = cl.total_distance(pos)

    print("Start address:", start_addr)
    # print("Addresses:")
    # print(addrs)
    # print("Positions:")
    # print(pos)
    print("Total distance:", tot_dist, "km")

    db.close()
