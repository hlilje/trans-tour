#!/usr/bin/python3

"""
Functions for plotting data points/routes on a map.
"""
import simplekml

FILE_NAME = "../kml/map.kml"

kml = None # The kml map object


def init():
    """
    Initialise the kml map object.
    """
    global kml
    kml = simplekml.Kml()

def plot_addresses(start_addr, addrs):
    """
    Plot the given start address and addresses on the map.
    """
    start = start_addr[0] # Unpack tuple from array
    kml.newpoint(name=start[0] + ' ' + start[1], description="Start address",
            coords=[(start[4], start[5])])

    # Plot all addresses
    for addr in addrs:
        kml.newpoint(name=addr[0], coords=[(addr[3], addr[4])])

def plot_route(pos):
    """
    Plot the given route on the map.
    """

    # Plot all positional points in segments from x to x + 1
    # TODO Thin the number of plotted positions
    for i, p in enumerate(pos[:-1]):
        p1 = p
        p2 = pos[i + 1]
        kml.newlinestring(name="Route", description="Delivery route",
                coords=[(p1[0], p1[1]), (p2[0], p2[1])])

def save():
    """
    Save the kml map file.
    """
    kml.save(FILE_NAME)
    print("Saved map file:", FILE_NAME)
