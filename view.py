#!/usr/bin/python3

"""
Functions for viewing the generated KML map.
"""
import fileinput
import os.path
import re
import sys
import webbrowser

PATH_VIEW = "view.html"
URL_KML   = "(url to public file on computer)"


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
