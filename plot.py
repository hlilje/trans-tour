#!/usr/bin/python3

"""
Functions for plotting data points/routes on a map.
"""
import os
import simplekml
import sys

PATH_FILE     = "../kml/map.kml"
URL_ICON_PRE  = "http://chart.apis.google.com/chart?chst=d_map_pin_letter&amp;chld="
URL_ICON_POST = "|FF0000"

kml = None # The kml map object


def init():
    """
    Initialise the kml map object.
    """
    global kml
    kml = simplekml.Kml()

def icon_url(n):
    """
    Get the URL corresponding to the given icon.
    """
    return URL_ICON_PRE + str(n) + URL_ICON_POST

def plot_addresses(start_addr, addrs):
    """
    Plot the given start address and addresses on the map.
    """
    # Switched order: lon, lat, (optional height)
    start = start_addr[0] # Unpack tuple from array
    pnt = kml.newpoint(name=start[0] + ' ' + start[1], description="Start address",
            coords=[(start[5], start[4])])

    # Icon based on number in route
    pnt.style.iconstyle.icon.href = icon_url(1)

    # Plot all addresses
    for i, addr in enumerate(addrs):
        pnt = kml.newpoint(name=addr[0], coords=[(addr[4], addr[3])])
        pnt.style.iconstyle.icon.href = icon_url(i + 2)

def plot_route(pos, thin=1):
    """
    Plot the given route on the map. The second argument specifies how much
    thinning should be done.
    """
    pos = pos[::thin] # Only take the thin't element

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
    if os.path.isdir(os.path.dirname(os.path.realpath(PATH_FILE))):
        kml.save(PATH_FILE)
        print("Saved map file:", PATH_FILE)
    else:
        print("No kml folder to generate file in")
        sys.exit(1)
