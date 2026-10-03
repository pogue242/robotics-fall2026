# Autosaved responses

- Name: Matteo Ferrantelli
- Student ID: (not provided)
- Section: (not provided)

## Check-in answers

### background_compare

The engineer decides how the PID controller should react based on the Kp, Ki, and Kd variables. They then have to tune them so the system reaches the target and responds with enough speed but not too aggressively. PID is a feedback controller because it keeps checking where the system is, compares that to the target, and adjusts based on the difference.

### background_social

If a drone is tuned too cautiously, it may not achieve any of its goals or objectives. It may deem the area it needs to fly too dangerous and may not find the optimal route. If it is too aggressive, it might make certain mistakes and not properly evaluate risk

### m3_prediction

Increasing the forward speed could make the robot harder to control, so it may have more tracking error and get closer to pedestrians than planned. Using too little derivative control could also cause more overshooting, which could reduce the clearance from pedestrians.

### m3_technical

It matched my prediction. I had to adjust the heading more than expected. The next route point becomes a heading command because that is not the target. If the wheel radius is estimated incorrectly, the robot can think it traveled farther or less than it really did.

### m3_human

The consequential failure is getting too close to a pedestrian.
I would require less clearance to speed up my robot. I trust my robot not to hit pedestrians. 
Responsibility belongs to those developing the robot. Don't ship a bad product.

## Mission explanations

### mission_3

**technical_analysis**: It matched my prediction. I had to adjust the heading more than expected. The next route point becomes a heading command because that is not the target. If the wheel radius is estimated incorrectly, the robot can think it traveled farther or less than it really did.

**human_centered_analysis**: The consequential failure is getting too close to a pedestrian.
I would require less clearance to speed up my robot. I trust my robot not to hit pedestrians. 
Responsibility belongs to those developing the robot. Don't ship a bad product.
