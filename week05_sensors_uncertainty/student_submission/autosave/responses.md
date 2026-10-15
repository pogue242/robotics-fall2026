# Week 5: Sensors, Noise, and Uncertainty

- course_id: 24416767
- email: matteo.ferrantelli67@login.cuny.edu
- name: Matteo Ferrantelli

## concepts.observation

Increasing noise spreads the distribution of measurements out, creating deeper troughs and higher peaks in the sample. Increasing bias skews the distribution to the right for positive values. The sample data distribution's median is to the right of the true value. 

## final.course_reflection

This lab made me think about how existing autonomous systems need to adapt to messy and inaccurate sensor data. Waymo needs to adjust for degraded LiDAR sensors in rain and snow and needs to rely on other sensors. It made me think about them shifting the weights of sensor inputs. The same applies to drones and even Roomba.  I also thought about how humans do something similar, since we don't always have perfect information about our surroundings and still have to react and adjust our movements. In a dark environment, hearing and touch may be more useful than sight. However, I didn't find this lab as engaging as the prior ones. Most of it involved changing settings and comparing numbers, and I think seeing more of a robot react to the different sensor errors would have made it more interesting.

## final.synthesis

The lab showed how sensor noise and bias can lead a robot off target, which means you need to adjust for a potentially faulty sensor. Even if the median sensor reading is on target, outliers like in Mission 1, where this exact example occurred, could lead a robot to the wrong decision if sensor delay is high or a quick decision is needed. 
In Mission 2, I experimented with moving average and median filters, along with sensor fusion. I expected larger windows to reduce the error, but window 3 had an RMSE of 0.136 compared to 0.1564 for window 11. Window 11 also had a shorter response delay, which I didn't expect. My selected median filter with a weight of 0.50 had the lowest RMSE of 0.1265. This showed how different estimation methods can affect both accuracy and responsiveness. Mission 3 was about deployment context, where the warehouse robot had a 1.23% false-safe rate, compared to 0% for the assistive robot. Even a low false-safe rate could be dangerous around workers or people relying on the robot

## mission_1.bias

0.02

## mission_1.bias_vs_variance

My prediction lines up with the statistics because the mean and median are close together and close to the truth, but the variance is high. Bias may not have high variance but is skewed from the true value. 

## mission_1.dropouts

2

## mission_1.mean

2.02

## mission_1.median

2.01

## mission_1.more_samples

Taking more samples could help get a more accurate average, but it would not completely fix the noise. More samples would give more credence to the median/average value, but we may get the same proportion of outliers

## mission_1.outliers

5

## mission_1.prediction

A biased sensor would have a more normal distribution, but would have the median skewed left or right, with clustering at those points. It is more likely for a noisy sensor to have a larger IQR.  This would result in a higher variance, but the average could still be close to the actual distance

## mission_1.prediction_draft

A biased sensor would have a more normal distribution, but would have the median skewed left or right, with clustering at those points. It is more likely for a noisy sensor to have a larger IQR.  This would result in a higher variance, but the average could still be close to the actual distance

## mission_1.profile

noisy

## mission_1.robot_consequence

If the robot bases its movement on outliers, it may attempt to move past the 2m obstacle and collide with whatever or whoever is in its path. 

## mission_1.variance

0.05

## mission_2.comparison

I expected the larger windows to be smoother but to have a longer delay. However, window 3 had the smallest RMSE value of only 0.136, while window 7 was at 0.1468 and window 11 had 0.1564. The delay was surprisingly higher for window 3 at 1.25 seconds compared to 1.1 seconds for both larger windows. The moving average and median were very similar for a window of 3 and a weight of .25. The moving average had an RMSE of 0.136, while the median had 0.1366, and both had a delay of 1.25 seconds. I was correct that relying more on sensor A/increasing its weight would increase error, but delay stayed the same.

## mission_2.fusion_choice

I think weight 0.50 with a window of 3 is the most preferable. All three had the same response delay of 1.25 seconds. All 3 had the same delay, so it is not a factor in the decision. Weight 0.25 had an RMSE of 0.1366, weight 0.50 had 0.1265, and weight 0.75 had 0.1335. 

## mission_2.manual_average

4.17

## mission_2.manual_fusion

2.25

## mission_2.manual_median

2.3

## mission_2.prediction_draft

Increasing the weight to .5 may reduce delay. However, Sensor A also has more noise and outliers, so giving it more weight could increase the effect of inaccurate readings.

## mission_2.responsiveness

A larger window doesn't always mean a longer delay. Even though the difference is only 0.15 seconds, it could matter if a fast object suddenly appeared in the robot's line of sight. A slower response could mean the robot doesn't stop in time

## mission_2.selected

0

## mission_3.Assistive.prediction_draft

May not stop enough and be too slow

## mission_3.Warehouse.prediction_draft

.75 performed better than .55, and lower window also performed better. Sensor A is noisy, so reducing its weight

## mission_3.context_comparison

My warehouse robot used a stopping threshold of 0.75 and a caution margin of 0.15, while the assistive robot used 0.85 and 0.30. The warehouse had a false-safe rate of about 1.23%, compared to 0% for the assistive robot. 1.23% is fairly high, and means the robot is contuing to unsafe conditions. 

## mission_3.error_costs

The workers/ones interacting with the robots bear the cost. My assistive baseline had a false-safe rate of 0 and an unnecessary-stop rate of 0.0135. The final policy kept the false-safe rate at 0 and reduced unnecessary stops to 0.

## mission_3.limitations

I think an important additional test/consideration would be interviewing workers on how they feel around it and if their behaviors change while the robot is around. 
