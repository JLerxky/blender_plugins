import bpy


class ResizeOperator(bpy.types.Operator):
    bl_idname = "jler.resize"
    bl_label = "Resize"

    filter_glob: bpy.props.StringProperty(default='*.glb', options={'HIDDEN'})
    filepath: bpy.props.StringProperty(subtype="FILE_PATH")
    filename: bpy.props.StringProperty(subtype="FILE_NAME")
    directory: bpy.props.StringProperty(
        subtype="DIR_PATH",
        name="Outdir Path",
        description="返回一个文件夹路径"
    )
    files: bpy.props.CollectionProperty(
        name="File Path",
        type=bpy.types.OperatorFileListElement,
    )

    def execute(self, context):
        print(self.filepath)
        for file in self.files:
            resize(self.directory, file.name)
        return {'FINISHED'}

    def invoke(self, context, event):
        context.window_manager.fileselect_add(self)
        return {'RUNNING_MODAL'}

def menu_func(self, context):
    self.layout.operator(ResizeOperator.bl_idname, text="批量Resize")

def register():
    bpy.utils.register_class(ResizeOperator)
    bpy.types.VIEW3D_MT_view.append(menu_func)# Adds the new operator to an existing menu.

def unregister():
    bpy.utils.unregister_class(ResizeOperator)

def resize(filepath, filename):
    # clean
    bpy.ops.object.select_all(action='DESELECT')
    
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete()

    # import
    bpy.ops.import_scene.gltf(
        filepath=filepath + filename,
        files=[{"name":filename}],
        loglevel=50
    )


    # resize
    bpy.ops.object.select_all(action='DESELECT')
    bpy.ops.object.select_hierarchy(direction='PARENT', extend=False)
    bpy.ops.object.select_hierarchy(direction='CHILD', extend=False)
    bpy.ops.object.select_hierarchy(direction='CHILD', extend=False)
    bpy.ops.object.select_hierarchy(direction='CHILD', extend=False)
    bpy.ops.object.select_hierarchy(direction='CHILD', extend=False)
    bpy.ops.object.select_hierarchy(direction='CHILD', extend=False)
    bpy.ops.object.select_hierarchy(direction='CHILD', extend=False)
    bpy.ops.object.select_hierarchy(direction='CHILD', extend=False)
    bpy.ops.object.select_hierarchy(direction='CHILD', extend=False)
    bpy.ops.object.select_hierarchy(direction='CHILD', extend=False)
    bpy.ops.object.select_hierarchy(direction='CHILD', extend=False)
    bpy.ops.object.select_hierarchy(direction='CHILD', extend=False)
    bpy.ops.object.select_hierarchy(direction='CHILD', extend=False)
    bpy.ops.object.select_hierarchy(direction='CHILD', extend=False)
    bpy.ops.object.select_hierarchy(direction='CHILD', extend=False)
    bpy.ops.object.select_hierarchy(direction='CHILD', extend=False)
    bpy.ops.object.select_hierarchy(direction='CHILD', extend=False)
    bpy.ops.object.select_hierarchy(direction='CHILD', extend=False)
    bpy.ops.object.select_hierarchy(direction='CHILD', extend=False)
    bpy.ops.object.select_hierarchy(direction='CHILD', extend=False)
    bpy.ops.object.select_hierarchy(direction='CHILD', extend=False)
    bpy.ops.object.select_hierarchy(direction='CHILD', extend=False)
    bpy.ops.object.select_hierarchy(direction='CHILD', extend=False)
    bpy.ops.object.select_hierarchy(direction='CHILD', extend=False)
    bpy.ops.object.select_hierarchy(direction='CHILD', extend=False)
    bpy.ops.object.select_hierarchy(direction='CHILD', extend=False)
    bpy.ops.object.select_hierarchy(direction='CHILD', extend=False)
    bpy.ops.object.select_hierarchy(direction='CHILD', extend=False)
    bpy.ops.object.select_hierarchy(direction='CHILD', extend=False)
    bpy.ops.object.select_hierarchy(direction='CHILD', extend=False)
    bpy.ops.object.select_hierarchy(direction='CHILD', extend=False)
    bpy.ops.object.select_hierarchy(direction='CHILD', extend=False)
    bpy.ops.object.select_hierarchy(direction='CHILD', extend=False)
    bpy.ops.object.select_hierarchy(direction='CHILD', extend=False)
    bpy.ops.object.select_hierarchy(direction='CHILD', extend=False)
    bpy.ops.object.select_hierarchy(direction='CHILD', extend=False)
    bpy.ops.object.select_hierarchy(direction='CHILD', extend=False)
    bpy.ops.object.select_hierarchy(direction='CHILD', extend=False)
    bpy.ops.object.select_hierarchy(direction='CHILD', extend=False)
    bpy.ops.object.select_hierarchy(direction='CHILD', extend=False)
    bpy.ops.object.select_hierarchy(direction='CHILD', extend=False)
    bpy.ops.object.select_hierarchy(direction='CHILD', extend=False)
    bpy.ops.object.select_hierarchy(direction='CHILD', extend=False)
    bpy.ops.object.select_hierarchy(direction='CHILD', extend=False)
    bpy.ops.object.select_hierarchy(direction='CHILD', extend=False)
    bpy.ops.object.select_hierarchy(direction='CHILD', extend=False)
    bpy.ops.object.select_hierarchy(direction='CHILD', extend=False)
    bpy.ops.object.select_hierarchy(direction='CHILD', extend=False)
    bpy.ops.object.select_hierarchy(direction='CHILD', extend=False)
    bpy.ops.object.select_hierarchy(direction='CHILD', extend=False)
    bpy.ops.object.select_hierarchy(direction='CHILD', extend=False)
    bpy.ops.object.select_by_type(extend=False, type='MESH')
    bpy.ops.object.editmode_toggle()
    bpy.ops.transform.resize(
        value=(2.0, 2.0, 2.0),
        orient_type='GLOBAL',
        orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)),
        orient_matrix_type='GLOBAL',
        mirror=True,
        use_proportional_edit=False,
        proportional_edit_falloff='SMOOTH',
        proportional_size=1,
        use_proportional_connected=False,
        use_proportional_projected=False,
        release_confirm=True
    )
    bpy.ops.object.editmode_toggle()
    
    # export
    bpy.ops.object.select_all(action='DESELECT')
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.export_scene.gltf(
        filepath=filepath + "2x_" + filename
    )
    bpy.ops.object.select_all(action='DESELECT')


if __name__ == "__main__":
   register()
#    bpy.ops.wm.hello_world()
