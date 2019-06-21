# Converts Blender coords to Minecraft
import mathutils
import math

# Get the Minecraft transformation of an object relative to (blender coordinates) startCoords
def getTransform(context, object, startCoords):

    # Get relative coords
    coords = object.location-startCoords

    # Account for difference in axes between Minecraft and Blender
    mcCoords = convertLoc(coords)
    location = [mcCoords.x, mcCoords.y, mcCoords.z]
    xrot = math.degrees(object.rotation_euler.z)*-1
    
    # Cameras have to be rotated down 90 degrees
    if object.type=='CAMERA':
        yrot = (math.degrees(object.rotation_euler.x)-90)*-1
    else:
        yrot = math.degrees(object.rotation_euler.x)*-1
    
    rotation = [xrot,yrot]

    return (location, rotation)

def convertLoc(coords):
    return mathutils.Vector((coords.x, coords.z, coords.y*-1))

