import rhinoscriptsyntax as rs

def make_hollow_vase(name, pos, outer_params, wall_thickness=0.5):
    tx, ty = pos
    # Outer
    outer_curves = []
    for x, y, z, r in outer_params:
        center = (tx + x, ty + y, z)
        crv = rs.AddCircle(center, r)
        outer_curves.append(crv)
    
    outer_loft = rs.AddLoftSrf(outer_curves)[0]
    rs.CapPlanarHoles(outer_loft)
    
    # Inner
    inner_curves = []
    for i, (x, y, z, r) in enumerate(outer_params):
        # Raise the bottom of the inner cavity to leave a solid base
        iz = z + wall_thickness if i == 0 else z
        # Shrink the radius to create the wall
        ir = max(0.2, r - wall_thickness)
        # Extend the top profile slightly so the boolean difference cleanly cuts the top open
        if i == len(outer_params) - 1: iz += 1.0
        
        center = (tx + x, ty + y, iz)
        crv = rs.AddCircle(center, ir)
        inner_curves.append(crv)
        
    inner_loft = rs.AddLoftSrf(inner_curves)[0]
    rs.CapPlanarHoles(inner_loft)
    
    # Create the hollow form
    final = rs.BooleanDifference(outer_loft, inner_loft)
    rs.DeleteObjects(outer_curves + inner_curves)
    
    if final:
        rs.ObjectName(final[0], name)
        print("Successfully generated: " + name)
        return final[0]
    else:
        print("Failed to generate: " + name)
        return None

# Example Execution
# The Biomorphic "Pinch" (Irregular shifting)
pinch_params = [(0, 0, 0, 3.5), (2, 1, 5, 5.5), (-3, -1, 10, 4.0), (1, 2, 15, 6.0), (0, 0, 20, 2.5)]
make_hollow_vase("Vase_Artsy", (0, 0), pinch_params, wall_thickness=0.5)
