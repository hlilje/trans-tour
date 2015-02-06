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
    # Lon, lat, optional height
    start_addr = start_addr[0] # Unpack tuple from array
    kml.newpoint(name=start_addr[0] + ' ' + start_addr[1],
            coords=[(start_addr[4], start_addr[5])])

    # Plot all addresses
    for addr in addrs:
        kml.newpoint(name=addr[0], coords=[(addr[3], addr[4])])

def save():
    """
    Save the kml map file.
    """
    kml.save(FILE_NAME)
    print("Saved file:", FILE_NAME)
