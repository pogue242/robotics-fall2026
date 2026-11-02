# pillar_search

## diagnosis
All attempts on blue were successful. For comparison, I changed the steering gain from 1.2 to 0.7 in attempt 20261102T040013-a554faf7 and compared it with attempt 20261102T025848-9a1dc5ae. In both attempts, the mask clearly selected the blue pillar, and the centroid started far to the left with an error close to -1. Because it is positive, it turned left. The 0.7 gain error stopped at about -0.03 while the 1.2 gain stopped at about 0.04. The two runs took 16.99 and 16.87 seconds, respectively. These are both within a margin of error of each other. 

## evidence
In attempt 20261102T040244-d00ce021, the robot centered red, green, turquoise, and blue successfully. The error graph has four separate sections, one for each color, where the error starts close to -1. Angular is 0 as the robot is at rest to detect the pillar. The final camera image and mask show blue because it was the last color in the sequence. This shows that the controller centered regions matching all four requested colors, but it does not prove those regions were actually the correct pillars because another object with the same color could pass the mask
