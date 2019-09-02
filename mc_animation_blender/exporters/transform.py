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

    location, rotation = transform_utils.getTransform(context, object, startCoords)

    frame = {
        "loc":location,
        "rot":rotation
    }

    return frame

