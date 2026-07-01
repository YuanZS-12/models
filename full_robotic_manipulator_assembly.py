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


def build(output_path: str = None):
    b = NXBuilder()

    # Independent prompt parameters, millimeters.
    base_size = 120.0
    base_height = 80.0
    shoulder_cube = 90.0
    housing_wall = 10.0
    flange_thickness = 10.0
    flange_hole_diameter = 8.0
    cbore_depth = 3.0

    lower_joint_length = 100.0
    lower_joint_width = 70.0
    lower_joint_height = 60.0
    lower_beam_length = 320.0
    lower_beam_width = 45.0
    lower_beam_height = 35.0
    lower_beam_wall = 6.0
    lower_boom_angle_degrees = 35.0
    lower_rib_length = 80.0
    lower_rib_height = 30.0
    lower_rib_thickness = 8.0
    rib_spacing = 30.0
    six_mm_hole = 6.0

    wrist_length = 75.0
    wrist_width = 60.0
    wrist_height = 55.0
    upper_beam_length = 180.0
    upper_beam_width = 40.0
    upper_beam_height = 32.0
    upper_beam_wall = 6.0
    upper_lug_width = 18.0
    end_flange_size = 90.0
    end_flange_thickness = 10.0
    end_spindle_diameter = 30.0
    end_hole_diameter = 7.0

    gripper_body_length = 110.0
    gripper_body_width = 75.0
    gripper_body_height = 65.0
    finger_root_length = 35.0
    finger_root_width = 22.0
    finger_thickness = 12.0
    claw_length = 85.0
    claw_tip_width = 8.0
    guide_rail_length = 130.0
    guide_rail_size = 10.0
    carrier_slot_clearance = 4.0
    manifold_boss_hole_diameter = 5.0

    exterior_fillet = 2.0
    bore_chamfer = 1.0
    overcut = 4.0

    # Derived coordinate frame.
    shoulder_z0 = base_height
    shoulder_center_z = shoulder_z0 + shoulder_cube / 2.0
    shoulder_top_z = shoulder_z0 + shoulder_cube
    shoulder_axis_y = 0.0
    lower_joint_x0 = shoulder_cube / 2.0
    lower_joint_z0 = shoulder_center_z - lower_joint_height / 2.0
    lower_joint_out_x = lower_joint_x0 + lower_joint_length

    lower_angle = math.radians(lower_boom_angle_degrees)
    lower_axis = (math.cos(lower_angle), 0.0, math.sin(lower_angle))
    beam_side_axis = (0.0, 1.0, 0.0)
    lower_beam_start = (
        lower_joint_out_x,
        0.0,
        shoulder_center_z - lower_beam_height / 2.0,
    )
    lower_beam_end = tuple(
        lower_beam_start[i] + lower_axis[i] * lower_beam_length
        for i in range(3)
    )
    wrist_origin = (
        lower_beam_end[0],
        -wrist_width / 2.0,
        lower_beam_end[2] - wrist_height / 2.0,
    )
    wrist_front_x = wrist_origin[0] + wrist_length
    wrist_center_z = wrist_origin[2] + wrist_height / 2.0
    upper_origin = (
        wrist_front_x,
        -upper_beam_width / 2.0,
        wrist_center_z - upper_beam_height / 2.0,
    )
    upper_front_x = upper_origin[0] + upper_beam_length
    flange_origin = (
        upper_front_x,
        -end_flange_size / 2.0,
        wrist_center_z - end_flange_size / 2.0,
    )
    gripper_origin = (
        upper_front_x + end_flange_thickness,
        -gripper_body_width / 2.0,
        wrist_center_z - gripper_body_height / 2.0,
    )

    def box_centered_x(body_length, body_width, body_height, center):
        return b.rounded_box(
            body_length,
            body_width,
            body_height,
            exterior_fillet,
            origin=(
                center[0] - body_length / 2.0,
                center[1] - body_width / 2.0,
                center[2] - body_height / 2.0,
            ),
        )

    def cut_counterbore_z(target, diameter, depth, cbore_diameter, x, y, z_top):
        return b.counterbore_hole(
            target,
            diameter,
            depth + overcut,
            cbore_diameter,
            cbore_depth,
            position=(x, y, z_top + 1.0),
            direction=(0, 0, -1),
        )

    def cut_hole_x(target, diameter, depth, x, y, z):
        hole = b.hole(
            diameter,
            depth + overcut,
            position=(x - 1.0, y, z),
            direction=(1, 0, 0),
        )
        b.boolean_subtract(target, hole)
        cbore = b.hole(
            diameter + 6.0,
            cbore_depth + 1.0,
            position=(x - 1.0, y, z),
            direction=(1, 0, 0),
        )
        b.boolean_subtract(target, cbore)

    def hollow_rect_prism(length, width, height, wall, origin, axis):
        body = b.polygon_prism_on_plane(
            [
                (-height / 2.0, -width / 2.0),
                (height / 2.0, -width / 2.0),
                (height / 2.0, width / 2.0),
                (-height / 2.0, width / 2.0),
            ],
            length,
            origin=origin,
            u_axis=(0, 0, 1),
            v_axis=beam_side_axis,
            extrude_axis=axis,
        )
        void = b.polygon_prism_on_plane(
            [
                (-(height / 2.0 - wall), -(width / 2.0 - wall)),
                ((height / 2.0 - wall), -(width / 2.0 - wall)),
                ((height / 2.0 - wall), (width / 2.0 - wall)),
                (-(height / 2.0 - wall), (width / 2.0 - wall)),
            ],
            length + overcut,
            origin=tuple(origin[i] - axis[i] * (overcut / 2.0) for i in range(3)),
            u_axis=(0, 0, 1),
            v_axis=beam_side_axis,
            extrude_axis=axis,
        )
        b.boolean_subtract(body, void)
        b.fillet(b.get_edges_by_axis(body, axis=axis), exterior_fillet)
        return body

    # Base station mount.
    base = b.rounded_box(
        base_size,
        base_size,
        base_height,
        exterior_fillet,
        origin=(-base_size / 2.0, -base_size / 2.0, 0.0),
    )

    shoulder = b.rounded_box(
        shoulder_cube,
        shoulder_cube,
        shoulder_cube,
        exterior_fillet,
        origin=(-shoulder_cube / 2.0, -shoulder_cube / 2.0, shoulder_z0),
    )
    cut_hole_x(
        shoulder,
        shoulder_cube - 2.0 * housing_wall,
        shoulder_cube,
        -shoulder_cube / 2.0,
        shoulder_axis_y,
        shoulder_center_z,
    )
    b.chamfer(b.get_edges_by_axis(shoulder, axis=(1, 0, 0)), bore_chamfer)

    shoulder_flanges = []
    flange_specs = [
        (
            flange_thickness,
            shoulder_cube,
            (-shoulder_cube / 2.0 - flange_thickness, -shoulder_cube / 2.0),
        ),
        (
            flange_thickness,
            shoulder_cube,
            (shoulder_cube / 2.0, -shoulder_cube / 2.0),
        ),
        (
            shoulder_cube,
            flange_thickness,
            (-shoulder_cube / 2.0, -shoulder_cube / 2.0 - flange_thickness),
        ),
        (
            shoulder_cube,
            flange_thickness,
            (-shoulder_cube / 2.0, shoulder_cube / 2.0),
        ),
    ]
    for length, width, origin_xy in flange_specs:
        flange_origin = (origin_xy[0], origin_xy[1], shoulder_top_z)
        flange = b.rounded_box(
            length,
            width,
            flange_thickness,
            exterior_fillet,
            origin=flange_origin,
        )
        shoulder_flanges.append(flange)
        for x in (flange_origin[0] + 5.0, flange_origin[0] + length - 5.0):
            for y in (flange_origin[1] + 5.0, flange_origin[1] + width - 5.0):
                cut_counterbore_z(
                    flange,
                    flange_hole_diameter,
                    flange_thickness,
                    flange_hole_diameter + 8.0,
                    x,
                    y,
                    shoulder_top_z + flange_thickness,
                )

    # Lower boom joint and hollow extrusion.
    lower_joint = b.rounded_box(
        lower_joint_length,
        lower_joint_width,
        lower_joint_height,
        exterior_fillet,
        origin=(lower_joint_x0, -lower_joint_width / 2.0, lower_joint_z0),
    )
    cut_hole_x(
        lower_joint,
        44.0,
        lower_joint_length,
        lower_joint_x0,
        0.0,
        shoulder_center_z,
    )

    for y_sign in (-1.0, 1.0):
        lug = b.rounded_box(
            24.0,
            12.0,
            24.0,
            exterior_fillet,
            origin=(
                lower_joint_x0 + 26.0,
                y_sign * (lower_joint_width / 2.0),
                shoulder_center_z - 12.0,
            ),
        )
        hole = b.hole(
            six_mm_hole,
            16.0,
            position=(
                lower_joint_x0 + 38.0,
                y_sign * (lower_joint_width / 2.0 + 13.0),
                shoulder_center_z,
            ),
            direction=(0, -y_sign, 0),
        )
        b.boolean_subtract(lug, hole)

    lower_beam = hollow_rect_prism(
        lower_beam_length,
        lower_beam_width,
        lower_beam_height,
        lower_beam_wall,
        lower_beam_start,
        lower_axis,
    )

    rib_start_distance = 70.0
    for offset in (-rib_spacing / 2.0, rib_spacing / 2.0):
        rib_origin = tuple(
            lower_beam_start[i] + lower_axis[i] * rib_start_distance
            for i in range(3)
        )
        rib_origin = (
            rib_origin[0],
            offset - lower_rib_thickness / 2.0,
            rib_origin[2] + lower_beam_height / 2.0,
        )
        rib = b.polygon_prism_on_plane(
            [
                (0.0, 0.0),
                (lower_rib_length, 0.0),
                (lower_rib_length, lower_rib_height),
                (0.0, lower_rib_height),
            ],
            lower_rib_thickness,
            origin=rib_origin,
            u_axis=lower_axis,
            v_axis=(0, 0, 1),
            extrude_axis=(0, 1, 0),
        )
        for d in (20.0, 60.0):
            pos = tuple(rib_origin[i] + lower_axis[i] * d for i in range(3))
            hole = b.hole(
                six_mm_hole,
                lower_rib_height + overcut,
                position=(pos[0], offset, pos[2] + lower_rib_height + 1.0),
                direction=(0, 0, -1),
            )
            b.boolean_subtract(rib, hole)

    # Wrist, upper link, and end flange.
    wrist = b.rounded_box(
        wrist_length,
        wrist_width,
        wrist_height,
        exterior_fillet,
        origin=wrist_origin,
    )
    cut_hole_x(wrist, 35.0, wrist_length, wrist_origin[0], 10.0, wrist_center_z)
    shaft = b.cylinder(
        32.0,
        30.0,
        origin=(wrist_front_x - 5.0, 10.0, wrist_center_z),
        axis=(1, 0, 0),
    )

    upper_beam = hollow_rect_prism(
        upper_beam_length,
        upper_beam_width,
        upper_beam_height,
        upper_beam_wall,
        (upper_origin[0], 0.0, upper_origin[2] + upper_beam_height / 2.0),
        (1, 0, 0),
    )
    for x in (upper_origin[0] + 55.0, upper_origin[0] + 115.0):
        lug = b.rounded_box(
            28.0,
            upper_lug_width,
            10.0,
            exterior_fillet,
            origin=(x - 14.0, -upper_lug_width / 2.0, upper_origin[2] + upper_beam_height),
        )
        cut_counterbore_z(
            lug,
            six_mm_hole,
            10.0,
            six_mm_hole + 6.0,
            x,
            0.0,
            upper_origin[2] + upper_beam_height + 10.0,
        )

    end_flange = b.rounded_box(
        end_flange_thickness,
        end_flange_size,
        end_flange_size,
        exterior_fillet,
        origin=flange_origin,
    )
    spindle = b.hole(
        end_spindle_diameter,
        end_flange_thickness + overcut,
        position=(upper_front_x - 1.0, 0.0, wrist_center_z),
        direction=(1, 0, 0),
    )
    b.boolean_subtract(end_flange, spindle)
    for y in (-28.0, 28.0):
        for z in (wrist_center_z - 28.0, wrist_center_z + 28.0):
            hole = b.hole(
                end_hole_diameter,
                end_flange_thickness + overcut,
                position=(upper_front_x - 1.0, y, z),
                direction=(1, 0, 0),
            )
            b.boolean_subtract(end_flange, hole)

    # Pneumatic three-finger gripper subassembly, mounted on final flange axis.
    gripper_body = b.rounded_box(
        gripper_body_length,
        gripper_body_width,
        gripper_body_height,
        exterior_fillet,
        origin=gripper_origin,
    )
    piston_cavity = b.hole(
        42.0,
        gripper_body_length + overcut,
        position=(gripper_origin[0] - 1.0, 0.0, wrist_center_z),
        direction=(1, 0, 0),
    )
    b.boolean_subtract(gripper_body, piston_cavity)
    for y in (-28.0, 28.0):
        for z in (wrist_center_z - 28.0, wrist_center_z + 28.0):
            hole = b.hole(
                end_hole_diameter,
                14.0,
                position=(gripper_origin[0] - 1.0, y, z),
                direction=(1, 0, 0),
            )
            b.boolean_subtract(gripper_body, hole)

    rail_x = gripper_origin[0] + gripper_body_length
    for z_off in (-18.0, 18.0):
        b.rounded_box(
            guide_rail_size,
            guide_rail_length,
            guide_rail_size,
            exterior_fillet,
            origin=(
                rail_x,
                -guide_rail_length / 2.0,
                wrist_center_z + z_off - guide_rail_size / 2.0,
            ),
        )

    for y_sign in (-1.0, 1.0):
        boss = b.rounded_box(
            18.0,
            10.0,
            20.0,
            exterior_fillet,
            origin=(
                gripper_origin[0] + 35.0,
                y_sign * gripper_body_width / 2.0,
                wrist_center_z - 10.0,
            ),
        )
        hole = b.hole(
            manifold_boss_hole_diameter,
            14.0,
            position=(
                gripper_origin[0] + 44.0,
                y_sign * (gripper_body_width / 2.0 + 11.0),
                wrist_center_z,
            ),
            direction=(0, -y_sign, 0),
        )
        b.boolean_subtract(boss, hole)

    finger_angles = (90.0, 210.0, 330.0)
    for angle_deg in finger_angles:
        angle = math.radians(angle_deg)
        radial = (0.0, math.cos(angle), math.sin(angle))
        tangent = (0.0, -math.sin(angle), math.cos(angle))
        root_center_y = radial[1] * 33.0
        root_center_z = wrist_center_z + radial[2] * 33.0
        root = b.polygon_prism_on_plane(
            [
                (-finger_root_width / 2.0, -finger_thickness / 2.0),
                (finger_root_width / 2.0, -finger_thickness / 2.0),
                (finger_root_width / 2.0, finger_thickness / 2.0),
                (-finger_root_width / 2.0, finger_thickness / 2.0),
            ],
            finger_root_length,
            origin=(rail_x + 8.0, root_center_y, root_center_z),
            u_axis=radial,
            v_axis=tangent,
            extrude_axis=(1, 0, 0),
        )
        slot = b.polygon_prism_on_plane(
            [
                (-(guide_rail_size + carrier_slot_clearance) / 2.0, -4.0),
                ((guide_rail_size + carrier_slot_clearance) / 2.0, -4.0),
                ((guide_rail_size + carrier_slot_clearance) / 2.0, 4.0),
                (-(guide_rail_size + carrier_slot_clearance) / 2.0, 4.0),
            ],
            finger_root_length + overcut,
            origin=(rail_x + 6.0, root_center_y, root_center_z),
            u_axis=radial,
            v_axis=tangent,
            extrude_axis=(1, 0, 0),
        )
        b.boolean_subtract(root, slot)

        claw_start_x = rail_x + 8.0 + finger_root_length
        claw = b.polygon_prism_on_plane(
            [
                (-finger_root_width / 2.0, -finger_thickness / 2.0),
                (finger_root_width / 2.0, -finger_thickness / 2.0),
                (claw_tip_width / 2.0, claw_length - finger_thickness / 2.0),
                (-claw_tip_width / 2.0, claw_length - finger_thickness / 2.0),
            ],
            finger_thickness,
            origin=(claw_start_x, root_center_y, root_center_z),
            u_axis=radial,
            v_axis=(1, 0, 0),
            extrude_axis=tangent,
        )
        face_relief = b.polygon_prism_on_plane(
            [
                (-finger_root_width / 2.0, 24.0),
                (finger_root_width / 2.0, 24.0),
                (finger_root_width / 2.0, 31.0),
                (-finger_root_width / 2.0, 31.0),
            ],
            finger_thickness + overcut,
            origin=(claw_start_x, root_center_y, root_center_z),
            u_axis=radial,
            v_axis=(1, 0, 0),
            extrude_axis=tangent,
        )
        b.boolean_subtract(claw, face_relief)
        b.chamfer(b.get_all_edges(claw), bore_chamfer)

    if output_path is None:
        output_path = os.path.splitext(os.path.abspath(__file__))[0] + ".step"
    b.export_step(output_path)


def main():
    default_output = os.path.splitext(os.path.abspath(__file__))[0] + ".step"
    output = sys.argv[1] if len(sys.argv) > 1 else default_output
    build(output)


if __name__ == "__main__":
    main()
