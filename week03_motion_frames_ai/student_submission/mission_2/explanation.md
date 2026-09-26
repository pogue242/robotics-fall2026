# Mission 2

## Snapshot

{'schema_version': 2, 'captured_at': '2026-09-24T02:14:15.290065+00:00', 'frames': ['odom', 'base_link', 'base_scan', 'rear_camera_link', 'hall_camera'], 'frame_chain': ['hall_camera', 'odom', 'base_link', 'base_scan', 'rear_camera_link'], 'transforms': {'base_scan_to_base_link': {'translation': {'x': -0.032, 'y': 0.0, 'z': 0.172}, 'yaw': 0.0}, 'rear_camera_to_base_link': {'translation': {'x': -0.18, 'y': 0.0, 'z': 0.22}, 'yaw': -3.1415926535795866}, 'hall_camera_to_base_link': {'translation': {'x': -9.599863141042569e-09, 'y': -2.0, 'z': 1.19}, 'yaw': 1.5707963268004614}}, 'point_prompts': {'hall_camera_point': 'Transform point (0.5, 0.0, 0.0) from hall_camera to base_link.'}, 'transformed_points': {'scan_point_in_base': {'x': 0.968, 'y': 0.0}, 'rear_camera_point_in_base': {'x': -1.18, 'y': -1.0206624774663903e-11}, 'hall_camera_point_in_base': {'x': -9.602645551370715e-09, 'y': -1.5}}, 'source': 'live'}

## Frame Context

The rear camera is attached to the robot, so its relative position always stays the same. The hallway camera is fixed to one point in space, so as the robot moves, the relative position changes. 

## Initial Prompt

Write ROS 2 Python code that converts a point detected by the hallway camera into the robot's base_link frame.
(I did not add anything or upload any files, as intended by this lab)

## Initial Output

ROS 2: Transform a camera point into base_link
In ROS 2, use tf2 to transform a detected 3D point from the hallway camera's coordinate frame into the robot's base_link frame.
The example below assumes that:
- The hallway camera publishes detected 3D points as geometry_msgs/msg/PointStamped.
- The point's header.frame_id identifies the camera's coordinate frame, such as hallway_camera_optical_frame.
- The TF tree contains a valid transform between the hallway camera and the robot's base_link frame.
- The point is expressed in metres, not image pixel coordinates.
Because the hallway camera may be stationary while the robot moves, the code uses the point's detection timestamp to obtain the robot's pose at the time of detection, rather than its current pose.
1. Python node
The node subscribes to /hallway_camera/detected_point, transforms each incoming point into base_link, and publishes the result on /detected_point/base_link.
#!/usr/bin/env python3import rclpyfrom rclpy.node import Nodefrom rclpy.duration import Durationfrom geometry_msgs.msg import PointStampedfrom tf2_ros import (    Buffer,    TransformListener,    TransformException,)# Registers geometry_msgs transformations with tf2.import tf2_geometry_msgsclass CameraPointTransformer(Node):    def __init__(self):        super().__init__('camera_point_transformer')        # TF2 buffer and listener.        self.tf_buffer = Buffer()        self.tf_listener = TransformListener(            self.tf_buffer,            self        )        # Subscribe to detected points in the camera frame.        self.subscription = self.create_subscription(            PointStamped,            '/hallway_camera/detected_point',            self.point_callback,            10        )        # Publish transformed points in the robot frame.        self.publisher = self.create_publisher(            PointStamped,            '/detected_point/base_link',            10        )        self.get_logger().info(            'Camera point transformer started.'        )    def point_callback(self, camera_point: PointStamped):        if not camera_point.header.frame_id:            self.get_logger().warn(                'Received a point without a source frame.'            )            return        try:            # Transform the point into base_link.            #            # TF2 uses:            #   - camera_point.header.frame_id as the source            #   - camera_point.header.stamp as the transform time            #   - base_link as the target frame            #            # The timeout allows TF2 to wait briefly for            # the required transform.            base_point = self.tf_buffer.transform(                camera_point,                'base_link',                timeout=Duration(seconds=0.1)            )            # Publish the transformed point.            self.publisher.publish(base_point)            self.get_logger().info(                f'Point in base_link: '                f'x={base_point.point.x:.3f}, '                f'y={base_point.point.y:.3f}, '                f'z={base_point.point.z:.3f}'            )        except TransformException as ex:            self.get_logger().warn(                f'Could not transform camera point: {ex}'            )def main(args=None):    rclpy.init(args=args)    node = CameraPointTransformer()    try:        rclpy.spin(node)    except KeyboardInterrupt:        pass    finally:        node.destroy_node()        rclpy.shutdown()if __name__ == '__main__':    main()
The key operation is self.tf_buffer.transform(camera_point, 'base_link'). TF2 handles the translation and rotation between coordinate frames, including intermediate frames in the TF tree. 
GitHub
+1
2. Expected TF tree
For a hallway-mounted camera observing a mobile robot, a typical TF tree is:
map
Global reference frame
Robot localization
odom
Robot odometry
base_link
Robot frame
hallway_camera_link
Camera mounting frame
hallway_camera_optical_frame
Point source frame
The camera must be calibrated relative to the map or another shared reference frame, and the robot must publish its own pose within that reference system.
If the camera is physically mounted on the robot instead, the TF tree can be simpler:
base_link
    |
    +-- hallway_camera_link
                |
                +-- hallway_camera_optical_frame
In either configuration, the incoming point must specify the coordinate frame in which its coordinates were actually measured.
3. Example input
Suppose the hallway camera detects an object at the following coordinates:
camera_point = PointStamped()camera_point.header.frame_id = (    'hallway_camera_optical_frame')camera_point.header.stamp = (    self.get_clock().now().to_msg())camera_point.point.x = 0.5camera_point.point.y = 0.2camera_point.point.z = 2.0
These coordinates are expressed in the camera's optical frame, in metres.
For a standard ROS optical frame, positive X points right, positive Y points down, and positive Z points forward.
The transformed output might be:
header:
  frame_id: base_link

point:
  x: 1.25
  y: -0.40
  z: 0.85
These output coordinates are illustrative. The actual values depend on the hallway camera's extrinsic calibration and the robot's pose at the detection timestamp.
4. Important implementation details
Timestamp synchronization: Use the timestamp of the camera measurement, not the time at which the subscriber callback runs. This matters when the robot is moving. The camera and robot must also use compatible, synchronized clocks.
Camera frame conventions: A camera optical frame is different from a conventional robot body frame. Do not manually swap axes if the TF tree already contains the optical-frame rotation.
Missing transforms: If the hallway camera and base_link are not connected in the TF tree, TF2 cannot perform the conversion. The code catches this failure rather than publishing an invalid point.
Pixel coordinates: If your camera detection is only (u, v) in image pixels, you must first reconstruct its 3D position using depth information or a geometric assumption, such as intersection with a known ground plane. TF2 cannot directly convert a 2D image detection into a 3D robot-frame point.
Static versus moving camera: A camera fixed in the hallway can have a static transform relative to map, while the robot's transform relative to map changes over time. The TF buffer must contain the historical transforms needed for the detection timestamp.
The essential relationship is:
\[ \boxed{ \mathbf{p}_{base} = \mathbf{R}_{base\leftarrow camera} \mathbf{p}_{camera} + \mathbf{t}_{base\leftarrow camera} } \]
Here, \(\mathbf{R}\) is the rotation matrix and \(\mathbf{t}\) is the translation vector from the camera coordinate frame to base_link. TF2 obtains and applies both automatically.

## Initial Source

#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from rclpy.duration import Duration

from geometry_msgs.msg import PointStamped
from tf2_ros import (
    Buffer,
    TransformListener,
    TransformException,
)

# Registers geometry_msgs transformations with tf2.
import tf2_geometry_msgs


class CameraPointTransformer(Node):

    def __init__(self):
        super().__init__('camera_point_transformer')

        # TF2 buffer and listener.
        self.tf_buffer = Buffer()
        self.tf_listener = TransformListener(
            self.tf_buffer,
            self
        )

        # Subscribe to detected points in the camera frame.
        self.subscription = self.create_subscription(
            PointStamped,
            '/hallway_camera/detected_point',
            self.point_callback,
            10
        )

        # Publish transformed points in the robot frame.
        self.publisher = self.create_publisher(
            PointStamped,
            '/detected_point/base_link',
            10
        )

        self.get_logger().info(
            'Camera point transformer started.'
        )

    def point_callback(self, camera_point: PointStamped):

        if not camera_point.header.frame_id:
            self.get_logger().warn(
                'Received a point without a source frame.'
            )
            return

        try:
            # Transform the point into base_link.
            #
            # TF2 uses:
            #   - camera_point.header.frame_id as the source
            #   - camera_point.header.stamp as the transform time
            #   - base_link as the target frame
            #
            # The timeout allows TF2 to wait briefly for
            # the required transform.

            base_point = self.tf_buffer.transform(
                camera_point,
                'base_link',
                timeout=Duration(seconds=0.1)
            )

            # Publish the transformed point.
            self.publisher.publish(base_point)

            self.get_logger().info(
                f'Point in base_link: '
                f'x={base_point.point.x:.3f}, '
                f'y={base_point.point.y:.3f}, '
                f'z={base_point.point.z:.3f}'
            )

        except TransformException as ex:
            self.get_logger().warn(
                f'Could not transform camera point: {ex}'
            )


def main(args=None):
    rclpy.init(args=args)

    node = CameraPointTransformer()

    try:
        rclpy.spin(node)

    except KeyboardInterrupt:
        pass

    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()

## Initial Analysis

It did not check that the source frame was correct. It created a full ROS node instead of just the function and logged a warning when the transform was unavailable instead of returning None.

## Improved Changes

The improved prompt specifies that the point must come from hall_camera and be converted to base_link. It also requires the program to use the point's timestamp and the TF buffer instead of fixed offsets. 

## Live Pending

True

## Synthesis

The new prompt created code that checked for hall_camera and used TF to convert the point into base_link. The original code did not do this, and this is an issue because it means the robot will not be able to judge obstacles/people and their distance. The only issue left was the live camera test. 

## Live Issue

All five tests passed, but the live camera test could not be completed. It returned point: null and live_passed: false without a specific error message. The live hall_camera-to-base_link transformation still needs to be verified in Gazebo.
