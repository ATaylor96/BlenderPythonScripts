bl_info = {
    "name": "Resolution X Y Flipper",
    "description": "Single line explaining what this script exactly does.",
    "author": "Adam Taylor",
    "version": (1, 0),
    "blender": (3, 0, 1),
    "location": "Output Properties > Resolution X Y Flipper",
    "category": "Render",
}

import bpy
 
class flipResolutions(bpy.types.Operator):
    bl_idname = 'render.resolutionflip'
    bl_label = 'Swap X and Y Resolution Values'
 
    def execute(self, context):
        render = bpy.context.scene.render
        x = render.resolution_x
        render.resolution_x = render.resolution_y
        render.resolution_y = x
        return {"FINISHED"}
 
class panelResSwap(bpy.types.Panel):
    bl_idname = "panel.panelResSwap"
    bl_label = "Resolution X Y Flipper"
    bl_space_type = "PROPERTIES"
    bl_region_type = "WINDOW"
    bl_context = "output"
 
    def draw(self, context):
        self.layout.operator("render.resolutionflip", icon='ARROW_LEFTRIGHT', text="Swap X and Y Resolution Values")
 
def register() :
    bpy.utils.register_class(flipResolutions)
    bpy.utils.register_class(panelResSwap)
 
def unregister() :
    bpy.utils.unregister_class(flipResolutions)
    bpy.utils.unregister_class(panelResSwap)
    
if __name__ == "__main__" :
    register()