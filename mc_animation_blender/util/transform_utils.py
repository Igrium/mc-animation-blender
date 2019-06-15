# Converts Blender coords to Minecraft
import mathutils

def convertLoc(coords):
    return mathutils.Vector((coords.x*-1, coords.z, coords.y))

