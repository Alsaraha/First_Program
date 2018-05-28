import bpy, random

def cream(x, y, z, c, s, m, mm, rx, ry, rz):
    # Select
    if s == 0:
    	bpy.ops.mesh.primitive_cube_add(view_align=False, enter_editmode=False, location=(-0.745644, 0.124446, -0.645324), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    elif s == 1:
    	bpy.ops.mesh.primitive_uv_sphere_add(view_align=False, enter_editmode=False, location=(-0.745644, 0.124446, -0.645324), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    elif s == 2:
    	bpy.ops.mesh.primitive_cylinder_add(view_align=False, enter_editmode=False, location=(-0.745644, 0.124446, -0.645324), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    elif s == 3:
    	bpy.ops.mesh.primitive_cone_add(radius1=1, radius2=0, depth=2, view_align=False, enter_editmode=False, location=(-0.745644, 0.124446, -0.645324), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    elif s == 4:
    	bpy.ops.mesh.primitive_torus_add(view_align=False, location=(-0.745644, 0.124446, -0.645324), rotation=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False), major_radius=1, minor_radius=0.25, abso_major_rad=1.25, abso_minor_rad=0.75)
    elif s == 5:
    	bpy.ops.mesh.primitive_monkey_add(view_align=False, enter_editmode=False, location=(-0.745644, 0.124446, -0.645324), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    elif s == 6:
    	bpy.ops.mesh.primitive_round_cube_add(view_align=False, location=(-0.745644, 0.124446, -0.645324), rotation=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    elif s == 7:
    	bpy.ops.mesh.primitive_elbow_joint_add()
    	bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')
    	bpy.ops.transform.resize(value=(0.25, 0.25, 0.25), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    elif s == 8:
    	bpy.ops.mesh.primitive_tee_joint_add()
    	bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')
    	bpy.ops.transform.resize(value=(0.25, 0.25, 0.25), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    elif s == 9:
    	bpy.ops.mesh.primitive_wye_joint_add()
    	bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')
    	bpy.ops.transform.resize(value=(0.25, 0.25, 0.25), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    elif s == 10:
    	bpy.ops.mesh.primitive_cross_joint_add()
    	bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')
    	bpy.ops.transform.resize(value=(0.25, 0.25, 0.25), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    elif s == 11:
    	bpy.ops.mesh.primitive_n_joint_add()
    	bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')
    	bpy.ops.transform.resize(value=(0.25, 0.25, 0.25), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    elif s == 12:
    	bpy.ops.mesh.primitive_gear()
    	bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')
    	bpy.ops.transform.rotate(value=1.5708, axis=(1, 0, 0), constraint_axis=(True, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    	bpy.ops.transform.resize(value=(0.9, 0.9, 0.9), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    elif s == 13:
    	bpy.ops.mesh.primitive_worm_gear()
    	bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')
    	bpy.ops.transform.resize(value=(0.3, 0.3, 0.3), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    elif s == 14:
    	bpy.ops.mesh.primitive_twisted_torus_add()
    	bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')
    	bpy.ops.transform.rotate(value=1.5708, axis=(1, 0, 0), constraint_axis=(True, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    elif s == 15:
    	bpy.ops.mesh.primitive_supertoroid_add()
    	bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')
    	bpy.ops.transform.rotate(value=1.5708, axis=(1, 0, 0), constraint_axis=(True, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    elif s == 16:
    	bpy.ops.mesh.primitive_torusknot_add()
    	bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')
    	bpy.ops.transform.resize(value=(0.3, 0.3, 0.3), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    elif s == 17:
    	bpy.ops.mesh.generate_geodesic_dome()
    elif s == 18:
    	bpy.ops.mesh.primitive_brilliant_add()
    elif s == 19:
    	bpy.ops.mesh.primitive_diamond_add()
    elif s == 20:
    	bpy.ops.mesh.primitive_gem_add()
    elif s == 21:
    	bpy.ops.mesh.add_beam()
    elif s == 22:
    	bpy.ops.mesh.wall_add()
    	bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')
    	bpy.ops.transform.resize(value=(0.1, 0.1, 0.1), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    elif s == 23:
    	bpy.ops.mesh.primitive_star_add()
    	bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')
    	bpy.ops.transform.rotate(value=1.5708, axis=(1, 0, 0), constraint_axis=(True, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    elif s == 24:
    	bpy.ops.mesh.primitive_steppyramid_add(view_align=False, location=(0, 0, 0), rotation=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    elif s == 25:
    	bpy.ops.mesh.honeycomb_add(layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False), view_align=False, location=(0, 0, 0), rotation=(1.5708, -0, 0))
    	bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')
    	bpy.ops.transform.resize(value=(0.8, 0.8, 0.8), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    	bpy.context.object.rotation_euler[0] -= 1.5708*rx*0.9-0.785398
    	bpy.context.object.rotation_euler[1] -= 1.5708*ry*0.9-0.785398
    	bpy.context.object.rotation_euler[2] -= 1.5708*rz*0.9-0.785398
    elif s == 26:
    	bpy.ops.mesh.primitive_teapot_add()
    	bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')
    	bpy.ops.transform.resize(value=(0.3, 0.3, 0.3), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    elif s == 27:
    	bpy.ops.mesh.menger_sponge_add(view_align=False, location=(0, 0, 0), rotation=(0, -0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    bpy.ops.object.shade_smooth()
    bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')
    bpy.context.object.rotation_euler[0] += 1.5708*rx-0.785398
    bpy.context.object.rotation_euler[1] += 1.5708*ry-0.785398
    bpy.context.object.rotation_euler[2] += 1.5708*rz-0.785398
    bpy.context.object.location[0] = x
    bpy.context.object.location[1] = y
    bpy.context.object.location[2] = z
    plane = bpy.context.active_object
    # Create a new material
    material = bpy.data.materials.new(name="Plane Light Emission Shader")
    material.use_nodes = True

    # Remove default
    material.node_tree.nodes.remove(material.node_tree.nodes.get('Diffuse BSDF'))
    material_output = material.node_tree.nodes.get('Material Output')
    if mm == 0:
        emission = material.node_tree.nodes.new('ShaderNodeBsdfDiffuse')
        emission.inputs[1].default_value = m
    elif mm == 1:
        emission = material.node_tree.nodes.new('ShaderNodeBsdfGlass')
        emission.inputs[1].default_value = m
    elif mm == 2:
        emission = material.node_tree.nodes.new('ShaderNodeBsdfGlossy')
        emission.inputs[1].default_value = m
    elif mm == 3:
        emission = material.node_tree.nodes.new('ShaderNodeBsdfPrincipled')
        emission.inputs[4].default_value = m
    elif mm == 4:
        emission = material.node_tree.nodes.new('ShaderNodeBsdfTranslucent')
    
    emission.inputs[0].default_value = c
    # link emission shader to material
    material.node_tree.links.new(material_output.inputs[0], emission.outputs[0])

    # set activer material to your new material
    plane.active_material = material

for z in range(1, 399, 3):
    for x in range(1, 12, 3):
        rx = random.random()
        ry = random.random()
        rz = random.random()
        mm = random.randint(0, 4)
        m = random.random()
        s = random.randint(0, 27)
        c = (random.random(), random.random(), random.random(), 1)
        cream(x, 1, z, c, s, m, mm, rx, ry, rz)
        rx = random.random()
        ry = random.random()
        rz = random.random()
        cream(x-15, 1, z, c, s, m, mm, rx, ry, rz)
        