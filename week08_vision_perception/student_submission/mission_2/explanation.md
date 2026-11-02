# mission_2

## comparison
The classical detector performed better on normal and dim. For both conditions, it had 2 correct boxes, no false boxes, and no missed mugs. The learned detector had 1 correct box and 1 missed mug for normal, and missed both mugs for dim, with no false boxes in either condition. Both detectors failed occluded and missed both mugs, but the classical detector also had 2 false boxes because it selected other masks.

## choice
Classical, including the upper value/brightness limit of 70. It detected the mugs in normal and dim modes that the learned detector missed. I would also try lowering the learned detector’s threshold to see whether it finds more cups. The normal_1 foreground mask had an IoU of 0.5756 and Dice of 0.7306., but missed the handle frequently. The mask identifies foreground regions, not specifically a mug. The limitation is that the small sample size and using only one cup are not transferable to wider cup designs.
