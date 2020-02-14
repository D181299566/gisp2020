import gdal_workaround
import pyproj
import generic_useful_parameters as gup

lat = 53.5
lon = -8.0

easting = 200000
northing = 250000

x,y = pyproj.transform(gup.WGS84, gup.TM75, lon, lat)
print("Turned Lat: {}, Lon: {} into IG Easting: {}, Northing: {}".format(lat, lon, x, y))

x,y = pyproj.transform(gup.TM75, gup.WGS84, easting, northing)
print("Turned IG Easting: {}, Northing: {} into Lon: {}, Lat: {}".format(easting, northing, x, y))

