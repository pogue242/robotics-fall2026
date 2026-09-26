# Mission 3

## Specification

The robot will do four arcs with a radius of 0.30 m. There will be two sets of turns, both being +45° and then -45°. I will use a forward speed of 0.12 m/s and angular speeds of +0.40 or -0.40 rad/s, which gives the required 0.30 m radius. After the fourth arc, the robot should stop and finish facing the same direction it started.

## Saved Specification

The robot will do four arcs with a radius of 0.30 m. There will be two sets of turns, both being +45° and then -45°. I will use a forward speed of 0.12 m/s and angular speeds of +0.40 or -0.40 rad/s, which gives the required 0.30 m radius. After the fourth arc, the robot should stop and finish facing the same direction it started.

## Assigned Pattern

alternating_arcs

## Original Prompt

This is a ROS 2 Jazzy Python package. Implement only build_pattern(pattern_name: str) -> list[Segment] for alternating_arcs in the existing pattern.py.

The robot must perform four forward arcs of radius 0.30 meters, turning +45°, -45°, +45°, -45°, and finish facing its initial direction.

Use a forward speed of 0.12 m/s and angular speeds of +0.40 and -0.40 rad/s. Calculate the appropriate duration for each arc.

The course-provided pattern_node.py calls this function, repeatedly sends the returned segments through /student_cmd_vel, and sends the final stop command.

Use the existing Segment class with linear_x (m/s), angular_z (rad/s), and duration (s).

Return the ordered segments and raise ValueError for an unknown pattern name.

Stay within 0.22 m/s, 0.80 rad/s, 30 seconds per segment, and 60 seconds total.

Do not replace the wrapper or course checks. Explain your assumptions and propose tests.

## Original Output

Each arc must turn exactly \(45^\circ=\pi/4\) radians. With angular speed magnitude \(0.40\ \text{rad/s}\),

\[
t=\frac{\Delta\theta}{|\omega|}
=\frac{\pi/4}{0.40}
=\frac{\pi}{1.6}
\approx 1.9635\text{ s}.
\]

The specified linear and angular speeds are also consistent with the requested radius:

\[
r=\frac{v}{|\omega|}=\frac{0.12}{0.40}=0.30\text{ m}.
\]

So `build_pattern` can be implemented as:

```python
import math

def build_pattern(pattern_name: str) -> list[Segment]:
    if pattern_name != "alternating_arcs":
        raise ValueError(f"Unknown pattern: {pattern_name}")

    arc_duration = (math.pi / 4.0) / 0.40

    return [
        Segment(linear_x=0.12, angular_z=+0.40, duration=arc_duration),
        Segment(linear_x=0.12, angular_z=-0.40, duration=arc_duration),
        Segment(linear_x=0.12, angular_z=+0.40, duration=arc_duration),
        Segment(linear_x=0.12, angular_z=-0.40, duration=arc_duration),
    ]
```

### Assumptions

I would **not add a stop segment**. The course-provided `pattern_node.py` is responsible for sending the final zero-velocity command, so `build_pattern()` should return only the four requested motion segments.

Each segment lasts approximately **1.9635 s**, giving a total commanded motion time of approximately **7.854 s**. The net heading change is

\[
45^\circ-45^\circ+45^\circ-45^\circ=0^\circ,
\]

so the robot finishes facing its initial direction. Note that this means **same orientation, not necessarily the same position**.

All limits are satisfied: `0.12 < 0.22 m/s`, `0.40 < 0.80 rad/s`, each segment is well under 30 s, and the total is well under 60 s.

### Tests I would add

Assuming `pytest`, the important checks are:

```python
import math
import pytest

def test_alternating_arcs():
    segments = build_pattern("alternating_arcs")

    assert len(segments) == 4

    expected_duration = (math.pi / 4.0) / 0.40

    expected_angular = [0.40, -0.40, 0.40, -0.40]

    for segment, angular_z in zip(segments, expected_angular):
        assert segment.linear_x == pytest.approx(0.12)
        assert segment.angular_z == pytest.approx(angular_z)
        assert segment.duration == pytest.approx(expected_duration)

    # Requested radius: r = v / |omega|
    for segment in segments:
        assert segment.linear_x / abs(segment.angular_z) == pytest.approx(0.30)

    # Net heading change should be zero.
    heading_change = sum(s.angular_z * s.duration for s in segments)
    assert heading_change == pytest.approx(0.0)

    # Safety/course constraints.
    assert all(abs(s.linear_x) <= 0.22 for s in segments)
    assert all(abs(s.angular_z) <= 0.80 for s in segments)
    assert all(s.duration <= 30.0 for s in segments)
    assert sum(s.duration for s in segments) <= 60.0


def test_unknown_pattern():
    with pytest.raises(ValueError):
        build_pattern("not_a_pattern")
```

One detail worth preserving is whatever constructor/signature the existing `Segment` class actually uses. If `pattern.py` already imports `math` or constructs `Segment` positionally, follow the existing file's conventions rather than modifying unrelated code.

## Original Source

import math


def build_pattern(pattern_name: str) -> list[Segment]:
    if pattern_name != "alternating_arcs":
        raise ValueError(f"Unknown pattern: {pattern_name}")

    # Each arc turns 45 degrees (pi/4 radians).
    # duration = angle / angular speed
    arc_duration = (math.pi / 4.0) / 0.40

    return [
        Segment(
            linear_x=0.12,
            angular_z=0.40,
            duration=arc_duration
        ),
        Segment(
            linear_x=0.12,
            angular_z=-0.40,
            duration=arc_duration
        ),
        Segment(
            linear_x=0.12,
            angular_z=0.40,
            duration=arc_duration
        ),
        Segment(
            linear_x=0.12,
            angular_z=-0.40,
            duration=arc_duration
        ),
    ]

## Assumptions

The AI assumed forward speed was in m/s, angular speed was in rad/s, and positive velocity meant going left (basic assumptions). It also assumed the segment class would be used.

## Problems

I found no initial errors (only after live testing).
I eventually identified that the forward speed was too fast and was the reason for the initial tests failing the Live motion and stop test. It was originally .12m/s, but I changed it to 0.08m/s and it passed. 

## Test Plan

The velocity-limit test checks that forward speed stays below 0.22 m/s and angular speed stays at or below 0.80 rad/s. The stop test checks that the command after the 4 repeating arcs is zero

## Modifications

Dropped the forward speed from 0.12m/s to 0.08m/s. Changed the angular speed calculation. Removed and revised the segments blocks. 

## Live Pending

False

## Evidence Analysis

The tests show that the program creates the four arcs correctly, stays within the speed limits, and stops after the pattern. The live test showed that the robot could perform the correct pattern in Gazebo. These results do not prove that the robot will behave correctly under different conditions. An additional useful test would be to start the robot at several randomized positions. 

## Ai Disclosure

I used GPT 5.6 Sol. I had a chat in the same project as the prior lab, both with general information about the lab.

## Live Issue


