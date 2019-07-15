import bpy
import math
import mathutils
from mc_animation_blender.util import transform_utils

# Writes an armature animation that animates the head based on object rotation
# (For advanced translational animations that require roll)
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

    location = transform_utils.getTransform(context, object, startCoords)[0]

    # construct frame
    frame = {
        "loc":location,
        "rot":[0,0],
        "pose": {
            "Body":[0,0,0],
			"LeftArm":[0,0,0],
			"RightArm":[0,0,0],
			"LeftLeg":[0,0,0],
			"RightLeg":[0,0,0],
			"Head":transform_utils.rotation_to_array(transform_utils.get_rotation(object), True)
        }
    }

    return frame