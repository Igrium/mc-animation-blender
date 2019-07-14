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
            "Body":convert_array(transform_utils.get_rotation(bones['body']), False),
			"LeftArm":convert_array(transform_utils.get_rotation(bones['left_arm']), False),
			"RightArm":convert_array(transform_utils.get_rotation(bones['right_arm']), False),
			"LeftLeg":convert_array(transform_utils.get_rotation(bones['left_leg']), False),
			"RightLeg":convert_array(transform_utils.get_rotation(bones['right_leg']), False),
			"Head":convert_array(transform_utils.get_rotation(bones['head']), True)
        }
    }

    return frame

# takes an array attained by armature.pose.bones[bone].rotation_euler, converts it to degrees, and does correct formulas.
def convert_array(array, isHead):
    
    if isHead:
        new_array = [array[0]*-1, array[1]*-1, array[2]]
    else:
        new_array = [array[2], array[1], array[0]*-1]  
        
    new_array[0] = round(math.degrees(new_array[0]), 2)
    new_array[1] = round(math.degrees(new_array[1]), 2)
    new_array[2] = round(math.degrees(new_array[2]), 2)
    
    return new_array
