# Mission 1

## Scan Observation

The /scan message contains distance measurements under ranges. The scan observed distances from about 0.9 to 3.1 meters, as well as many in values, which I think means the sensor did not detect a surface. 

## Guided Checks

{'node_list': True, 'guard_info': True, 'bridge_info': True, 'scan_info': True, 'scan_message': True, 'command_topics': True}

## Graph Explanation

An ROS 2 graph is a list of and connection etween various nodes running. For example, /course_cmd_vel_guard is a node that listens to /student_cmd_vel and sends commands out on /cmd_vel.

## Command Path Explanation

A proposed movement command goes through /student_cmd_vel. The guard checks it, then sends the command, if approved, to /cmd_vel to the robot.f

## Tools Explanation

Gazebo simulates the movement and physics of a robot. RViz visualizes sensor data.
