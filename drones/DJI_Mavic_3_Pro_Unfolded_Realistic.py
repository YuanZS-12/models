from math import atan2, degrees, hypot

from build123d import *
from build123d import GeomType


# Units: millimeters
# Origin: drone body center on XY, Z=0 at ground contact.


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
        shape = fillet(shape.edges().filter_by(GeomType.CIRCLE), radius)
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
    lower = rounded_box(72, 70, 22, (-52, 0, 57), 2.0, "pod_lower")
    upper = rounded_box(54, 52, 22, (-55, 0, 67), 2.0, "pod_upper")
    nose = rounded_box(28, 46, 18, (-82, 0, 58), 2.0, "pod_front_nose")
    return lower + upper + nose


def blade_local():
    # Swept planform from hub to near tip. The curved centerline and taper
    # create a propeller-like mass without airfoil surface detail.
    stations = [
        (4.5, 5.5, 0.0),
        (30.0, 8.0, 2.0),
        (65.0, 11.0, 7.0),
        (98.0, 9.0, 13.0),
        (119.5, 3.8, 17.0),
    ]
    upper = [(r, sweep + width) for r, width, sweep in stations]
    lower = [(r, sweep - width) for r, width, sweep in reversed(stations)]
    with BuildPart() as blade:
        with BuildSketch(Plane.XY):
            with BuildLine():
                Polyline(*(upper + lower), close=True)
            make_face()
        extrude(amount=2.5)
    solid = Pos(0, 0, 70.0) * blade.part
    solid.label = "prop_blade"
    return solid


def propeller(center_xy, label):
    x, y = center_xy
    prop = rounded_cylinder(16, 4, (x, y), 68.5, 0.8, f"{label}_prop_hub")
    sleeve = rounded_cylinder(10, 8.5, (x, y), 64.0, 0.6, f"{label}_shaft_sleeve")
    sleeve_hole = Pos(x, y, 63.0) * Cylinder(
        radius=3,
        height=11,
        align=(Align.CENTER, Align.CENTER, Align.MIN),
    )
    prop += (sleeve - sleeve_hole).solids()[0]
    base_blade = blade_local()
    for angle in (0, 120, 240):
        blade = Pos(x, y, 0) * Rot(0, 0, angle) * base_blade
        prop += blade
    prop = prop.clean()
    prop.label = label
    return prop


def gen_step():
    body = rounded_box(185, 110, 42, (0, 0, 39), 3.0, "main_fuselage")
    body += rounded_box(160, 85, 20, (0, 0, 62), 2.0, "top_battery_hump")
    body += tapered_gimbal_pod()

    body += rounded_cylinder(18, 32, (-55, 0), 46, 1.2, "main_camera_cylinder")
    body += rounded_cylinder(10, 26, (-55, -14), 50, 0.8, "left_lens_cylinder")
    body += rounded_cylinder(12, 26, (-55, 14), 50, 0.8, "right_lens_cylinder")

    hub_centers = [(148, 120), (148, -120), (-148, 120), (-148, -120)]
    arm_roots = [(72, 45), (72, -45), (-72, 45), (-72, -45)]

    for i, (root, hub) in enumerate(zip(arm_roots, hub_centers), start=1):
        body += arm_between(root, hub, 18, 14, 55, 1.5, f"arm_{i}")

    for i, (x, y) in enumerate(hub_centers, start=1):
        hub = rounded_cylinder(26, 18, (x, y), 48, 2.0, f"motor_hub_{i}")
        shaft = Pos(x, y, 46) * Cylinder(
            radius=3,
            height=24,
            align=(Align.CENTER, Align.CENTER, Align.MIN),
        )
        body += (hub - shaft).solids()[0]

    for i, (x, y) in enumerate([(75, 55), (75, -55), (-75, 55), (-75, -55)], start=1):
        body += rounded_cylinder(8, 12, (x, y), 7, 1.0, f"landing_post_{i}")
        body += rounded_cylinder(12, 8, (x, y), 0, 1.5, f"landing_foot_{i}")

    prop_ne = propeller((148, 120), "three_blade_prop_ne")
    body += prop_ne
    body += mirror(prop_ne, about=Plane.YZ)
    body += mirror(prop_ne, about=Plane.XZ)
    body += mirror(mirror(prop_ne, about=Plane.YZ), about=Plane.XZ)

    body = body.clean()
    body.label = "DJI_Mavic_3_Pro_Unfolded_Realistic"
    return body


if __name__ == "__main__":
    export_step(gen_step(), "DJI_Mavic_3_Pro_Unfolded_Realistic.step")
