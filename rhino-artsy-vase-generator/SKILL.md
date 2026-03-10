---
name: rhino-artsy-vase-generator
description: Generates contemporary, sculptural, and fully hollow 3D vases in Rhino. Use this when a user asks to design, create, or model a modern, artsy, biomorphic, or functional vase/pottery in Rhino.
---

# Rhino Artsy Vase Generator

This skill enables the automated generation of contemporary, "artsy" ceramic vases in Rhino using RhinoScript Python. The generated vases are fully functional, meaning they are properly hollowed out with solid walls (capable of holding water) rather than just being single-surface shells.

The core logic uses a double-lofting technique (an outer profile lofted, an inner profile lofted, and then a Boolean Difference to hollow it out).

## Usage Instructions

To create a sculptural vase, use the bundled Python script.

1. **Read the Script**: Use the `read_file` tool to read the contents of the `scripts/generate_vase.py` file included in this skill.
2. **Customize Profiles (Optional)**: The script contains pre-defined parameter sets for a "Pinch", "Totem", and "Neck" style vase. The user can request specific dimensions or shapes. You can modify the `outer_params` list in the script before executing it.
   - The format is `(x_offset, y_offset, z_height, radius)`.
   - By shifting the `x_offset` and `y_offset`, you create asymmetrical, organic shapes.
   - The script automatically handles hollowing out the vase based on the `wall_thickness` parameter.
3. **Execute the Code**: Use the `execute_rhinoscript_python_code` tool to run the customized script.
4. **Validate**: Check the `output` of the execution tool and optionally capture the viewport using `capture_viewport` to visually verify the model.