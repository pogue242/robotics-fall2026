# Lab 7 saved answers

## mission_1.diagnosis
The only real failure/incorrect detection was occluded_1 and _2, which resulted in the mask of the mug being broken up, and selecting the laptop edge instead. Normal_1, dim_1, glare_1, cluttered_1, and far_1 all were successful, but the first two included a significant portion of the cup's shadow, while far did not fully box the handle.


## mission_1.limitations
I changed the value/brightness parameter. I tried a few settings, and when it got below 70, it consistently and erroneously detected the laptop edge, rather than the cup. However, higher brightness levels caused it to fail the dim image test


## mission_2.comparison
The classical detector performed better on normal and dim. For both conditions, it had 2 correct boxes, no false boxes, and no missed mugs. The learned detector had 1 correct box and 1 missed mug for normal, and missed both mugs for dim, with no false boxes in either condition. Both detectors failed occluded and missed both mugs, but the classical detector also had 2 false boxes because it selected other masks.

## mission_2.choice
Classical, including the upper value/brightness limit of 70. It detected the mugs in normal and dim modes that the learned detector missed. I would also try lowering the learned detector’s threshold to see whether it finds more cups. The normal_1 foreground mask had an IoU of 0.5756 and Dice of 0.7306., but missed the handle frequently. The mask identifies foreground regions, not specifically a mug. The limitation is that the small sample size and using only one cup are not transferable to wider cup designs.

## pillar_search.diagnosis
All attempts on blue were successful. For comparison, I changed the steering gain from 1.2 to 0.7 in attempt 20261102T040013-a554faf7 and compared it with attempt 20261102T025848-9a1dc5ae. In both attempts, the mask clearly selected the blue pillar, and the centroid started far to the left with an error close to -1. Because it is positive, it turned left. The 0.7 gain error stopped at about -0.03 while the 1.2 gain stopped at about 0.04. The two runs took 16.99 and 16.87 seconds, respectively. These are both within a margin of error of each other. 

## pillar_search.evidence
In attempt 20261102T040244-d00ce021, the robot centered red, green, turquoise, and blue successfully. The error graph has four separate sections, one for each color, where the error starts close to -1. Angular is 0 as the robot is at rest to detect the pillar. The final camera image and mask show blue because it was the last color in the sequence. This shows that the controller centered regions matching all four requested colors, but it does not prove those regions were actually the correct pillars because another object with the same color could pass the mask

## line_following.comparison
For the practice attempt, the mean absolute error was 0.0876. It worked and detected the line well. 
On the curved track, the mask detected the magenta line in both attempts. With a gain of 0.08, the robot turned too slowly on the curves and often moved far from the center. The run took 187.38 seconds and had an average error of 0.4848. Increasing the gain to 0.30 created better steering commands and kept the line centered. The second run took 138.27 seconds, and its average error dropped to 0.1734. 

## line_following.limits
The main problem was in attempt 20261102T043232-2c8acbcd. The camera still detected the line, but the 0.08 gain was too low for the curves. This made the robot turn too slowly and move farther away from the center of the line. he mean error increased to 0.4848, and the run took 187.38 seconds. It needs to be able to do more than follow a line/labelled finish line.

## final.synthesis
The missions taught me that correctly detecting and understanding visual evidence, while extremely difficult in its own right, does not always lead to ideal behavior, as the fundamentals of movement from other labs also apply. In Mission 1, the classical detector worked on the normal and dim mug images, but occlusion broke up the mug’s contours and caused it to select the laptop edge. In Mission 2, the robot centered red, green, turquoise, and blue, but the masks only showed color and position. In Mission 3, the robot detected the line with both settings, but changing the movement controller yielded significantly better results. 

## final.course_reflection
This lab felt like an intro to the micro mouse challenge. It would be fun to have a lab/challenge to create a single controller and visual detection system to perform on a set of unknown obstacles and courses. 
