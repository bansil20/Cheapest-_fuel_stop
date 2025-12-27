from fuel_app_api.models import FuelStation

def segment_route(distance, max_range=500):
    segments = []
    while distance > max_range:
        segments.append(max_range)
        distance -= max_range
    if distance > 0:
        segments.append(distance)
    return segments


def cheapest_station():
    return FuelStation.objects.order_by("price").first()


def cheapest_station_in_state(state):
    return FuelStation.objects.filter(state=state).order_by("price").first()


def compute_cost(segments, state=None):
    total = 0
    stops = []

    if state:
        station = cheapest_station_in_state(state)
    else:
        station = None

    # fallback if no station in state or state not given
    if not station:
        station = cheapest_station()

    if not station:
        raise ValueError("No fuel stations available in database")

    for seg in segments:
        gallons = seg / 10    
        cost = gallons * station.price
        total += cost
        stops.append({
            "station": station.name,
            "price": station.price,
            "segment_miles": round(seg, 2)
        })

    return total, stops


def compute_route_cost(route, start_coords, end_coords, state=None):
    distance_miles = route["distance"] / 1609.34
    segments = segment_route(distance_miles)
    total, stops = compute_cost(segments, state)

    map_url = (
        f"https://www.google.com/maps/dir/"
        f"{start_coords[0]},{start_coords[1]}/"
        f"{end_coords[0]},{end_coords[1]}"
    )

    return {
        "distance": round(distance_miles, 2),
        "duration": round(route["duration"] / 3600, 2),
        "fuel_stops": stops,
        "fuel_cost": round(total, 2),
        "map_url": map_url
    }


def choose_best_route(routes, start_coords, end_coords, state=None):
    if not routes:
        raise ValueError("No routes returned from routing service")

    enriched = [compute_route_cost(r, start_coords, end_coords, state) for r in routes]
    best = min(enriched, key=lambda r: r["fuel_cost"])
    return best, enriched
