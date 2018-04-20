import bpy

bpy.ops.mesh.primitive_cube_add(radius=3, location=(1.5, 0, 1.5))
bpy.ops.transform.resize(value=(1, 0.1/3, 1))

objs = []
mats = []
glss = []

class Group:
    def __init__ (self, name, color, g_i, r, x_n, y_n, x_o, y_o, x_s, y_s, ct, yv, ff):
        self.colour = color
        self.group_index = g_i
        self.radius = r
        self.x_steps = x_n
        self.y_steps = y_n
        self.name = name
        self.x_offset = x_o
        self.y_offset = y_o
        self.x_scale = x_s
        self.y_scale = y_s
        self.count = ct
        self.y = yv
        self.first_frame = ff
        global objs
        global mats
        global glss
        objs.append([])
        mats.append([])
        glss.append([])
        

groups = []

def draw_group(group):
    group_index = group.group_index
    x_steps = group.x_steps
    y_steps = group.y_steps
    x_offset = group.x_offset
    y_offset = group.y_offset
    x_scale = group.x_scale
    y_scale = group.y_scale
    count = group.count
    y=group.y
    r = group.radius
    global mats
    global objs
    global glss
    ojs = objs[group_index]
    mts = mats[group_index]
    gss = glss[group_index]
    for x in range(0, x_steps):
        ojs.append([])
        mts.append([])
        gss.append([])
        for z in range(0, y_steps):
            bpy.ops.mesh.primitive_cube_add(radius=r, location=(x*x_scale+x_offset, y, z*y_scale+y_offset))
            bpy.ops.transform.resize(value=(1, 0.1, 1))
            bpy.ops.material.new()
            obj = bpy.context.scene.objects.active
            ojs[x].append(obj)
            
            # Create a new material
            material = bpy.data.materials.new(name="Light Emission")
            material.use_nodes = True

            # Remove default
            material.node_tree.nodes.remove(material.node_tree.nodes.get('Diffuse BSDF'))
            material_output = material.node_tree.nodes.get('Material Output')
            emission = material.node_tree.nodes.new('ShaderNodeEmission')
            mixer = material.node_tree.nodes.new('ShaderNodeMixShader')
            glass = material.node_tree.nodes.new('ShaderNodeBsdfGlass')
            emission.inputs['Strength'].default_value = 0

            # link emission shader to material
            material.node_tree.links.new(material_output.inputs[0], mixer.outputs[0])
            material.node_tree.links.new(mixer.inputs[1], glass.outputs[0])
            material.node_tree.links.new(mixer.inputs[2], emission.outputs[0])

            # set activer material to your new material
            mts[x].append([glass, emission, mixer])

            bpy.context.scene.objects.active.active_material = material

def blink(g, x, y, start, length=24):
    mat = mats[g.group_index][x][y][1]
    matx = mats[g.group_index][x][y][0]
    matxx = mats[g.group_index][x][y][2]
    matxx.inputs[0].default_value = 0
    matx.inputs[0].default_value = g.colour
    mat.inputs[0].default_value = g.colour
    mat.inputs['Strength'].default_value = 0
    matxx.inputs[0].default_value = 0
    mat.inputs[1].keyframe_insert("default_value", frame=start)
    matxx.inputs[0].keyframe_insert("default_value", frame=start)
    mat.inputs['Strength'].default_value = 1
    matxx.inputs[0].default_value = 1
    mat.inputs[1].keyframe_insert("default_value", frame=start+length/2)
    matxx.inputs[0].keyframe_insert("default_value", frame=start+length/2)
    mat.inputs['Strength'].default_value = 0
    matxx.inputs[0].default_value = 0
    mat.inputs[1].keyframe_insert("default_value", frame=start+length)
    matxx.inputs[0].keyframe_insert("default_value", frame=start+length)



c = 1

def blink_rec(w, h, g):
    l=24
    c = g.first_frame
    for y in range(g.y_steps-1,-2+h,-1):
        for x in range(0,g.x_steps+1-w,1):
            for i in range(0,w):
                for j in range(0,h):
                    blink(g,x+i,y-j,c,l)
            bpy.ops.object.text_add(location=(-1.4, 0.5, 2.5))
            bpy.ops.transform.rotate(value=1.5708, axis=(1, 0, 0))
            ob=bpy.context.object
            
            ob.data.body = str(g.count)
            bpy.context.object.data.extrude = 0.05
            bpy.context.object.data.bevel_depth = 0.01
            bpy.context.object.data.bevel_resolution = 4
            ob.keyframe_insert(data_path='location', frame=(c))
            bpy.ops.transform.translate(value=(0, -2, 0))
            ob.keyframe_insert(data_path='location', frame=(c+l/2))
            bpy.ops.transform.translate(value=(0, 4, 0))
            ob.keyframe_insert(data_path='location', frame=(c+l))
            material = bpy.data.materials.new(name="Light Emission")
            material.use_nodes = True
            emission = material.node_tree.nodes.new('ShaderNodeEmission')
            material_output = material.node_tree.nodes.get('Material Output')
            material.node_tree.links.new(material_output.inputs[0], emission.outputs[0])
            bpy.context.scene.objects.active.active_material = material
            g.count+=1
            c+=24
            g.first_frame=c


g = Group('back', (1, 0, 0, 1), 0, 0.45, 4, 4, 0, 0, 1, 1, 1, -0.1, 20)

draw_group(g)
for i in range(1,g.x_steps+1):
    blink_rec(i,i,g)

g = Group('front', (0, 1, 1, 1), 1, 0.45/2, 2, 2, 1+1/4, 2+1/4, 0.5, 0.5, 31, -0.2, 800)

draw_group(g)
for i in range(1,g.x_steps+1):
    blink_rec(i,i,g)

g = Group('front', (0, 1, 1, 1), 2, 0.45/2, 2, 2, 1+1/4, 1/4, 0.5, 0.5, 36, -0.2, 920)

draw_group(g)
for i in range(1,g.x_steps+1):
    blink_rec(i,i,g)


