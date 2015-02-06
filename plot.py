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
    # lon, lat, optional height
    kml.newpoint(name="Kirstenbosch", coords=[(18.432314,-33.988862)])

def save():
    """
    Save the kml map file.
    """
    kml.save(FILE_NAME)
