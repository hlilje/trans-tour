# TransTour

A program for analysing the route taken for deliveries.

The total route distance is calculated and the delivery locations are numbered after the
order in which they were visited, according to the tracked GPS positions.

A KML map is generated with the route and numbered delivery locations.

The generated map is shown on Google Maps from a public location on the computer.

## Notes

- An SQLite database with tracked GPS positions, delivery locations and the start address
must be present in `../db/`.
- A `../kml/` folder is needed to generate the map in.
- A public location for the KML file is necessary to show it on Google Maps.
