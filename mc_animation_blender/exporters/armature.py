import bpy
import math
import mathutils
from mc_animation_blender.util import transform_utils

# Write an armature animation
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

    # get all the bones in the armature
    bones = object.pose.bones

    # construct frame
    frame = {
        "loc":location,
        "rot":rotation,
        "pose": {
            "Body":transform_utils.rotation_to_array(transform_utils.get_rotation(bones['body']), False),
			"LeftArm":transform_utils.rotation_to_array(transform_utils.get_rotation(bones['left_arm']), False),
			"RightArm":transform_utils.rotation_to_array(transform_utils.get_rotation(bones['right_arm']), False),
			"LeftLeg":transform_utils.rotation_to_array(transform_utils.get_rotation(bones['left_leg']), False),
			"RightLeg":transform_utils.rotation_to_array(transform_utils.get_rotation(bones['right_leg']), False),
			"Head":transform_utils.rotation_to_array(transform_utils.get_rotation(bones['head']), True)
        }
    }

    return frame