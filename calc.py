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
    # Extracts the arguments from the lists to calculate distance with haversine
    f = lambda l1, l2: haversine(l1[0], l1[1], l2[0], l2[1])

    # Call f on every pair of list elements
    # TODO Add smart condition
    sums = [f(pos[i - 1], x) for i, x in enumerate(pos) if True][1:]
    print(sums)

    # Returns the sum of the distances
    return sum(sums)
