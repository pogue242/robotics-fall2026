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