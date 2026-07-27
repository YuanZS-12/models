Line 1 : Traceback (most recent call last):
  File "D:\Workdir\iproot\nx2606.1700\test44\workspace\aerospace_frame_003\aerospace_hpc_rear_frame.py", line 383, in <module>
    main()
  File "D:\Workdir\iproot\nx2606.1700\test44\workspace\aerospace_frame_003\aerospace_hpc_rear_frame.py", line 350, in main
    builder, step_path = build(output)
                         ^^^^^^^^^^^^^
  File "D:\Workdir\iproot\nx2606.1700\test44\workspace\aerospace_frame_003\aerospace_hpc_rear_frame.py", line 284, in build
    radial_boss_with_hole(borescope_angle_degrees, borescope_x, borescope_boss_diameter, borescope_boss_height, borescope_hole_diameter)
  File "D:\Workdir\iproot\nx2606.1700\test44\workspace\aerospace_frame_003\aerospace_hpc_rear_frame.py", line 280, in radial_boss_with_hole
    b.boolean_subtract(frame, tool)
  File "D:\Workdir\iproot\nx2606.1700\test44\workspace\aerospace_frame_003\cadnx\builder.py", line 893, in boolean_subtract
    feature = builder.CommitFeature()
              ^^^^^^^^^^^^^^^^^^^^^^^
NXOpen.NXException: 'The tool and target do not form a complete intersection or have a touch condition which will result in a region with zero wall thickness.
'The tool and target do not form a complete intersection or have a touch condition which will result in a region with zero wall thickness.
