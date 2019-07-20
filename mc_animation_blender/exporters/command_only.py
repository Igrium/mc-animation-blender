# Write an empty animation so commands can be added
def write_animation(context):
    frames = []
    # Add empty frames into array so compiler can count them
    for i in range(context.scene.frame_start, context.scene.frame_end):
        frames.append({})

    return frames
