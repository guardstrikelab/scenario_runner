from srunner.osc2_dm.physical_types import Physical


def air(weather, wetness: float):
    weather.wetness = wetness


def rain(weather, precipitation: Physical):
    weather.precipitation = precipitation.gen_physical_value() * 18000000


def wind(weather, intensity: Physical):
    weather.wind_intensity = intensity.gen_physical_value() * 2.5


def fog(weather, visual_distance: Physical):
    weather.fog_falloff = 3
    weather.fog_density = 50
    weather.fog_distance = visual_distance.gen_physical_value()


def clouds(weather, cloudiness: float):
    weather.cloudiness = cloudiness * 12.5


def assign_celestial_position(weather, body: str, azimuth: Physical, elevation: Physical):
    # Carla里面好像没有月亮，直接太阳倒转表示月亮
    if body == "sun":
        weather.sun_azimuth_angle = azimuth.num
        weather.sun_altitude_angle = elevation.num
    elif body == "moon":
        weather.sun_altitude_angle = azimuth.num
        weather.sun_altitude_angle = -1 * elevation.num
