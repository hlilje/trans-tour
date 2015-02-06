# TransTour

A program for analysing the route taken for deliveries.

The total route distance is calculated and the delivery locations are numbered after the
order in which they were visited, according to the tracked GPS positions.

A KML map is generated with the route and numbered delivery locations.

## Notes

- The program expects an SQLite database with tracked GPS positions, delivery locations
and the start address in `../db/`.
- The program needs a `../kml/` folder to generate the map in.
