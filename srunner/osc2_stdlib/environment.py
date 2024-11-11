from srunner.osc2_dm.physical_types import Physical

class Environment:
    def __init__(self) -> None:
        self.args = {}

    def set_args(self, kw_args) -> None:
        self.args = kw_args


class Air(Environment):
    def __init__(self) -> None:
        super().__init__()
        self.args = {}

    def get_wetness(self) -> float:
        return self.args["wetness"]


class Rain(Environment):
    def __init__(self) -> None:
        super().__init__()
        self.args = {}

    def get_precipitation(self) -> float:
        return self.args["precipitation"]


class Wind(Environment):
    def __init__(self) -> None:
        super().__init__()
        self.args = {}

    def get_intensity(self) -> float:
        return self.args["intensity"]


class Fog(Environment):
    def __init__(self) -> None:
        super().__init__()
        self.args = {}

    def get_visual(self):
        return self.args["visual"]


class Clouds(Environment):
    def __init__(self) -> None:
        super().__init__()
        self.args = {}

    def get_cloudiness(self) -> float:
        return self.args["cloudiness"]


class Celestial(Environment):
    def __init__(self) -> None:
        super().__init__()
        self.args = {}

    def get_body(self):
        return self.args["body"]

    def get_angle(self):
        return self.args["angle"]
