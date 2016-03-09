#!/usr/bin/env python

import sys
import math
import random
import colorsys
import tempfile
import argparse

import pygmaps

def parse_cmd_args():

    parser = argparse.ArgumentParser(description="Plot IP address locations "
                                                 "on a world map.")

    parser.add_argument("-f", "--file_name", type=str,
                        help="IP, latitude, longitude, asn")

    return parser.parse_args()


def load_addresses_locations(file_name):

    ips_geolocations = {}

    with open(file_name, "r") as fd:
        for line in fd:
            line = line.strip()
            loc = line.split(',')
            try:
                ips_geolocations[loc[0]] = (float(loc[1]),float(loc[2]),loc[3])
            except:
                print loc
    return ips_geolocations


def main():

    args = parse_cmd_args()

    my_map = pygmaps.maps(0, 0, 2)
    colors = ["#ff0000", "#00ff00", "#0000ff", "#ffff00", "#00ffff", "#ff00ff",
              "#000000", "#ffffff", "#770000", "#007700", "#000077", "#777700",
              "#007777", "#770077"]

    # Iterate over all files provided over the command line and plot its IP
    # addresses on a map in different colours.

    color = colors.pop(0)
    locations = load_addresses_locations(args.file_name)
    for address in locations.keys():
        latitude, longitude, country = locations[address]
        my_map.addpoint(latitude, longitude, color=color, title=address)

    # Write the resulting map to disk.
    output_file = tempfile.mktemp(prefix="map_", suffix=".html")
    my_map.draw(output_file)
    print >> sys.stderr, "[*] Wrote output to: %s" % output_file

    return 0

if __name__ == "__main__":
    sys.exit(main())
