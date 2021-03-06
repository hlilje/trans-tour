#!/usr/bin/python3

import calc as cl
import database as db
import plot as pl
import view as vw


if __name__ == "__main__":
    db.connect()

    start_addr = db.get_start_address()
    stops      = db.get_stop_positions()
    pos        = db.get_unique_positions()
    addrs      = cl.order_addresses(db.get_all_addresses(), stops)

    tot_dist = cl.total_distance(pos)
    print("Total route distance:", round(tot_dist, 2), "km")

    pl.init()
    pl.plot_addresses(start_addr, addrs)
    pl.plot_route(pos)
    pl.save()

    vw.copy_kml_public("/home/hlilje/Dropbox/")
    vw.write_kml_url()
    vw.view()

    db.close()
