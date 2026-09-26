"""AI-assisted motion pattern implementation.

Preserve the original AI response in Streamlit. Review it, then implement a safe
version here. The node accepts only segments returned by ``build_pattern``.
"""

from __future__ import annotations

import math
from dataclasses import dataclass


@dataclass(frozen=True)
class Segment:
    linear_x: float
    angular_z: float
    duration: float


def build_pattern(pattern_name: str) -> list[Segment]:
    """Return ordered, bounded motion segments for the assigned pattern."""

    if pattern_name != "alternating_arcs":
        raise ValueError(f"Unknown pattern: {pattern_name}")

    forward_speed = 0.08
    radius = 0.30
    turn_angle = math.pi / 4

    # R = v / |omega|
    angular_speed = forward_speed / radius

    # theta = omega * t
    arc_duration = turn_angle / angular_speed

    turn_signs = (1, -1, 1, -1)

    return [
        Segment(
            linear_x=forward_speed,
            angular_z=sign * angular_speed,
            duration=arc_duration,
        )
        for sign in turn_signs
    ]