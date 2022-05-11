bl_info = {
    "name": "Resolution from Background Image",
    "description": "Set the current scene resolution to that of the selected camera background image",
    "author": "Adam Taylor",
    "version": (1, 0),
    "blender": (3, 0, 1),
}

import bpy

class resolutionFromBackgroundImage(bpy.types.Operator):
    bl_idname = 'data.getbackgroundresolution'
    bl_label = 'Get Background Image Resolution'
    
    def execute(self, context):
        active_cam = bpy.context.scene.camera
        if active_cam is not None and active_cam.type == 'CAMERA':
            render = bpy.context.scene.render
            bg_images = active_cam.data.background_images
            
            for i in bg_images:
                render.resolution_x = i.image.size[0]
                render.resolution_y = i.image.size[1]

        return {"FINISHED"}


class toolPanel(bpy.types.Panel):
    
    bl_idname = 'VIEW3D_PT_example_panel'
    bl_label = 'Scene'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    
    def draw(self, context):
        self.layout.operator('data.getbackgroundresolution', text='Get Background Resolution')



CLASSES = [
    resolutionFromBackgroundImage,
    toolPanel,
]
        
def register():
    print('registered') # just for debug
    for c in CLASSES:
        bpy.utils.register_class(c)

def unregister():
    print('unregistered') # just for debug
    for c in CLASSES:
        bpy.utils.unregister_class(c)


if __name__ == '__main__':
    register()