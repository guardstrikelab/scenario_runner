import random
import sys
from time import sleep

from srunner.osc2_dm.physical_types import Physical
from srunner.osc2_stdlib.misc_object import AVCarSide, ScenarioEvent
from srunner.osc2_stdlib.vehicle import Vehicle


class Modifier:
    def __init__(self, actor_name: str, name: str) -> None:
        self.actor_name = actor_name
        self.name = name
        self.args = {}

    def set_args(self, kw_args) -> None:
        self.args = kw_args

    def get_name(self) -> str:
        return self.name

    def get_actor_name(self) -> str:
        return self.actor_name

    def __str__(self) -> str:
        s = f"{self.name}("
        for key, value in self.args.items():
            s += str(key) + ":" + str(value) + ","
        return s + ")"


class SpeedModifier(Modifier):
    # speed([speed: ]<speed>, [faster_than: <car> | slower_than: <car>][, at: <event>])
    def __init__(self, actor_name: str, name: str) -> None:
        super().__init__(actor_name, name)
        self.args = {}

    def set_speed(self, speed) -> None:
        self.args["speed"] = speed

    def get_speed(self):
        speed = self.args["speed"]
        if isinstance(speed, Physical):
            return Physical(speed.gen_single_value(), speed.unit)
        else:
            print("[Error] 'speed' parameter of SpeedModifier must be 'Physical' type")
            sys.exit(1)

    def set_relative_car(self, car: Vehicle, side: AVCarSide) -> None:
        self.args[side] = car

    def set_trigger_point(self, trigger_point: ScenarioEvent) -> None:
        self.args["at"] = trigger_point


class PositionModifier(Modifier):
    # position([distance: ]<distance> | time: <time>, [ahead_of: <car> | behind: <car>], [at: <event>])
    def __init__(self, actor_name: str, name: str) -> None:
        super().__init__(actor_name, name)

    def get_distance(self):
        dist = self.args["distance"]
        if isinstance(dist, Physical):
            return dist
        else:
            print(
                "[Error] 'distance' parameter of PositionModifier must be 'Physical' type"
            )
            sys.exit(1)

    def get_refer_car(self):
        if self.args.get("ahead_of"):
            return self.args.get("ahead_of"), "ahead_of"
        elif self.args.get("behind"):
            return self.args.get("behind"), "behind"
        else:
            print("PositionModifier key error")

    def get_trigger_point(self) -> str:
        return self.args.get("at", "all")


class LaneModifier(Modifier):
    # lane([[lane: ]<lane>][right_of | left_of | same_as: <car>] | [side_of: <car>, side: <av-side>][at: <event>])
    # <av-side> is right or left.
    def __init__(self, actor_name: str, name: str) -> None:
        super().__init__(actor_name, name)

    def get_refer_car(self):
        if self.args.get("right_of"):
            return self.args.get("right_of"), "right_of"
        elif self.args.get("left_of"):
            return self.args.get("left_of"), "left_of"
        elif self.args.get("same_as"):
            return self.args.get("same_as"), "same_as"
        elif self.args.get("side_of"):
            return self.args.get("side_of"), self.args.get("side")
        else:
            return None

    def get_lane_id(self):
        return self.args.get("lane")

    def get_trigger_point(self) -> str:
        return self.args.get("at", "all")


class ChangeSpeedModifier(Modifier):
    # change_speed([speed: ]<speed>)
    def __init__(self, actor_name: str, name: str) -> None:
        super().__init__(actor_name, name)

    def get_speed(self):
        desired_speed = self.args["desired_speed"]
        if isinstance(desired_speed, Physical):
            return Physical(desired_speed.gen_single_value(), desired_speed.unit)
        else:
            print(
                "[Error] 'desired_speed' parameter of ChangeSpeedModifier must be 'Physical' type"
            )
            sys.exit(1)


class ChangeLaneModifier(Modifier):
    def __init__(self, actor_name: str, name: str) -> None:
        super().__init__(actor_name, name)

    def get_lane_changes(self):
        if len(self.args.values()) == 1:
            return 1
        else:
            if (
                self.args["lane_changes"][0] != "["
                and self.args["lane_changes"][-1] != "]"
            ):
                return int(float(self.args["lane_changes"]))
            else:
                values = self.args["lane_changes"][1:-1].split("..")
                start = int(float(values[0]))
                end = int(float(values[1]))
                value = random.randint(start, end)
                return value

    def get_side(self):
        for value in self.args.values():
            if value == "right":
                return "right"
            elif value == "left":
                return "left"
        else:
            print("ChangeLaneModifier has no such position define")


class AccelerationModifier(Modifier):
    def __init__(self, actor_name: str, name: str) -> None:
        super().__init__(actor_name, name)

    def get_accelerate(self):
        return self.args["acceleration"]


class LateralModifier(Modifier):
    def __init__(self, actor_name: str, name: str) -> None:
        super().__init__(actor_name, name)

    def get_distance(self):
        dist = self.args["distance"]
        if isinstance(dist, Physical):
            return dist
        else:
            print(
                "[Error] 'distance' parameter of PositionModifier must be 'Physical' type"
            )
            sys.exit(1)

    def get_refer_car(self):
        if self.args.get("right_of"):
            return self.args.get("right_of"), "right_of"
        elif self.args.get("left_of"):
            return self.args.get("left_of"), "left_of"
        elif self.args.get("same_as"):
            return self.args.get("same_as"), "same_as"
        elif self.args.get("side_of"):
            return self.args.get("side_of"), self.args.get("side")
        else:
            return None

    def get_trigger_point(self):
        return self.args.get("at", "all")


class YawModifier(Modifier):
    def __init__(self, actor_name: str, name: str) -> None:
        super().__init__(actor_name, name)

    def get_angle(self):
        if(
                self.args["angle"][0] != "[" and self.args["angle"][-1] != "]"
        ):
            return int(float(self.args["angle"]))
        else:
            values = self.args["lane_changes"][1:-1].split("..")
            start = int(float(values[0]))
            end = int(float(values[1]))
            value = random.randint(start, end)
            return value


class OrientationModifier(Modifier):
    def __init__(self, actor_name: str, name: str) -> None:
        super().__init__(actor_name, name)

    def get_yaw(self):
        if (
                self.args["yaw"][0] != "[" and self.args["yaw"][-1] != "]"
        ):
            return int(float(self.args["yaw"]))
        else:
            values = self.args["yaw"][1:-1].split("..")
            start = int(float(values[0]))
            end = int(float(values[1]))
            value = random.randint(start, end)
            return value

    def get_pitch(self):
        if (
                self.args["pitch"][0] != "[" and self.args["pitch"][-1] != "]"
        ):
            return int(float(self.args["pitch"]))
        else:
            values = self.args["pitch"][1:-1].split("..")
            start = int(float(values[0]))
            end = int(float(values[1]))
            value = random.randint(start, end)
            return value

    def get_roll(self):
        if (
                self.args["roll"][0] != "[" and self.args["roll"][-1] != "]"
        ):
            return int(float(self.args["roll"]))
        else:
            values = self.args["roll"][1:-1].split("..")
            start = int(float(values[0]))
            end = int(float(values[1]))
            value = random.randint(start, end)
            return value


class AlongModifier(Modifier):
    def __init__(self, actor_name: str, name: str) -> None:
        super().__init__(actor_name, name)

    def get_route(self):
        return self.args["route"]

    def get_start(self):
        start_offset = self.args["start_offset"]
        if isinstance(start_offset, Physical):
            return start_offset
        else:
            print(
                "[Error] 'distance' parameter of PositionModifier must be 'Physical' type"
            )
            sys.exit(1)

    def get_end(self):
        end_offset = self.args["end_offset"]
        if isinstance(end_offset, Physical):
            return end_offset
        else:
            print(
                "[Error] 'distance' parameter of PositionModifier must be 'Physical' type"
            )
            sys.exit(1)


class AlongTrajectoryModifier(Modifier):
    def __init__(self, actor_name: str, name: str) -> None:
        super().__init__(actor_name, name)

    def get_trajectory(self):
        return self.args["trajectory"]

    def get_start(self):
        start_offset = self.args["start_offset"]
        if isinstance(start_offset, Physical):
            return start_offset
        else:
            print(
                "[Error] 'distance' parameter of PositionModifier must be 'Physical' type"
            )
            sys.exit(1)

    def get_end(self):
        end_offset = self.args["end_offset"]
        if isinstance(end_offset, Physical):
            return end_offset
        else:
            print(
                "[Error] 'distance' parameter of PositionModifier must be 'Physical' type"
            )
            sys.exit(1)


class DistanceModifier(Modifier):
    def __init__(self, actor_name: str, name: str) -> None:
        super().__init__(actor_name, name)

    def get_distance(self):
        if (
                self.args["distance"][0] != "["
                and self.args["distance"][-1] != "]"
        ):
            return int(float(self.args["distance"]))
        else:
            values = self.args["distance"][1:-1].split("..")
            start = int(float(values[0]))
            end = int(float(values[1]))
            value = random.randint(start, end)
            return value


class PhysicalMovementModifier(Modifier):
    def __init__(self, actor_name: str, name: str) -> None:
        super().__init__(actor_name, name)

    def get_option(self):
        return self.args["options"]


class AvoidCollisionsModifier(Modifier):
    def __init__(self, actor_name: str, name: str) -> None:
        super().__init__(actor_name, name)

    def get_bool(self):
        return self.args["bool"]

