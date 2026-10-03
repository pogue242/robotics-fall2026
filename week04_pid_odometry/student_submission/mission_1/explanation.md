# mission_1 Submission

- Name: Matteo Ferrantelli
- Section: (not provided)

## Explanations

### prediction

With too little Kp, I expect that it won't be able to meet the target properly/too slowly. 
With too little Kd, I expect it will probably undershoot the target since it won't be able to control oscillations.

### tuning_analysis

I predicted that smaller kd and kp values would make the arm slower and undershoot the target. These were correct and adjusting the values allowed the arm to catch up faster. 
Gravity compensation helped the arm hold its position better, especially at the shoulder, because the controller did not have to fight gravity as much.