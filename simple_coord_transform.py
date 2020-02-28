import gdal_workaround
import pyproj

lat = 53.5
lon = -8.0

easting = 200000
northing = 250000

transformer = pyproj.Transformer.from_crs(4326, 29903, always_xy=True)
x,y = transformer.transform(lon, lat)
print("Turned Lat: {}, Lon: {} into IG Easting: {}, Northing: {}".format(lat, lon, x, y))

transformer = pyproj.Transformer.from_crs(29903, 4326, always_xy=True)
x,y = transformer.transform(easting, northing)
print("Turned IG Easting: {}, Northing: {} into Lon: {}, Lat: {}".format(easting, northing, x, y))

