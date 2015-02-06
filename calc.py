#!/usr/bin/python3

"""
Functions for doing geographical calculations.
"""
from math import radians, cos, sin, asin, sqrt


def haversine(lon1, lat1, lon2, lat2):
    """
    Calculate the great circle distance between two points
    on the earth (specified in decimal degrees).
    """
    # Convert decimal degrees to radians
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # Haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * asin(sqrt(a))

    # 6371 km is the approx. radius of the Earth
    km = 6371 * c

    return km

def total_distance(pos):
    """
    Calculate the total tour distance from the given positions.
    """
    # Extract the arguments from the lists to calculate distance with haversine
    f = lambda l1, l2: haversine(l1[0], l1[1], l2[0], l2[1])

    # Call f on every pair of list elements, skip the wrap-around element
    sums = [f(pos[i - 1], x) for i, x in enumerate(pos)][1:]

    # Return the sum of the distances
    return sum(sums)

def closest_stops(stops, addrs):
    """
    Find the closest stops to the given addresses from the given stop
    positions.
    Return a list of (address, stop time) tuples.
    """
    stop_addrs = []

    # Go through all addresses and find the closest stop positions
    for i, a in enumerate(addrs):
        # Compare distance using haversine, a is an enumerate tuple
        f = lambda x: haversine(x[1][0], x[1][1], a[3], a[4])

        # Find closest index and value using min and comparing with f
        min_ix, min_stop = min(enumerate(stops), key=f)

        # Save (stop time, address) tuple
        stop_addrs.append((a, min_stop[2]))

    return stop_addrs

def order_addresses(addrs, stops):
    """
    Order the given addresses based on delivery time.
    """
    sorted_pos = []
    # Find closest stop position + timestamp for each address
    stop_addrs = closest_stops(stops, addrs)
    # Sort tuples on timestamp
    stop_addrs.sort(key=lambda x: x[1])
    # Unpack tuples to remove timestamps
    stop_addrs = [s for s, _ in stop_addrs]

    return stop_addrs
