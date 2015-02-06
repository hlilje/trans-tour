#!/usr/bin/python3

import calc as cl
import database as db
import plot as pl


if __name__ == "__main__":
    db.connect()

    start_addr = db.get_start_address()
    addrs = db.get_all_addresses()
    pos = db.get_unique_positions()

    tot_dist = cl.total_distance(pos)

    # print("Start address:", start_addr)
    # print("Addresses:")
    # print(addrs)
    # print("Positions:")
    # print(pos)
    print("Total distance:", round(tot_dist, 2), "km")

    # pl.init()
    # pl.plot_addresses(start_addr, addrs)
    # pl.plot_route(pos) # Optional param for thinning
    # pl.save()

    print(db.get_stop_positions())

    db.close()
