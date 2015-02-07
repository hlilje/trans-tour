#!/usr/bin/python3

"""
Functions for viewing the generated KML map.
"""
import fileinput
import os.path
import re
import sys

PATH_VIEW = "view.html"
URL_KML   = "TODO"


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
        print("View does not exist")
        sys.exit(1)
