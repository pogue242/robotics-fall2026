# Mission 2

## comparison

I expected the larger windows to be smoother but to have a longer delay. However, window 3 had the smallest RMSE value of only 0.136, while window 7 was at 0.1468 and window 11 had 0.1564. The delay was surprisingly higher for window 3 at 1.25 seconds compared to 1.1 seconds for both larger windows. The moving average and median were very similar for a window of 3 and a weight of .25. The moving average had an RMSE of 0.136, while the median had 0.1366, and both had a delay of 1.25 seconds. I was correct that relying more on sensor A/increasing its weight would increase error, but delay stayed the same.

## fusion_choice

I think weight 0.50 with a window of 3 is the most preferable. All three had the same response delay of 1.25 seconds. All 3 had the same delay, so it is not a factor in the decision. Weight 0.25 had an RMSE of 0.1366, weight 0.50 had 0.1265, and weight 0.75 had 0.1335. 

## manual_average

4.17

## manual_fusion

2.25

## manual_median

2.3

## prediction_draft

Increasing the weight to .5 may reduce delay. However, Sensor A also has more noise and outliers, so giving it more weight could increase the effect of inaccurate readings.

## responsiveness

A larger window doesn't always mean a longer delay. Even though the difference is only 0.15 seconds, it could matter if a fast object suddenly appeared in the robot's line of sight. A slower response could mean the robot doesn't stop in time

## selected

0
