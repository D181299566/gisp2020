# pyproj definitions
from pyproj import CRS
WGS84  = CRS.from_epsg(4326)
WEB_MERCATOR = CRS.from_epsg(3857)
TM65 = CRS.from_epsg(29902)
TM75 = CRS.from_epsg(29903)
ITM = CRS.from_epsg(2157)

# Database connection arguments
DB_CONN_STRING = "dbname=census2011 user=student password=student host=193.1.33.31 port=5433"

# Geoserver URL constructed based on required resource
def get_geoserver_url(workspace, layer, epsg_code, output_format="json",):
    return f"http://193.1.33.31:8081/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature" \
          f"&typeName={workspace}:{layer}&outputFormat={output_format}&srsName=epsg:{epsg_code}"
    # url += property_text
    # url += filter_text

