import math
import os
import sys

_SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
for _candidate in (
    _SCRIPT_DIR,
    os.path.abspath(os.path.join(_SCRIPT_DIR, "..", "skills", "nx-cad")),
):
    if _candidate not in sys.path:
        sys.path.insert(0, _candidate)

from cadnx import NXBuilder


def _polar_point(radius, angle_deg):
    angle = math.radians(angle_deg)
    return (radius * math.cos(angle), radius * math.sin(angle))


def _annular_sector_points(inner_radius, outer_radius, center_angle, sweep_angle, segments):
    start = center_angle - sweep_angle / 2.0
    end = center_angle + sweep_angle / 2.0
    points = []

    for index in range(segments + 1):
        angle = start + (end - start) * index / float(segments)
        points.append(_polar_point(outer_radius, angle))

    for index in range(segments, -1, -1):
        angle = start + (end - start) * index / float(segments)
        points.append(_polar_point(inner_radius, angle))

    return points


def _helix_point(radius, z_start, z_end, revolutions, fraction):
    angle = 2.0 * math.pi * revolutions * fraction
    z = z_start + (z_end - z_start) * fraction
    return (radius * math.cos(angle), radius * math.sin(angle), z)


def _distance(start, end):
    return math.sqrt(
        (end[0] - start[0]) ** 2
        + (end[1] - start[1]) ** 2
        + (end[2] - start[2]) ** 2
    )


def _axis(start, end):
    length = _distance(start, end)
    return (
        (end[0] - start[0]) / length,
        (end[1] - start[1]) / length,
        (end[2] - start[2]) / length,
    )


def build(output_path: str = None):
    b = NXBuilder()

    # Units: millimeters. Origin is on the staircase centerline at base bottom.
    column_diameter = 14.0
    column_height = 140.0

    tread_count = 20
    tread_thickness = 4.0
    tread_inner_radius = 10.0
    tread_outer_radius = 62.0
    tread_plan_angle = 24.0
    tread_first_z = 4.0
    tread_rise = 6.0
    tread_rotation = 18.0
    tread_arc_segments = 8

    handrail_diameter = 5.0
    handrail_radius = 66.0
    handrail_z_start = 14.0
    handrail_z_end = 130.0
    handrail_revolutions = 1.0
    handrail_segments = 96

    baluster_diameter = 3.0
    base_diameter = 90.0
    base_thickness = 5.0

    b.cylinder(base_diameter, base_thickness, origin=(0.0, 0.0, 0.0), axis=(0.0, 0.0, 1.0))
    b.cylinder(column_diameter, column_height, origin=(0.0, 0.0, 0.0), axis=(0.0, 0.0, 1.0))

    for index in range(tread_count):
        center_angle = index * tread_rotation
        tread_center_z = tread_first_z + index * tread_rise
        tread_bottom_z = tread_center_z - tread_thickness / 2.0
        points = _annular_sector_points(
            tread_inner_radius,
            tread_outer_radius,
            center_angle,
            tread_plan_angle,
            tread_arc_segments,
        )
        b.polygon_prism(points, tread_thickness, origin=(0.0, 0.0, tread_bottom_z), axis=(0.0, 0.0, 1.0))

    # Approximate the helical tube as short, overlapping cylinders along the
    # exact one-turn helical centerline for robust NX journal execution.
    for index in range(handrail_segments):
        f0 = index / float(handrail_segments)
        f1 = (index + 1) / float(handrail_segments)
        start = _helix_point(handrail_radius, handrail_z_start, handrail_z_end, handrail_revolutions, f0)
        end = _helix_point(handrail_radius, handrail_z_start, handrail_z_end, handrail_revolutions, f1)
        segment_length = _distance(start, end) + 0.15
        b.cylinder(handrail_diameter, segment_length, origin=start, axis=_axis(start, end))

    for index in range(tread_count):
        angle_deg = index * tread_rotation
        angle_fraction = angle_deg / 360.0
        x, y = _polar_point(handrail_radius, angle_deg)
        tread_center_z = tread_first_z + index * tread_rise
        bottom_z = tread_center_z + tread_thickness / 2.0
        top_z = handrail_z_start + (handrail_z_end - handrail_z_start) * angle_fraction
        b.cylinder(
            baluster_diameter,
            max(top_z - bottom_z, 0.1),
            origin=(x, y, bottom_z),
            axis=(0.0, 0.0, 1.0),
        )

    if output_path is None:
        output_path = os.path.splitext(os.path.abspath(__file__))[0] + ".step"
    b.export_step(output_path)


def main():
    default_output = os.path.splitext(os.path.abspath(__file__))[0] + ".step"
    output = sys.argv[1] if len(sys.argv) > 1 else default_output
    build(output)


if __name__ == "__main__":
    main()
