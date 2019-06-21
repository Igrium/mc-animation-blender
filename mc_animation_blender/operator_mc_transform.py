import bpy
import mathutils
from mc_animation_blender.util import transform_utils

class MC_Transform_Operator(bpy.types.Operator):
    bl_idname = "mcanim.minecraft_transform"
    bl_label = "Get Minecraft Transform"

    originCoords = bpy.props.FloatVectorProperty(name="Origin Coordinates",
     description="The Minecraft coordinates of the Blender origin",
     default=(0.0, 0.0, 0.0))

    def invoke(self, context, event):
        wm = context.window_manager
        return wm.invoke_props_dialog(self)

    def execute(self, context):
        # Create vector object of origin coords
        originCoordsVector = mathutils.Vector((self.originCoords[0],
        self.originCoords[1],
        self.originCoords[2]))

        loc, rot = getMinecraftTransform(context, originCoordsVector, context.view_layer.objects.active)
        self.report({'PROPERTY'}, "Location: "+str(loc)+" Rotation: "+str(rot))
        self.report({'PROPERTY'}, "Use command: tp @s "+str(loc[0])+" "+str(+loc[1])+" "+str(loc[2])+
        " "+str(rot[0])+" "+str(rot[1]))

        return {'FINISHED'}

  # Gets the minecraft coordinates of an object
def getMinecraftTransform(context, originCoords, object):
    # getTransform() returns blenderCoords - startCoords, and we need blenderCoords + originCoords(Blender), 
    # so if we substitute startCoords with the opposite of originCoords, getTransform() does all the work for us.

    originCoordsBlender = transform_utils.convertLoc(originCoords)
    loc, rot = transform_utils.getTransform(context, object, originCoordsBlender*-1)
    
    return loc, rot

def register():
    bpy.utils.register_class(MC_Transform_Operator)

def unregister():
    bpy.utils.unregister_class(MC_Transform_Operator)