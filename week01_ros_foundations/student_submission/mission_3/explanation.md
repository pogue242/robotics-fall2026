# Mission 3

## Data To Command

Front_distance() determines which LiDAR measurements are in front of the robot and valid. The decide_velocity() function checks how far the obstacle is and, if it is far enough, then the robot can move. 

## Missing Data Safety

The robot stops because a missing measurement could mean the object is too close/it may not be safe to move. 

## System Layers

The command guard checks the commands supplied by the ROS node. The ROS node/obstacle guard uses the decision functions. 
