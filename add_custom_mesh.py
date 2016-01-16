import bpy
import mathutils

bl_info = {
		"name": "Add Custom Mesh",
		"description": "Adds custom meshes to the Add Mesh menu",
		"author": "pmurphy",
		"version": (1, 1),
		"blender": (2, 74),
		"location": "View3D > Add > Mesh",
		"warning": "",
		"wiki_url": "",
		"category": "Add Mesh"
}

import bpy
import mathutils

class addPipeOp(bpy.types.Operator):
	bl_idname = "mesh.primitive_pipe_add"
	bl_label = "Pipe"
	bl_options = {'REGISTER', 'UNDO'}

	def execute(self, context):
		
		verts = [(0.0, 1.0, -1.0), (-0.19508881866931915, 0.9807855486869812, 1.105945348739624), (0.19509032368659973, 0.9807852506637573, -1.0), (-0.38268208503723145, 0.9238801002502441, 1.105945348739624), (0.3826834559440613, 0.9238795042037964, -1.0), (-0.5555691123008728, 0.8314703702926636, 1.105945348739624), (0.5555702447891235, 0.8314695954322815, -1.0), (-0.7071058750152588, 0.707107663154602, 1.105945348739624), (0.7071067690849304, 0.7071067690849304, -1.0), (-0.831468939781189, 0.5555712580680847, 1.105945348739624), (0.8314696550369263, 0.5555701851844788, -1.0), (-0.923879086971283, 0.38268446922302246, 1.105945348739624), (0.9238795042037964, 0.3826834261417389, -1.0), (-0.980785071849823, 0.1950913518667221, 1.105945348739624), (0.9807852506637573, 0.19509035348892212, -1.0), (-1.0, 9.655991561885457e-07, 1.105945348739624), (1.0, 7.549790126404332e-08, -1.0), (-0.9807854294776917, -0.1950894594192505, 1.105945348739624), (0.9807853102684021, -0.19509020447731018, -1.0), (-0.923879861831665, -0.3826826810836792, 1.105945348739624), (0.9238795638084412, -0.38268327713012695, -1.0), (-0.8314700126647949, -0.5555696487426758, 1.105945348739624), (0.8314696550369263, -0.5555701851844788, -1.0), (-0.7071072459220886, -0.707106351852417, 1.105945348739624), (0.7071067690849304, -0.7071067690849304, -1.0), (-0.5555707216262817, -0.8314692974090576, 1.105945348739624), (0.5555701851844788, -0.8314696550369263, -1.0), (-0.3826838731765747, -0.9238793253898621, 1.105945348739624), (0.38268327713012695, -0.9238796234130859, -1.0), (-0.19509072601795197, -0.9807851910591125, 1.105945348739624), (0.19509008526802063, -0.9807853102684021, -1.0), (-3.2584136988589307e-07, -1.0, 1.105945348739624), (-3.2584136988589307e-07, -1.0, -1.0), (0.19509008526802063, -0.9807853102684021, 1.105945348739624), (-0.19509072601795197, -0.9807851910591125, -1.0), (0.38268327713012695, -0.9238796234130859, 1.105945348739624), (-0.3826838731765747, -0.9238793253898621, -1.0), (0.5555701851844788, -0.8314696550369263, 1.105945348739624), (-0.5555707216262817, -0.8314692974090576, -1.0), (0.7071067690849304, -0.7071067690849304, 1.105945348739624), (-0.7071072459220886, -0.707106351852417, -1.0), (0.8314696550369263, -0.5555701851844788, 1.105945348739624), (-0.8314700126647949, -0.5555696487426758, -1.0), (0.9238795638084412, -0.38268327713012695, 1.105945348739624), (-0.923879861831665, -0.3826826810836792, -1.0), (0.9807853102684021, -0.19509020447731018, 1.105945348739624), (-0.9807854294776917, -0.1950894594192505, -1.0), (1.0, 7.549790126404332e-08, 1.105945348739624), (-1.0, 9.655991561885457e-07, -1.0), (0.9807852506637573, 0.19509035348892212, 1.105945348739624), (-0.980785071849823, 0.1950913518667221, -1.0), (0.9238795042037964, 0.3826834261417389, 1.105945348739624), (-0.923879086971283, 0.38268446922302246, -1.0), (0.8314696550369263, 0.5555701851844788, 1.105945348739624), (-0.831468939781189, 0.5555712580680847, -1.0), (0.7071067690849304, 0.7071067690849304, 1.105945348739624), (-0.7071058750152588, 0.707107663154602, -1.0), (0.5555702447891235, 0.8314695954322815, 1.105945348739624), (-0.5555691123008728, 0.8314703702926636, -1.0), (0.3826834559440613, 0.9238795042037964, 1.105945348739624), (-0.38268208503723145, 0.9238801002502441, -1.0), (0.19509032368659973, 0.9807852506637573, 1.105945348739624), (-0.19508881866931915, 0.9807855486869812, -1.0), (0.0, 1.0, 1.105945348739624), (-3.507657453383217e-08, 0.908132791519165, -1.0), (0.17716790735721588, 0.8906832337379456, -1.0), (0.3475273847579956, 0.8390052318572998, -1.0), (0.5045315623283386, 0.755084753036499, -1.0), (0.6421468257904053, 0.6421468257904053, -1.0), (0.7550848722457886, 0.5045315027236938, -1.0), (0.8390052318572998, 0.3475273847579956, -1.0), (0.8906832337379456, 0.17716793715953827, -1.0), (0.908132791519165, 6.139849517694529e-08, -1.0), (0.8906832933425903, -0.17716780304908752, -1.0), (0.8390052914619446, -0.3475272059440613, -1.0), (0.7550848126411438, -0.5045315027236938, -1.0), (0.6421468257904053, -0.6421468257904053, -1.0), (0.5045315027236938, -0.7550848722457886, -1.0), (0.34752723574638367, -0.8390053510665894, -1.0), (0.17716771364212036, -0.8906832933425903, -1.0), (-2.976425435008423e-07, -0.908132791519165, -1.0), (-0.17716827988624573, -0.8906831741333008, -1.0), (-0.34752777218818665, -0.8390051126480103, -1.0), (-0.504531979560852, -0.7550845146179199, -1.0), (-0.6421472430229187, -0.6421464681625366, -1.0), (-0.7550851702690125, -0.5045310258865356, -1.0), (-0.8390055894851685, -0.3475266695022583, -1.0), (-0.8906834125518799, -0.1771671324968338, -1.0), (-0.908132791519165, 8.816904824016092e-07, -1.0), (-0.8906830549240112, 0.1771688461303711, -1.0), (-0.8390048742294312, 0.3475283086299896, -1.0), (-0.755084216594696, 0.5045324563980103, -1.0), (-0.6421459913253784, 0.6421476602554321, -1.0), (-0.5045304894447327, 0.7550854682922363, -1.0), (-0.3475261330604553, 0.8390057682991028, -1.0), (-0.17716652154922485, 0.8906835317611694, -1.0), (-3.507657453383217e-08, 0.908132791519165, 1.105945348739624), (0.17716790735721588, 0.8906832337379456, 1.105945348739624), (0.3475273847579956, 0.8390052318572998, 1.105945348739624), (0.5045315623283386, 0.755084753036499, 1.105945348739624), (0.6421468257904053, 0.6421468257904053, 1.105945348739624), (0.7550848722457886, 0.5045315027236938, 1.105945348739624), (0.8390052318572998, 0.3475273847579956, 1.105945348739624), (0.8906832337379456, 0.17716793715953827, 1.105945348739624), (0.908132791519165, 6.139849517694529e-08, 1.105945348739624), (0.8906832933425903, -0.17716780304908752, 1.105945348739624), (0.8390052914619446, -0.3475272059440613, 1.105945348739624), (0.7550848126411438, -0.5045315027236938, 1.105945348739624), (0.6421468257904053, -0.6421468257904053, 1.105945348739624), (0.5045315027236938, -0.7550848722457886, 1.105945348739624), (0.34752723574638367, -0.8390053510665894, 1.105945348739624), (0.17716771364212036, -0.8906832933425903, 1.105945348739624), (-2.976425435008423e-07, -0.908132791519165, 1.105945348739624), (-0.17716827988624573, -0.8906831741333008, 1.105945348739624), (-0.34752777218818665, -0.8390051126480103, 1.105945348739624), (-0.504531979560852, -0.7550845146179199, 1.105945348739624), (-0.6421472430229187, -0.6421464681625366, 1.105945348739624), (-0.7550851702690125, -0.5045310258865356, 1.105945348739624), (-0.8390055894851685, -0.3475266695022583, 1.105945348739624), (-0.8906834125518799, -0.1771671324968338, 1.105945348739624), (-0.908132791519165, 8.816904824016092e-07, 1.105945348739624), (-0.8906830549240112, 0.1771688461303711, 1.105945348739624), (-0.8390048742294312, 0.3475283086299896, 1.105945348739624), (-0.755084216594696, 0.5045324563980103, 1.105945348739624), (-0.6421459913253784, 0.6421476602554321, 1.105945348739624), (-0.5045304894447327, 0.7550854682922363, 1.105945348739624), (-0.3475261330604553, 0.8390057682991028, 1.105945348739624), (-0.17716652154922485, 0.8906835317611694, 1.105945348739624)]
		polygons = [(80, 112, 111, 79), (96, 63, 1, 127), (127, 1, 3, 126), (126, 3, 5, 125), (125, 5, 7, 124), (124, 7, 9, 123), (123, 9, 11, 122), (122, 11, 13, 121), (121, 13, 15, 120), (120, 15, 17, 119), (119, 17, 19, 118), (118, 19, 21, 117), (117, 21, 23, 116), (116, 23, 25, 115), (115, 25, 27, 114), (114, 27, 29, 113), (113, 29, 31, 112), (112, 31, 33, 111), (111, 33, 35, 110), (110, 35, 37, 109), (109, 37, 39, 108), (108, 39, 41, 107), (107, 41, 43, 106), (106, 43, 45, 105), (105, 45, 47, 104), (104, 47, 49, 103), (103, 49, 51, 102), (102, 51, 53, 101), (101, 53, 55, 100), (100, 55, 57, 99), (99, 57, 59, 98), (98, 59, 61, 97), (97, 61, 63, 96), (65, 64, 0, 2), (66, 65, 2, 4), (67, 66, 4, 6), (68, 67, 6, 8), (69, 68, 8, 10), (70, 69, 10, 12), (71, 70, 12, 14), (72, 71, 14, 16), (73, 72, 16, 18), (74, 73, 18, 20), (75, 74, 20, 22), (76, 75, 22, 24), (77, 76, 24, 26), (78, 77, 26, 28), (79, 78, 28, 30), (80, 79, 30, 32), (81, 80, 32, 34), (82, 81, 34, 36), (83, 82, 36, 38), (84, 83, 38, 40), (85, 84, 40, 42), (86, 85, 42, 44), (87, 86, 44, 46), (88, 87, 46, 48), (89, 88, 48, 50), (90, 89, 50, 52), (91, 90, 52, 54), (92, 91, 54, 56), (93, 92, 56, 58), (94, 93, 58, 60), (95, 94, 60, 62), (64, 95, 62, 0), (0, 63, 61, 2), (24, 39, 37, 26), (95, 127, 126, 94), (34, 29, 27, 36), (44, 19, 17, 46), (73, 105, 104, 72), (88, 120, 119, 87), (54, 9, 7, 56), (66, 98, 97, 65), (81, 113, 112, 80), (64, 96, 127, 95), (10, 53, 51, 12), (20, 43, 41, 22), (74, 106, 105, 73), (89, 121, 120, 88), (30, 33, 31, 32), (40, 23, 21, 42), (67, 99, 98, 66), (50, 13, 11, 52), (82, 114, 113, 81), (60, 3, 1, 62), (75, 107, 106, 74), (90, 122, 121, 89), (6, 57, 55, 8), (16, 47, 45, 18), (68, 100, 99, 67), (83, 115, 114, 82), (26, 37, 35, 28), (36, 27, 25, 38), (46, 17, 15, 48), (76, 108, 107, 75), (91, 123, 122, 90), (56, 7, 5, 58), (69, 101, 100, 68), (2, 61, 59, 4), (84, 116, 115, 83), (12, 51, 49, 14), (22, 41, 39, 24), (77, 109, 108, 76), (92, 124, 123, 91), (32, 31, 29, 34), (70, 102, 101, 69), (42, 21, 19, 44), (85, 117, 116, 84), (52, 11, 9, 54), (62, 1, 63, 0), (78, 110, 109, 77), (93, 125, 124, 92), (8, 55, 53, 10), (18, 45, 43, 20), (71, 103, 102, 70), (86, 118, 117, 85), (28, 35, 33, 30), (38, 25, 23, 40), (48, 15, 13, 50), (79, 111, 110, 78), (94, 126, 125, 93), (58, 5, 3, 60), (72, 104, 103, 71), (87, 119, 118, 86), (4, 59, 57, 6), (14, 49, 47, 16), (65, 97, 96, 64)]
		
		mesh = bpy.data.meshes.new("Pipe_mesh")
		object = bpy.data.objects.new("Pipe", mesh)

		object.location = bpy.context.scene.cursor_location
		bpy.context.scene.objects.link(object)

		mesh.from_pydata(verts, [], polygons)
		mesh.update(calc_edges=True)
		
		return{'FINISHED'}

class addOctahedronOp(bpy.types.Operator):
	bl_idname = "mesh.primitive_octahedron_add"
	bl_label = "Octahedron"
	bl_options = {'REGISTER', 'UNDO'}
	
	def execute(self, context):
		verts = [(1.0, 1.0, -1.5099580252808664e-07), (-1.0, 1.0, -1.5099580252808664e-07), (0.0, -1.5099580252808664e-07, -1.0), (1.0, -1.0, 0.0), (-1.0, -1.0, 0.0), (0.0, 0.0, 1.0)] 

		polygons = [(0, 1, 2), (3, 4, 5), (4, 3, 2), (3, 0, 2), (1, 4, 2), (1, 0, 5), (0, 3, 5), (4, 1, 5)] 

		mesh = bpy.data.meshes.new("octahedron_mesh")
		object = bpy.data.objects.new("octahedron", mesh)

		object.location = bpy.context.scene.cursor_location
		bpy.context.scene.objects.link(object)

		mesh.from_pydata(verts, [], polygons)
		mesh.update(calc_edges=True)
		
		return{'FINISHED'}

#ENDOPERATORS
		
class INFO_MT_mesh_custom_menu_add(bpy.types.Menu):
	bl_idname = "INFO_MT_mesh_custom_menu_add"
	bl_label = "customMenu"
	
	def draw(self, context):
		layout = self.layout
		layout.operator("mesh.primitive_pipe_add", text="Add Pipe")
		layout.operator("mesh.primitive_octahedron_add", text = "Add Octahedron")
		#ENDDRAW

# Register all operators and panels

# Define menu
def menu_func(self, context):
	self.layout.menu("INFO_MT_mesh_custom_menu_add", icon="PLUGIN")

def register():
	bpy.utils.register_module(__name__)
	bpy.types.INFO_MT_mesh_add.append(menu_func)

def unregister():
	bpy.utils.unregister_module(__name__)
	bpy.types.INFO_MT_mesh_add.remove(menu_func)

