import bpy
from mc_animation_blender.util import transform_utils

class MC_Transform_Operator(bpy.types.Operator):
    bl_idname = "mcanim.minecraft_transform"
    bl_label = "Get Minecraft Transform"

    originCoords = bpy.props.FloatVectorProperty(name="Origin Coordinates",
     description="The Minecraft coordinates of the Blender origin")

    def execute(self, context):
        print("executing mc_transform")
        loc, rot = getMinecraftTransform(context, self.originCoords, context.view_layer.objects.active)
        self.report({'PROPERTY'}, "Location: "+str(loc)+" Rotation: "+str(rot))

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