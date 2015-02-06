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
    # Switched order: lon, lat, (optional height)
    start = start_addr[0] # Unpack tuple from array
    kml.newpoint(name=start[0] + ' ' + start[1], description="Start address",
            coords=[(start[5], start[4])])

    # Plot all addresses
    for addr in addrs:
        kml.newpoint(name=addr[0], coords=[(addr[4], addr[3])])

def plot_route(pos, thin=1):
    """
    Plot the given route on the map. The second argument specifies how much
    thinning should be done.
    """

    pos = pos[::thin] # Only take element number thin

    # Plot all positional points in segments from x to x + 1
    for i, p in enumerate(pos[:-1]):
        p1 = p
        p2 = pos[i + 1]
        kml.newlinestring(name="Route", description="Delivery route",
                coords=[(p1[1], p1[0]), (p2[1], p2[0])])

def save():
    """
    Save the kml map file.
    """
    kml.save(FILE_NAME)
    print("Saved map file:", FILE_NAME)
