#!/usr/bin/python3

"""
Functions for viewing the generated KML map.
"""
import fileinput
import os.path
import re
import shutil
import sys
import webbrowser
import plot as pl

PATH_VIEW = "view.html" # Path to Google Maps html file
URL_KML   = ""          # URL to public file on computer


def copy_kml_public(folder_path):
    """
    Copies the KML file to the given public location on the computer.
    The given path must have a trailing '/'.
    """
    # Take file path specified in plot
    kml_path = os.path.realpath(pl.PATH_FILE)
    kml_file = os.path.basename(kml_path)
    folder_path = os.path.normpath(folder_path) + os.sep # Add trailing '/'

    if os.path.isdir(folder_path):
        # Copy the KML file to the given location
        shutil.copyfile(kml_path, folder_path + kml_file) # Src, dst
        print("Map file copied to:", folder_path)
    else:
        print("The given public folder does not exist")
        sys.exit(1)

def write_kml_url():
    """
    Write the KML URL to the html file for viewing.
    """
    if os.path.isfile(PATH_VIEW):
        # Replace the javascript url variable
        for line in fileinput.input(PATH_VIEW, inplace=True):
            line = re.sub(r"url:\ \'.*\'", "url: '" + URL_KML + "'", line)
            print(line, end='')
    else:
        print("View file does not exist")
        sys.exit(1)

def view():
    """
    Open the view file in the browser.
    """
    url = "file://" + os.path.abspath(PATH_VIEW)
    webbrowser.open_new_tab(url)
    print("Map opened in browser")
