#!/usr/bin/python3

import calc as cl
import database as db


if __name__ == "__main__":
    db.connect()
    db.test_db()

    pos = db.get_positions()
    start_addr = db.get_start_address()

    # print(cl.total_distance(pos))
    # print(start_addr)

    test = [[59.3792707, 17.9037962, 0, 50, 80.859375, '2015-01-04 14:00:42'],
            [59.38612, 17.8922192, 13.22468280792236, 10, 306.9140625, '2015-01-04 14:19:15'],
            [59.4056151, 18.3176224, 6.822463035583496, 5, 165.5859375, '2015-01-04 15:37:39'],
            [59.4250348, 18.3322676, 0.8699989914894104, 5, 161.71875, '2015-01-04 19:22:39']]
    print("test:", test)
    print(cl.total_distance(test), "km")

    test2 = [[59.38612, 17.8922192, 13.22468280792236, 10, 306.9140625, '2015-01-04 14:19:15'],
            [59.4056151, 18.3176224, 6.822463035583496, 5, 165.5859375, '2015-01-04 15:37:39']]
    print("test2:", test2)
    print("ref:", cl.haversine(test2[0][0], test2[0][1], test2[1][0], test2[1][1]), "km")

    db.close()
