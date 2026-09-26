
"""Transform a hallway-camera point into the robot's coordinate frame."""

from geometry_msgs.msg import PointStamped
from tf2_ros import TransformException
import tf2_geometry_msgs


def transform_camera_point(
    tf_buffer,
    point: PointStamped,
) -> PointStamped | None:

    # Make sure the point comes from the correct camera.
    if point.header.frame_id != "hall_camera":
        raise ValueError("Expected a point from hall_camera")

    # Transform the point into the robot's coordinate frame.
    # TF2 uses the timestamp stored in the point's header.
    try:
        return tf_buffer.transform(point, "base_link")

    # Return None if the required transform is unavailable.
    except TransformException:
        return None
