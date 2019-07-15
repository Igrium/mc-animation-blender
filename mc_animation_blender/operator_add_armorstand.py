import bpy
import os


from bpy.props import (
    BoolProperty,
    BoolVectorProperty,
    FloatProperty,
    FloatVectorProperty,
)


class AddBox(bpy.types.Operator):
    """Add a simple box mesh"""
    bl_idname = "mcanim.add_armorstand"
    bl_label = "Add Armor Stand Rig"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        # Append armor stand
        blendfile = os.path.abspath("mc_animation_blender/resources/armor_stand.blend")
        section   = "\\Collection\\"
        object    = "ArmorStand"

        filepath  = blendfile + section + object
        directory = blendfile + section
        filename  = object

        bpy.ops.wm.append(
            filepath=filepath, 
            filename=filename,
            directory=directory)

        return {'FINISHED'}


def menu_func(self, context):
    self.layout.operator(AddBox.bl_idname, icon='MESH_CUBE')


def register():
    bpy.utils.register_class(AddBox)
    bpy.types.VIEW3D_MT_mesh_add.append(menu_func)


def unregister():
    bpy.utils.unregister_class(AddBox)
    bpy.types.VIEW3D_MT_mesh_add.remove(menu_func)


if __name__ == "__main__":
    register()

    # test call
    bpy.ops.mesh.primitive_box_add()
