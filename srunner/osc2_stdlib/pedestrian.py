import carla
import srunner.osc2_stdlib.misc_object as misc
import srunner.scenariomanager.carla_data_provider as carla_provider
from srunner.tools.osc2_helper import OSC2Helper

class Pedestrian:

    def __init__(self) -> None:
        self.model = 'walker.pedestrians.*'
        self.rolename = 'hero'
        self.gender = "woman"
        self.age = None
        self.speed = 0
        self.color = None
        self.generation = 0
        self.category = 'pedestrian'
        self.is_invincible = False
        self.transform = carla.Transform()  # initial position
        self.random_location = True
        self.autopilot = False
        self.args = dict()

    def set_model(self, model: str) -> None:
        self.model = model

    def set_name(self, name: str) -> None:
        self.rolename = name

    def get_name(self) -> str:
        return self.rolename

    def set_gender(self, gender: str) -> None:
        self.gender = gender

    def set_speed(self, speed: float) -> None:
        self.speed = speed

    def set_isvincible(self, is_invincible: bool) -> None:
        self.is_invincible = is_invincible

    def set_age(self, age: str) -> None:
        self.age = age

    def set_arg(self, kw):
        self.args.update(kw)

    def get_arg(self, key):
        return self.args[key]

    def set_position(self, pos: misc.Position) -> None:
        self.position = pos
        # convert position to transform，reference convert_position_to_transform function
        if type(pos) is misc.WorldPosition:
            x = float(pos.x)
            y = float(pos.y)
            z = float(pos.z)
            # yaw = math.degrees(float(pos.h))
            # pitch = math.degrees(float(pos.p))
            # roll = math.degrees(float(pos.r))
            yaw = float(pos.yaw)
            pitch = float(pos.pitch)
            roll = float(pos.roll)
            # if not OpenScenarioParser.use_carla_coordinate_system:
            #     y = y * (-1.0)
            #     yaw = yaw * (-1.0)
            self.transform = carla.Transform(
                carla.Location(x=x, y=y, z=z),
                carla.Rotation(yaw=yaw, pitch=pitch, roll=roll),
            )
        elif type(pos) is misc.LanePosition:
            pass
        else:
            print("no implement position type")


class Walker(Pedestrian):
    def __init__(self) -> None:
        super().__init__()


class Walker01(Walker):
    def __init__(self) -> None:
        super().__init__()
        self.set_model("walker.pedestrian.0001")


class Walker02(Walker):
    def __init__(self) -> None:
        super().__init__()
        self.set_model("walker.pedestrian.0002")


class Walker03(Walker):
    def __init__(self) -> None:
        super().__init__()
        self.set_model("walker.pedestrian.0003")


class Walker04(Walker):
    def __init__(self) -> None:
        super().__init__()
        self.set_model("walker.pedestrian.0004")


class Walker05(Walker):
    def __init__(self) -> None:
        super().__init__()
        self.set_model("walker.pedestrian.0005")


class Walker06(Walker):
    def __init__(self) -> None:
        super().__init__()
        self.set_model("walker.pedestrian.0006")


class Walker07(Walker):
    def __init__(self) -> None:
        super().__init__()
        self.set_model("walker.pedestrian.0007")


class Walker08(Walker):
    def __init__(self) -> None:
        super().__init__()
        self.set_model("walker.pedestrian.0008")


class Walker09(Walker):
    def __init__(self) -> None:
        super().__init__()
        self.set_model("walker.pedestrian.0009")


class Walker10(Walker):
    def __init__(self) -> None:
        super().__init__()
        self.set_model("walker.pedestrian.0010")


class Walker11(Walker):
    def __init__(self) -> None:
        super().__init__()
        self.set_model("walker.pedestrian.0011")


class Walker12(Walker):
    def __init__(self) -> None:
        super().__init__()
        self.set_model("walker.pedestrian.0012")


class Walker13(Walker):
    def __init__(self) -> None:
        super().__init__()
        self.set_model("walker.pedestrian.0013")


class Walker14(Walker):
    def __init__(self) -> None:
        super().__init__()
        self.set_model("walker.pedestrian.0014")


class Walker15(Walker):
    def __init__(self) -> None:
        super().__init__()
        self.set_model("walker.pedestrian.0015")


class Walker16(Walker):
    def __init__(self) -> None:
        super().__init__()
        self.set_model("walker.pedestrian.0016")


class Walker17(Walker):
    def __init__(self) -> None:
        super().__init__()
        self.set_model("walker.pedestrian.0017")


class Walker18(Walker):
    def __init__(self) -> None:
        super().__init__()
        self.set_model("walker.pedestrian.0018")


class Walker19(Walker):
    def __init__(self) -> None:
        super().__init__()
        self.set_model("walker.pedestrian.0019")


class Walker20(Walker):
    def __init__(self) -> None:
        super().__init__()
        self.set_model("walker.pedestrian.0020")


class Walker21(Walker):
    def __init__(self) -> None:
        super().__init__()
        self.set_model("walker.pedestrian.0021")


class Walker22(Walker):
    def __init__(self) -> None:
        super().__init__()
        self.set_model("walker.pedestrian.0022")


class Walker23(Walker):
    def __init__(self) -> None:
        super().__init__()
        self.set_model("walker.pedestrian.0023")


class Walker24(Walker):
    def __init__(self) -> None:
        super().__init__()
        self.set_model("walker.pedestrian.0024")


class Walker25(Walker):
    def __init__(self) -> None:
        super().__init__()
        self.set_model("walker.pedestrian.0025")


class Walker26(Walker):
    def __init__(self) -> None:
        super().__init__()
        self.set_model("walker.pedestrian.0026")


class Walker27(Walker):
    def __init__(self) -> None:
        super().__init__()
        self.set_model("walker.pedestrian.0027")


class Walker28(Walker):
    def __init__(self) -> None:
        super().__init__()
        self.set_model("walker.pedestrian.0028")


class Walker29(Walker):
    def __init__(self) -> None:
        super().__init__()
        self.set_model("walker.pedestrian.0029")


class Walker30(Walker):
    def __init__(self) -> None:
        super().__init__()
        self.set_model("walker.pedestrian.0030")


class Walker31(Walker):
    def __init__(self) -> None:
        super().__init__()
        self.set_model("walker.pedestrian.0031")


class Walker32(Walker):
    def __init__(self) -> None:
        super().__init__()
        self.set_model("walker.pedestrian.0032")


class Walker33(Walker):
    def __init__(self) -> None:
        super().__init__()
        self.set_model("walker.pedestrian.0033")


class Walker34(Walker):
    def __init__(self) -> None:
        super().__init__()
        self.set_model("walker.pedestrian.0034")


class Walker35(Walker):
    def __init__(self) -> None:
        super().__init__()
        self.set_model("walker.pedestrian.0035")


class Walker36(Walker):
    def __init__(self) -> None:
        super().__init__()
        self.set_model("walker.pedestrian.0036")


class Walker37(Walker):
    def __init__(self) -> None:
        super().__init__()
        self.set_model("walker.pedestrian.0037")


class Walker38(Walker):
    def __init__(self) -> None:
        super().__init__()
        self.set_model("walker.pedestrian.0038")


class Walker39(Walker):
    def __init__(self) -> None:
        super().__init__()
        self.set_model("walker.pedestrian.0039")


class Walker40(Walker):
    def __init__(self) -> None:
        super().__init__()
        self.set_model("walker.pedestrian.0040")


class Walker41(Walker):
    def __init__(self) -> None:
        super().__init__()
        self.set_model("walker.pedestrian.0041")


class Walker42(Walker):
    def __init__(self) -> None:
        super().__init__()
        self.set_model("walker.pedestrian.0042")


class Walker43(Walker):
    def __init__(self) -> None:
        super().__init__()
        self.set_model("walker.pedestrian.0043")


class Walker44(Walker):
    def __init__(self) -> None:
        super().__init__()
        self.set_model("walker.pedestrian.0044")


class Walker45(Walker):
    def __init__(self) -> None:
        super().__init__()
        self.set_model("walker.pedestrian.0045")


class Walker46(Walker):
    def __init__(self) -> None:
        super().__init__()
        self.set_model("walker.pedestrian.0046")


class Walker47(Walker):
    def __init__(self) -> None:
        super().__init__()
        self.set_model("walker.pedestrian.0047")


class Walker48(Walker):
    def __init__(self) -> None:
        super().__init__()
        self.set_model("walker.pedestrian.0048")