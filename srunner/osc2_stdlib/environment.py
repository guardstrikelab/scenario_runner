import time

from carla import WeatherParameters

from srunner.osc2_dm.physical_types import Physical


class Environment(object):
    # The maximum rainfall intensity here is set to be 50mmph. Refers to:
    # https://www.baranidesign.com/faq-articles/2020/1/19/rain-rate-intensity-classification
    MAX_RAIN_INTENSITY = 50.0  # mmph

    # The maximum wind intensity here is set to be 30mps
    MAX_WIND_INTENSITY = 30.0  # mps

    MMPH_TO_MPS = 0.000000278

    def __init__(self, weather: WeatherParameters):
        self.weather = weather

    # Carla does not support setting temperature and air pressure.
    # The wetness in OpenSCENARIO 2.0 is from 0 to 1, but the wetness in Carla is from 0 to 100
    def air(self, temperature: float = 0.0, pressure: float = 0.0, relative_humidity: float = 0.0):
        print(f"set air: temperature: {temperature}, pressure: {pressure}, relative_humidity: {relative_humidity}")
        self.weather.wetness = relative_humidity * 100.0

    def rain(self, intensity: float = 0.0):
        precipitation = intensity / Environment.MMPH_TO_MPS / Environment.MAX_RAIN_INTENSITY * 100.0
        self.weather.precipitation = precipitation
        self.weather.precipitation_deposits = 100  # if it rains, make the road wet
        self.weather.wetness = precipitation

    def snow(self, intensity: float = 0.0):
        raise AttributeError("CARLA does not support snow precipitation")

    # Carla only supports setting the intensity of the wind, not the direction of the wind.
    def wind(self, speed: float = 0.0, direction: Physical = None):
        self.weather.wind_intensity = speed / Environment.MAX_WIND_INTENSITY * 100.0

    def fog(self, visual_range: float = 0.0):
        self.weather.fog_distance = visual_range
        if self.weather.fog_distance < 1000:
            self.weather.fog_density = 100

    def clouds(self, cloudiness: int = 0):
        self.weather.cloudiness = cloudiness

    def assign_celestial_position(self, sun_or_moon: str = "environment.sun", azimuth: float = None,
                                  elevation: float = None):
        if sun_or_moon == "environment.sun":
            self.weather.cloudiness = 0
        elif sun_or_moon == "environment.moon":
            self.weather.cloudiness = 100
        self.weather.sun_azimuth_angle = azimuth
        self.weather.sun_azimuth_angle = elevation

    def datetime(self, datetime: float = time.time()):
        pass
