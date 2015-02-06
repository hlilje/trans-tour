#!/usr/bin/python3

"""
Functions for plotting data points/routes on a map.
"""
import simplekml

PATH_FILE = "../kml/map.kml"
URL_ICON  = "http://mapicons.nicolasmollet.com/wp-content/uploads/mapicons/shape-default/color-666666/shapecolor-color/shadow-1/border-dark/symbolstyle-white/symbolshadowstyle-dark/gradient-no/number_"

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
    pnt = kml.newpoint(name=start[0] + ' ' + start[1], description="Start address",
            coords=[(start[5], start[4])])

    # Icon based on number in route
    pnt.style.iconstyle.icon.href = URL_ICON + "1.png"

    # Plot all addresses
    for i, addr in enumerate(addrs):
        pnt = kml.newpoint(name=addr[0], coords=[(addr[4], addr[3])])
        # TODO Current URL only goes to 100
        if (i + 2) <= 100:
            pnt.style.iconstyle.icon.href = URL_ICON + str(i + 2) + ".png"

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
    kml.save(PATH_FILE)
    print("Saved map file:", PATH_FILE)
