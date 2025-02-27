import math
from typing import Tuple

def calculate_road_distance(
    origin_coords: Tuple[float, float],
    destination_coords: Tuple[float, float]
) -> float:
    """
    Calculates the straight-line distance (not road-based) between two points.

    Args:
        origin_coords: (latitude, longitude) starting point
        destination_coords: (latitude, longitude) destination point

    Returns:
        float: Distance in kilometers

    Example:
        >>> distance = calculate_road_distance((41.0082, 28.9784), (39.9208, 32.8541))
    Example2:
        >>> distance = some example
    """

    def to_radians(degrees: float) -> float:
        return degrees * (math.pi / 180)

    # Convert coordinates to radians
    lat1, lon1 = map(to_radians, origin_coords)
    lat2, lon2 = map(to_radians, destination_coords)

    # Earth's radius (km)
    EARTH_RADIUS_KM = 6371.0

    # Calculate distance using the Haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = (
        math.sin(dlat / 2) ** 2
        + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) ** 2
    )
    c = 2 * math.asin(math.sqrt(a))
    distance = EARTH_RADIUS_KM * c
    
    distance_meter = distance * 1000  # Convert to meters

    return distance_meter

# Example
result = calculate_road_distance((40.9956, 37.8763), (41.0000, 37.8694))
print(result)

