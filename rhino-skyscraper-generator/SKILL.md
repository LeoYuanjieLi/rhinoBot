---
name: rhino-skyscraper-generator
description: Generates a parametric 3D skyscraper model in Rhino with a central core, floor slabs, and a structural column grid. Use this when a user asks to build or model a skyscraper in Rhino.
---

# Rhino Skyscraper Generator

This skill enables the automated generation of detailed, parametrized skyscrapers in Rhino using RhinoScript Python. The generated building includes:
- A central structural core starting at the ground plane (Z=0).
- Floor slabs with adjustable thickness and programmatic setbacks.
- A comprehensive structural column grid that correctly spans between floors without clipping the core.
- Organized layer structure (`Core`, `Slabs`, `Columns`).

## Usage Instructions

To create a skyscraper, you should use the bundled Python script.

1. **Read the Script**: Use the `read_file` tool to read the contents of the `scripts/generate_skyscraper.py` file included in this skill.
2. **Customize Parameters (Optional)**: If the user provided specific requirements (e.g., a specific height, floor count, footprint size, or column spacing), you can modify the parameter variables at the top of the script using string replacement or simply prepending new variable declarations before executing it.
   * `total_height` (default: 200)
   * `floor_height` (default: 4)
   * `core_size` (default: 12)
   * `slab_thickness` (default: 0.3)
   * `column_size` (default: 0.8)
   * `grid_spacing` (default: 8.0)
3. **Execute the Code**: Use the `execute_rhinoscript_python_code` tool to run the script.
4. **Validate**: Check the `output` of the execution tool and optionally capture the viewport using `capture_viewport` to visually verify the model.
