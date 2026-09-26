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