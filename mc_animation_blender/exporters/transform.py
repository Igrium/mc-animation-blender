import bpy
import math
import mathutils
from mc_animation_blender.util import transform_utils

# Write a basic transform animation
def write_animation(context, object, id, looping, resetWhenDone):
    frames = []

    # Get start coordinates
    startCoords = object.location.copy()

    # Write all frames into array
    for i in range(context.scene.frame_start, context.scene.frame_end):
        frames.append(write_frame(context, object, startCoords, i))

    return frames

# Returns a dictionary with a single frame of animation
def write_frame(context, object, startCoords, frame):
    context.scene.frame_set(frame)

    # Get relative coords
    coords = object.location-startCoords

    # Account for difference in axes between Minecraft and Blender
    mcCoords = transform_utils.convertLoc(coords)
    location = [mcCoords.x, mcCoords.y, mcCoords.z]
    xrot = math.degrees(object.rotation_euler.z)*-1
    
    # Cameras have to be rotated down 90 degrees
    if object.type=='CAMERA':
        yrot = (math.degrees(object.rotation_euler.x)-90)*-1
    else:
        yrot = math.degrees(object.rotation_euler.x)*-1
    
    rotation = [xrot,yrot]

    frame = {
        "loc":location,
        "rot":rotation
    }

    return frame

# Gets the minecraft coordinates of an object
def getTransform(context, originCoords, object):
    # write_frame() returns blenderCoords - startCoords, and we need blenderCoords + minecraftCoords, 
    # so if we substitute startCoords with the opposite of minecraftCoords, write_frame() does all the work for us.

    originCoordsBlender = transform_utils.convertLoc(originCoords)
    frame = write_frame(context, object, originCoordsBlender*-1, context.scene.frame_current)

    print("tp @s "+str(frame['loc'][0])+" "+str(frame['loc'][1])+" "+str(frame['loc'][2])+" "+str(frame['rot'][0])+" "+str(frame['rot'][1]))
    return frame
    