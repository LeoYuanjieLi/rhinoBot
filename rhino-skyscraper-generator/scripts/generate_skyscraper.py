import rhinoscriptsyntax as rs

def regenerate_skyscraper_with_grid():
    # --- Building Parameters ---
    total_height = 200
    floor_height = 4
    core_size = 12
    slab_thickness = 0.3
    column_size = 0.8
    grid_spacing = 8.0  # Spacing between columns in the grid
    # ---------------------------
    
    num_floors = int(total_height / floor_height)
    
    # Setup Layers
    if not rs.IsLayer("Core"): rs.AddLayer("Core", (150,150,150))
    if not rs.IsLayer("Slabs"): rs.AddLayer("Slabs", (200,200,200))
    if not rs.IsLayer("Columns"): rs.AddLayer("Columns", (100,100,100))
    
    c_half = core_size / 2.0
    
    # 1. Core (Start at Z=0, End at Z=total_height)
    rs.CurrentLayer("Core")
    rs.AddBox([
        (-c_half, -c_half, 0), (c_half, -c_half, 0), (c_half, c_half, 0), (-c_half, c_half, 0),
        (-c_half, -c_half, total_height), (c_half, -c_half, total_height), (c_half, c_half, total_height), (-c_half, c_half, total_height)
    ])
    
    # 2. Slabs and Column Grid
    for i in range(num_floors + 1):
        z_base = i * floor_height
        
        # Setback logic for current slab footprint
        footprint = 40
        if i > (num_floors * 0.7): footprint = 28
        elif i > (num_floors * 0.4): footprint = 34
        
        half = footprint / 2.0
        
        # Add Slab
        rs.CurrentLayer("Slabs")
        rs.AddBox([
            (-half, -half, z_base), (half, -half, z_base), (half, half, z_base), (-half, half, z_base),
            (-half, -half, z_base + slab_thickness), (half, -half, z_base + slab_thickness), (half, half, z_base + slab_thickness), (-half, half, z_base + slab_thickness)
        ])
        
        # Add Grid of Columns supporting the next floor
        if i < num_floors:
            rs.CurrentLayer("Columns")
            
            # Use the footprint of the NEXT floor to ensure column alignment
            next_footprint = 40
            if i + 1 > (num_floors * 0.7): next_footprint = 28
            elif i + 1 > (num_floors * 0.4): next_footprint = 34
            
            col_limit = min(half, next_footprint / 2.0)
            z_bottom = z_base + slab_thickness
            z_top = (i + 1) * floor_height
            cs = column_size / 2.0
            
            # Generate Grid Points
            steps = int(col_limit * 2 / grid_spacing)
            actual_spacing = (col_limit * 2) / steps if steps > 0 else 0
            
            for gx in range(steps + 1):
                for gy in range(steps + 1):
                    px = -col_limit + gx * actual_spacing
                    py = -col_limit + gy * actual_spacing
                    
                    # Check if the column is OUTSIDE the core area
                    if abs(px) > (c_half - 0.1) or abs(py) > (c_half - 0.1):
                        rs.AddBox([
                            (px-cs, py-cs, z_bottom), (px+cs, py-cs, z_bottom), (px+cs, py+cs, z_bottom), (px-cs, py+cs, z_bottom),
                            (px-cs, py-cs, z_top), (px+cs, py-cs, z_top), (px+cs, py+cs, z_top), (px-cs, py+cs, z_top)
                        ])

    print("Skyscraper with full column grid generated successfully.")

regenerate_skyscraper_with_grid()
