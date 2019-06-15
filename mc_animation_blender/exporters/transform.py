import bpy
import math

# Write a basic transform animation
def write_animation(context, object, id, looping, resetWhenDone):
    frames = []

    # Write all frames into array
    for i in range(context.scene.frame_start, context.scene.frame_end):
        frames.append(write_frame(context, object, i))

    return frames

# Returns a dictionary with a single frame of animation
def write_frame(context, object, frame):
    context.scene.frame_set(frame)

    # Account for difference in axes between Minecraft and Blender
    location = [object.location.x, object.location.z, object.location.y]
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
