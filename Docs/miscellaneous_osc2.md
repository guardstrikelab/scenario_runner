# Project completion status of OSC2

## Domain Model

### Support of Actor Model

#### Vehicle Model

All Carla built-in models can be set

The list of model：

| Vehicle Model |            |           |             |                    |
| ------------- | ---------- | --------- | ----------- | ------------------ |
| Model3        | Mkz2017    | Carlacola | Rubicon     | TT                 |
| A2            | Etron      | Crossbike | GrandTourer | Firetruck          |
| Impala        | C3         | Century   | Charger2020 | Charger_police2020 |
| Ambulance     | Crown      | Mustang   | Omafiets    | Low_rider          |
| Ninja         | Mkz2020    | Coupe     | Coupe2020   | Sprinter           |
| Microlino     | Cooper_s   | Micra     | Patrol      | Patrol2021         |
| Leon          | Cybertruck | Prius     | Zx125       | T2                 |
| T22021        | Yzf        |           |             |                    |

How to use：

```
actor Model3
actor Rubicon
ego_vehicle: Model3
npc: Rubicon
```

#### Pedestrian Model

All Carla built-in pedestrian models can be set

Model：Walker01、Walker02……Walker48

How to use：

```
actor Walker01
person: Walker01
```



## Movement Actions

#### Action of vehicle and walker

Set the vehicle's color：

```
ego_vehicle.set_color(blue)
```

Set the starting position：

```
ego_vehicle.set_position(x:255.0m, y:-204.7m, z:0.0m, pitch:0.0rad, yaw:88.4rad, roll:0.0rad)
person.set_position(x:255.0m, y:-200.7m, z:0.0m, pitch:0.0rad, yaw:88.4rad, roll:0.0rad)
```



#### Environment Actions

Set humidity, parameter value range 0～100：

```
actor Environment
modifier Environment.air
environment : Environment
environment.air(80)
```

Set cloud, parameter value range 0 to 8：

```
actor Environment
modifier Environment.clouds
environment : Environment
environment.clouds(8)
```

Rain：

```
actor Environment
modifier Environment.rain
environment : Environment
environment.rain(20mmph)
```

Wind;

```
actor Environment
modifier Environment.wind
environment : Environment
environment.wind(40mps)
```

Fog：

```
actor Environment
modifier Environment.fog
environment : Environment
environment.fog(5m)
```

> [!CAUTION]
>
> In OpenScenario2, the definition of fog has only one parameter  (Visibility distance), while in CARLA, there are three parameters for fog settings, and here only the Fog_distance is used.



To set day or night, the first parameter selects the celestial body (sun or  moon), the second parameter is the azimuth angle, and the third parameter is the  elevation angle：

```
actor Environment
modifier Environment.assign_celestial_position
environment : Environment
environment.assign_celestial_position(moon, 45deg, 90deg) #night
```



#### Action of Path

Set the map for the scenario：

```
actor Path
modifier Path.set_map
Path.set_map("Town04")
```

> [!CAUTION]
>
> Despite the definition of many path-related actions in the project, only the `set_map` action truly implements functionality.



## Movement Modifiers

Currently implemented movement modifiers：

| Movement Modifiers | Definition                                                   | Usage                                                        | How to use                                                   |
| ------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| speed              | Currently, it is only used to determine the speed of object movement. | speed(speed: speed)                                          | speed(20kph)                                                 |
| position           | Determine the position of an actor at a certain time         | position(distance: length\|time: time,<br /> [ahead_of: physical_object \| behind: physical_object] | position(15m, behind: ego_vehicle, at: start)                |
| lane               | Determine the lane based on other actor                      | lane(lane: uint, <br />side_of: physical_object, <br />side: side_left_right <br />[, standard-movement-parameters]) | lane(1, at: start)<br />lane(right_of: ego_vehicle, at: start) |
| acceleration       | Determine the acceleration and proceed to accelerate         | acceleration(acceleration: acceleration)                     | acceleration(15kphps)                                        |
| keep_lane          | Keep the actor in the current lane                           | keep_lane()                                                  | keep_lane()                                                  |
| change_speed       | Change the speed, either increase or decrease                | change_speed(speed: speed)                                   | change_speed(3kph)                                           |
| change_lane        | Change lanes to the left or right                            | change_lane(lane: int, side: side_left_right)                | change_lane(lane_changes:[1..2], side: left)                 |
| keep_position      | Maintain the position unchanged within a specified time.     | keep_position()                                              | keep_position()                                              |
| keep_speed         | Maintain the speed constant within a specified time          | keep_speed()                                                 | keep_speed()                                                 |
| lateral            | Determine the lateral distance based on other actor          | lateral(distance: length, side_of: vehicle, side: side_left_right) | lateral(3m, right_of: ego_vehicle)                           |
| distance           | Determine the distance the actor need move                   | distance(distance: length)                                   | distance(50m)                                                |



These have been written in the project, but they cannot be clearly displayed in the scenario：

| Movement Modifiers | Definition                                           | Usage                                                        | How to use                                         |
| ------------------ | ---------------------------------------------------- | ------------------------------------------------------------ | -------------------------------------------------- |
| yaw                | Determine the yaw angle                              | yaw(angle: angle )<br />yaw(angle: angle, relative_to: physical_object) | yaw(angle: 10deg)                                  |
| orientation        | Determine the yaw, pitch, and roll angles            | orientation(yaw: angle  [, pitch: angle] [, roll: angle]     | orientation(yaw: 10deg, pitch: 10deg, roll: 10deg) |
| physical_movement  | Determine whether the object has physical properties | physical_movement(option: movement_options)                  | physical_movement(must_be_physical)                |
| avoid_collisions   | Is collision allowed                                 | avoid_collisions(avoid: bool)                                | avoid_collisions(true)                             |



Unimplemented movement modifiers：

| Movement Modifiers | Definition                         | How to use                                                   |
| ------------------ | ---------------------------------- | ------------------------------------------------------------ |
| along              | Move along the specific path       | along(route: route <br />[, start_offset: length] [, end_offset: length]<br /> [, <standard-movement-parameters>]) |
| along_trajectory   | Move along the specific trajectory | along_trajectory(trajectory: trajectory <br />[, start_offset: length] [, end_offset: length] <br />[, <standard-movement-parameters>]) |



## Behavioral Model

Not implemented

## Abstract Road Network And Map

Not implemented