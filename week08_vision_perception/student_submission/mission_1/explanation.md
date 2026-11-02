# mission_1

## diagnosis
The only real failure/incorrect detection was occluded_1 and _2, which resulted in the mask of the mug being broken up, and selecting the laptop edge instead. Normal_1, dim_1, glare_1, cluttered_1, and far_1 all were successful, but the first two included a significant portion of the cup's shadow, while far did not fully box the handle.


## limitations
I changed the value/brightness parameter. I tried a few settings, and when it got below 70, it consistently and erroneously detected the laptop edge, rather than the cup. However, higher brightness levels caused it to fail the dim image test

