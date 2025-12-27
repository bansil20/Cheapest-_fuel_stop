from rest_framework.decorators import api_view
from rest_framework.response import Response
from fuel_app_api.services.routing import get_routes
from fuel_app_api.services.fuel_logic import choose_best_route
from fuel_app_api.services.geocoding import geocode


@api_view(["POST"])
def plan_route(request):
    start = request.data["start"]
    end = request.data["end"]

    start_coords = geocode(start)
    end_coords = geocode(end)  

    routes = get_routes(start, end)
    best, all_routes = choose_best_route(routes, start_coords, end_coords)

    return Response({
        "best_route": best,
        "all_routes": all_routes
    })
