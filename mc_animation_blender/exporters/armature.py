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

    body_v = transform_utils.rotation_to_array(transform_utils.get_rotation(bones['body']), True)
    left_arm_v = transform_utils.rotation_to_array(transform_utils.get_rotation(bones['left_arm']), False)
    right_arm_v = transform_utils.rotation_to_array(transform_utils.get_rotation(bones['right_arm']), False)
    left_leg_v = transform_utils.rotation_to_array(transform_utils.get_rotation(bones['left_leg']), False)
    right_leg_v = transform_utils.rotation_to_array(transform_utils.get_rotation(bones['right_leg']), False)
    head_v = transform_utils.rotation_to_array(transform_utils.get_rotation(bones['head']), False)
    
    # construct frame
    frame = {
        "location": {
            "x": location[0],
            "y": location[1],
            "z": location[2]
        },
        "rotation": {
            "x": rotation[0],
            "z": rotation[1]
        },
        "pose": {
            "body": {
                "x": body_v[0],
                "y": body_v[1],
                "z": body_v[2]
            },
            "leftArm": {
                "x": left_arm_v[0],
                "y": left_arm_v[1],
                "z": left_arm_v[2]
            },
            "rightArm": {
                "x": right_arm_v[0],
                "y": right_arm_v[1],
                "z": right_arm_v[2]
            },
            "leftLeg": {
                "x": left_leg_v[0],
                "y": left_leg_v[1],
                "z": left_leg_v[2]
            },
            "rightLeg": {
                "x": right_leg_v[0],
                "y": right_leg_v[1],
                "z": right_leg_v[2]
            },
            "head": {
                "x": head_v[0],
                "y": head_v[1],
                "z": head_v[2]
            }
        }
    }

    return frame
