# Mission 2

## Measurement Explanation

The traveled path is the length of the actual curve the robot took, while the start-to-end is a straight line between the start and end points. 

## Modified Settings

{'linear_x': 0.12, 'angular_z': 0.6, 'duration': 4.0}

## Motion Comparison

All my predictions have greater displacement than the actual test. For the straight-line test, I predicted it would move .45 meters, but it only moved .309 meters. I believe this is because an actual simulation needs to accelerate and decelerate, so it is not moving at .15 m/s for 3 seconds. 

## Prediction Locks

{'curve': '2026-09-10T04:57:15.827979+00:00', 'curve_modified': '2026-09-10T05:00:46.706557+00:00', 'rotation': '2026-09-10T04:54:20.016575+00:00', 'straight': '2026-09-10T04:51:27.378821+00:00'}

## Predictions

{'curve': 'I predict the path will be an arc moving to the right because it will turn 1.6 radians to the right and have a total arc movement of .6 meters. However, It will not be .6 meters away from the starting point.', 'curve_modified': 'The curve will be tighter and turn the other way because radians are positive, so it is a left turn, and the turning speed is faster. ', 'rotation': 'The robot will turn 1.5 radians, or approximately 90 degrees.', 'straight': 'I predict the robot will be .45 meters ahead of its starting point. '}

## Safety Explanation

The command guard checks if each proposed movement is within the given speed limits and turning radii. The final zero command ends the robot's movement by bringing the velocity down to 0. The timeout command prevents a robot from continuing during a crash by sending a stop command after .5 seconds without an update. 
