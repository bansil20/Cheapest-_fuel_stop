import requests
from .geocoding import geocode

def get_routes(start, end):
    lat1, lon1 = geocode(start)
    lat2, lon2 = geocode(end)

    url = (
        f"http://router.project-osrm.org/route/v1/driving/"
        f"{lon1},{lat1};{lon2},{lat2}"
        f"?alternatives=true&overview=full&geometries=geojson"
    )

    r = requests.get(url).json()
    return r["routes"]