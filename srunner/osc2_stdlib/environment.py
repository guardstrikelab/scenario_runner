from srunner.osc2_dm.physical_types import Physical


def air(weather, wetness):
    weather.wetness = wetness


def rain(weather, precipitation):
    weather.precipitation = precipitation


def wind(weather, intensity):
    weather.wind_intensity = intensity


def fog(weather, visual_distance):
    weather.fog_falloff = 6
    weather.fog_density = 50
    weather.fog_distance = visual_distance


def clouds(weather, cloudiness):
    weather.cloudiness = cloudiness


def assign_celestial_position(weather, body, azimuth, elevation):
    # Carla里面好像没有月亮，直接太阳倒转表示月亮
    if body == "sun":
        weather.sun_azimuth_angle = azimuth
        weather.sun_altitude_angle = elevation
    elif body == "moon":
        weather.sun_altitude_angle = azimuth
        weather.sun_altitude_angle = -1 * elevation
