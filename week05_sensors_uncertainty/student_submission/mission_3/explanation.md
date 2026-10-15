# Mission 3

## Assistive.prediction_draft

May not stop enough and be too slow

## Warehouse.prediction_draft

.75 performed better than .55, and lower window also performed better. Sensor A is noisy, so reducing its weight

## context_comparison

My warehouse robot used a stopping threshold of 0.75 and a caution margin of 0.15, while the assistive robot used 0.85 and 0.30. The warehouse had a false-safe rate of about 1.23%, compared to 0% for the assistive robot. 1.23% is fairly high, and means the robot is contuing to unsafe conditions. 

## error_costs

The workers/ones interacting with the robots bear the cost. My assistive baseline had a false-safe rate of 0 and an unnecessary-stop rate of 0.0135. The final policy kept the false-safe rate at 0 and reduced unnecessary stops to 0.

## limitations

I think an important additional test/consideration would be interviewing workers on how they feel around it and if their behaviors change while the robot is around. 
