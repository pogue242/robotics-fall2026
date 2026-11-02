# line_following

## comparison
For the practice attempt, the mean absolute error was 0.0876. It worked and detected the line well. 
On the curved track, the mask detected the magenta line in both attempts. With a gain of 0.08, the robot turned too slowly on the curves and often moved far from the center. The run took 187.38 seconds and had an average error of 0.4848. Increasing the gain to 0.30 created better steering commands and kept the line centered. The second run took 138.27 seconds, and its average error dropped to 0.1734. 

## limits
The main problem was in attempt 20261102T043232-2c8acbcd. The camera still detected the line, but the 0.08 gain was too low for the curves. This made the robot turn too slowly and move farther away from the center of the line. he mean error increased to 0.4848, and the run took 187.38 seconds. It needs to be able to do more than follow a line/labelled finish line.
