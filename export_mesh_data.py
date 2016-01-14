bl_info = {
		"name": "Export Mesh Data",
		"description": "Exports mesh data to txt file",
		"author": "pmurphy",
		"version": (1, 4),
		"blender": (2, 74),
		"location": "View3D > Tools",
		"warning": "",
		"wiki_url": "",
		"category": "Import-Export"
}

import bpy


class export_mesh_data(bpy.types.Operator):
	bl_idname = "export.export_mesh_data"
	bl_label = "Export Mesh Data"
	
	filepath = bpy.props.StringProperty(subtype="FILE_PATH")
	
	def execute(self, context):
		obverts = bpy.context.active_object.data.vertices
		obpolygons = bpy.context.active_object.data.polygons
		
		verts = []
		polygons = []
		
		for vertex in obverts:
			verts.append(tuple(vertex.co))
		
		for polygon in obpolygons:
			polygons.append(tuple(polygon.vertices))
			
		file = open(self.filepath, 'w')
		print ("Hello")
		print (len(obpolygons))
		file.write(str(verts))
		file.write("\n\n\n\n\n\n\n\n")
		file.write(str(polygons))
			
		return {'FINISHED'}
		
	def invoke(self, context, event):
		context.window_manager.fileselect_add(self)
		
		return {'RUNNING_MODAL'}
		
class export_mesh_data_panel(bpy.types.Panel):
	bl_idname = "export_mesh_data"
	bl_label = "export_mesh_data"
	bl_space_type = "VIEW_3D"
	bl_region_type = "TOOLS"
	bl_context = "objectmode"
	
	def draw(self, context):
		layout = self.layout
		layout.operator("export.export_mesh_data", text = "Export Mesh Data")

def register():
	bpy.utils.register_module(__name__)

def unregister():
	bpy.utils.unregister_module(__name__)