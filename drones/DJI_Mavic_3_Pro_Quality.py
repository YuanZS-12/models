from math import atan2, degrees, hypot

from build123d import *
from build123d import GeomType


# Units: millimeters
# Origin: drone center on XY, Z=0 at the lowest landing feet.


def rounded_box(size_x, size_y, size_z, center, radius, label):
    shape = Box(size_x, size_y, size_z, align=(Align.CENTER, Align.CENTER, Align.CENTER))
    shape = Pos(*center) * shape
    if radius > 0:
        shape = fillet(shape.edges(), radius)
    shape.label = label
    return shape


def rounded_cylinder(diameter, height, center_xy, bottom_z, radius, label):
    shape = Cylinder(
        radius=diameter / 2,
        height=height,
        align=(Align.CENTER, Align.CENTER, Align.MIN),
    )
    shape = Pos(center_xy[0], center_xy[1], bottom_z) * shape
    if radius > 0:
        top_bottom_edges = shape.edges().filter_by(GeomType.CIRCLE)
        shape = fillet(top_bottom_edges, radius)
    shape.label = label
    return shape


def arm_between(start, end, width, height, z_center, radius, label):
    sx, sy = start
    ex, ey = end
    length = hypot(ex - sx, ey - sy)
    angle = degrees(atan2(ey - sy, ex - sx))
    cx = (sx + ex) / 2
    cy = (sy + ey) / 2
    shape = Box(length, width, height, align=(Align.CENTER, Align.CENTER, Align.CENTER))
    shape = Pos(cx, cy, z_center) * Rot(0, 0, angle) * shape
    if radius > 0:
        shape = fillet(shape.edges(), radius)
    shape.label = label
    return shape


def tapered_gimbal_pod():
    # A rounded solid approximation of the front gimbal fairing. The stacked
    # overlapping blocks give a tapered plan/profile while preserving a robust
    # single-body boolean target.
    lower = rounded_box(70, 80, 22, (-55, 0, 57), 2.0, "pod_lower")
    upper = rounded_box(52, 58, 22, (-58, 0, 67), 2.0, "pod_upper")
    nose = rounded_box(28, 50, 18, (-82, 0, 58), 2.0, "pod_front_nose")
    return lower + upper + nose


def gen_step():
    body = rounded_box(185, 110, 42, (0, 0, 39), 3.0, "main_fuselage")
    body += rounded_box(160, 85, 20, (0, 0, 62), 2.0, "top_battery_hump")
    body += tapered_gimbal_pod()

    # Camera stack, all fused to the pod/body. Cylinders are vertical as requested.
    body += rounded_cylinder(18, 32, (-60, 0), 46, 1.2, "main_camera_cylinder")
    body += rounded_cylinder(10, 26, (-60, -14), 50, 0.8, "left_lens_cylinder")
    body += rounded_cylinder(12, 26, (-60, 14), 50, 0.8, "right_lens_cylinder")

    hub_centers = [(148, 120), (148, -120), (-148, 120), (-148, -120)]
    arm_roots = [(72, 45), (72, -45), (-72, 45), (-72, -45)]

    for i, (root, hub) in enumerate(zip(arm_roots, hub_centers), start=1):
        body += arm_between(root, hub, 18, 14, 55, 1.5, f"arm_{i}")

    for i, (x, y) in enumerate(hub_centers, start=1):
        hub = rounded_cylinder(26, 18, (x, y), 46, 2.0, f"motor_hub_{i}")
        shaft = Pos(x, y, 44) * Cylinder(
            radius=3,
            height=24,
            align=(Align.CENTER, Align.CENTER, Align.MIN),
        )
        cut_hub = (hub - shaft).solids()[0]
        body += cut_hub

    for i, (x, y) in enumerate([(75, 55), (75, -55), (-75, 55), (-75, -55)], start=1):
        body += rounded_cylinder(8, 12, (x, y), 7, 1.0, f"landing_post_{i}")
        body += rounded_cylinder(12, 8, (x, y), 0, 1.5, f"landing_foot_{i}")

    body = body.clean()
    body.label = "DJI_Mavic_3_Pro_Quality"
    return body


if __name__ == "__main__":
    export_step(gen_step(), "DJI_Mavic_3_Pro_Quality.step")
