import datetime
from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="my-application")
import pyproj
from pyproj import CRS


def geocode_address(address=""):
    """
    Address geocoder using OSM Nominatim. Accepts 'address' string and returns a dictionary response containing
    everything that the geocoder provides.

    :param address: Address to be geocoded
    :return: response as dict
    """
    body = {}

    try:
        if not address:
            raise Exception("No address supplied")

        loc = geolocator.geocode(address, addressdetails=True)

        if not loc:
            raise Exception(f"No result found for '{address}'")

        body["message"] = f"Called 'geocode_address'. OK! {datetime.datetime.now()}"
        body["input_address"] = address
        body["result"] = loc.raw

        response = {
            "body": body
        }
    except Exception as e:
        body["error"] = f"{e} - {datetime.datetime.now()}"
        response = {
            "body": body
        }

    return response


def geocode_location(location="", epsg=4326):
    """
    Address geocoder using OSM Nominatim. Accepts 'location' string in lat, lon format and returns a
    dictionary response containing everything that the geocoder provides.

    :param location: string in lat, lon
    :param epsg: EPSG code of input coordinates, these will be converted to EPSG:4326 if not already 4326
    :return: dict response
    """
    body = {}

    # set the input projection of the original file.
    input_projection = CRS.from_epsg(epsg)
    # set the projection for the output file.
    output_projection = CRS.from_epsg(4326)

    try:
        if not location:
            raise Exception("No location supplied")

        if epsg != 4326:
            lon, lat = pyproj.transform(
                input_projection, output_projection, float(location.strip().split(",")[0]),
                float(location.strip().split(",")[1])
            )
        else:
            lon, lat = float(location.strip().split(",")[1]), float(location.strip().split(",")[0])

        loc = geolocator.reverse(f"{lon}, {lat}")

        if not loc:
            raise Exception("No result found for '{}'".format(location))

        body["message"] = "Called 'geocode_location'. OK! {}".format(datetime.datetime.now())
        body["input_location"] = location
        body["result"] = loc.raw

        response = {
            "body": body
        }
    except Exception as e:
        body["error"] = "{} - {}".format(e, datetime.datetime.now())
        response = {
            "body": body
        }

    return response


if __name__ == "__main__":
    my_address = "Drumcondra, Dublin, Ireland"
    result = geocode_address(my_address)
    print(result)
    my_location = "53.33, -6.33"
    result = geocode_location(my_location)
    print(result)
    my_location = "200000.0, 250000"
    result = geocode_location(my_location, 29902)
    print(result)