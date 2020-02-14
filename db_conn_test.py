"""
This program implements functions to get a data source from either a PostgreSQL database or a geoserver instance (GeoJSON)
"""

import generic_useful_parameters as prm
import read_from_file_or_net as rfn
import json


def main():
    CONN_STRING = prm.DB_CONN_STRING
    SQL_QUERY = "SELECT * FROM \"Counties\""

    GEOSERVER_URL = prm.get_geoserver_url("census2011", "counties", 29902)

    try:
        geo_result = rfn.get_stuff_from_net(GEOSERVER_URL)
        geo_result = json.loads(geo_result)
        if geo_result:
            print("Got {} GeoJSON features".format(len(geo_result["features"])))
    except Exception as e:
        print(f"Something bad happened trying to get data from Geoserver.\n{GEOSERVER_URL}\n{e}")

    try:
        pg_result = rfn.get_data_from_postgres(CONN_STRING, SQL_QUERY)
        if pg_result:
            print("Got {} rows from database".format(len(pg_result)))
    except Exception as e:
        print(f"Something bad happened trying to get data from PostGIS.\n{CONN_STRING}\n{e}")


if __name__ == "__main__":
    main()
