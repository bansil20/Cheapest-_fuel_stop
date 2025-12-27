from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="fuel_app")

def geocode(place):
    location = geolocator.geocode(place)
    if not location:
        raise ValueError(f"Could not geocode location: {place}")
    return location.latitude, location.longitude  #lat, log malse
