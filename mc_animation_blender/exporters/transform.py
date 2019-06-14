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

    # Account for difference in up axis between Minecraft and Blender
    location = [object.location.x, object.location.z, object.location.y]
    # Account for different rotation values in Minecraft and Blender
    rotation = [math.degrees(object.rotation_euler.z)*-1, math.degrees(object.rotation_euler.x)]

    frame = {
        "loc":location,
        "rot":rotation
    }

    return frame
