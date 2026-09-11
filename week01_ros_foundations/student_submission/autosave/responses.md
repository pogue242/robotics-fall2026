# Week 1: Discovering a Robot Through ROS 2

## Student

- Name: Matteo Ferrantelli
- Email: matteo.ferrantelli67@login.cuny.edu

## mission_1.command_path_explanation

A proposed movement command goes through /student_cmd_vel. The guard checks it, then sends the command, if approved, to /cmd_vel to the robot.f

## mission_1.graph_explanation

An ROS 2 graph is a list of and connection etween various nodes running. For example, /course_cmd_vel_guard is a node that listens to /student_cmd_vel and sends commands out on /cmd_vel.

## mission_1.guided_checks

{'bridge_info': True, 'command_topics': True, 'guard_info': True, 'node_list': True, 'scan_info': True, 'scan_message': True}

## mission_1.scan_observation

The /scan message contains distance measurements under ranges. The scan observed distances from about 0.9 to 3.1 meters, as well as many in values, which I think means the sensor did not detect a surface. 

## mission_1.tools_explanation

Gazebo simulates the movement and physics of a robot. RViz visualizes sensor data.

## mission_2.measurement_explanation

The traveled path is the length of the actual curve the robot took, while the start-to-end is a straight line between the start and end points. 

## mission_2.modified_settings

{'linear_x': 0.12, 'angular_z': 0.6, 'duration': 4.0}

## mission_2.motion_comparison

All my predictions have greater displacement than the actual test. For the straight-line test, I predicted it would move .45 meters, but it only moved .309 meters. I believe this is because an actual simulation needs to accelerate and decelerate, so it is not moving at .15 m/s for 3 seconds. 

## mission_2.prediction_locks

{'curve': '2026-09-10T04:57:15.827979+00:00', 'curve_modified': '2026-09-10T05:00:46.706557+00:00', 'rotation': '2026-09-10T04:54:20.016575+00:00', 'straight': '2026-09-10T04:51:27.378821+00:00'}

## mission_2.predictions

{'curve': 'I predict the path will be an arc moving to the right because it will turn 1.6 radians to the right and have a total arc movement of .6 meters. However, It will not be .6 meters away from the starting point.', 'curve_modified': 'The curve will be tighter and turn the other way because radians are positive, so it is a left turn, and the turning speed is faster. ', 'rotation': 'The robot will turn 1.5 radians, or approximately 90 degrees.', 'straight': 'I predict the robot will be .45 meters ahead of its starting point. '}

## mission_2.safety_explanation

The command guard checks if each proposed movement is within the given speed limits and turning radii. The final zero command ends the robot's movement by bringing the velocity down to 0. The timeout command prevents a robot from continuing during a crash by sending a stop command after .5 seconds without an update. 

## part_1.activity

{'sensor': {'normal': True, 'changed': True}, 'timing': {'normal': True, 'changed': True}, 'hardware': {'normal': True, 'changed': True}}

## part_2.activity

{'reactive': {'normal': True, 'changed': True}, 'behavior': {'normal': True, 'changed': True}, 'deliberative': {'normal': True, 'changed': True}, 'hybrid': {'normal': True, 'changed': True}, 'safety': {'normal': True, 'changed': True}}

## part_3.activity

{'middleware': {'single': True, 'multiple': True}, 'communication': {'topic': True, 'service': True}, 'failure': {'healthy': True, 'sensor': True, 'type': True, 'visualization': True}, 'inspection': {'nodes': True, 'node_info': True, 'topics': True, 'topic_info': True, 'echo': True, 'services': True, 'broken': True}}
