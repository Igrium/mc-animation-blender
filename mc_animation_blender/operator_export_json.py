import bpy
import json
from . exporters import transform
from . exporters import armature
from . exporters import transform_advanced
from . exporters import command_only

def write_json(context, filepath, object, animType, id, looping, resetWhenDone, exportCommands):
    # identify correct export type and get frames
    if animType == 'TRANSFORM':
        frames = transform.write_animation(context, object, id, looping, resetWhenDone)
        typeLabel = "transform"
    elif animType == 'ARMATURE':
        frames = armature.write_animation(context, object, id, looping, resetWhenDone)
        typeLabel = "armature"
    elif animType == 'TRANSFORM_ADVANCED':
        frames = transform_advanced.write_animation(context, object, id, looping, resetWhenDone)
        typeLabel = "armature"
    elif animType == 'COMMAND_ONLY':
        frames = command_only.write_animation(context)
        typeLabel = "command_only"
    else:
        print("Unknown animation type "+animType)
        return {'CANCELED'}

    # add commands
    commands = []

    if exportCommands:
        # get all timeline markers and iterate over keys
        markers = context.scene.timeline_markers
        for k in markers.keys():
            # only add if marker starts with '/'
            if k[:1] == '/':
                commands.append({
                    "frame":markers[k].frame-context.scene.frame_start,
                    "contents":k[1:]
                })

    # add metadata
    animation = {
        "name":"remove this slot",
        "type":typeLabel,
        "id":id,
        "looping":looping,
        "resetWhenDone":resetWhenDone,
        "frames":frames,
        "commands":commands
    }

    # create json string
    formatted = json.dumps(animation, sort_keys=True, indent=4, separators=(',', ': '))

    # write file
    file = open(filepath, 'w')
    file.write(formatted)
    file.close

    print("Wrote to "+filepath)
    return {'CANCELLED'}

# ExportHelper is a helper class, defines filename and
# invoke() function which calls the file selector.
from bpy_extras.io_utils import ExportHelper
from bpy.props import StringProperty, BoolProperty, EnumProperty
from bpy.types import Operator


class MC_Export_Operator(Operator, ExportHelper):
    """This appears in the tooltip of the operator and in the generated docs"""
    bl_idname = "mcanim.export_anim"  # important since its how bpy.ops.import_test.some_data is constructed
    bl_label = "Export Minecraft Animation"

    # ExportHelper mixin class uses this
    filename_ext = ".json"

    filter_glob: StringProperty(
        default="*.json",
        options={'HIDDEN'},
        maxlen=255,  # Max internal buffer length, longer would be clamped. 
    )

    # List of operator properties, the attributes will be assigned
    # to the class instance from the operator settings before calling.
    animType = EnumProperty(
        name="Type",
        description="Animation type to export",
        items={('TRANSFORM','Transform', 'Basic transform animation (no roll)'),
         ('ARMATURE', 'Armature', 'Armor Stand animation (requires special rig)'),
         ('TRANSFORM_ADVANCED', 'Advanced Transform', 'More advanced transform w/ roll (uses armor stands)'),
         ('COMMAND_ONLY', 'Command Only', 'Only export animation commands')},
        default='TRANSFORM'
    )

    looping = BoolProperty(
        name="Looping",
        description="Should this animation loop?",
        default=True,
        )

    resetWhenDone = BoolProperty(
        name="Reset when done",
        description="Should this reset to starting position when done?",
        default=False,
        )

    id = StringProperty(
        name="ID",
        description="Unique numerical ID that Minecraft will refer to this animation by",
        default='0',
        )
    
    exportCommands = BoolProperty(
        name="Export Commands",
        description="Export markers starting with '/' as commands",
        default=True
    )

    def execute(self, context):
        return write_json(context, 
        self.filepath, 
        context.view_layer.objects.active, 
        self.animType, 
        int(self.id), 
        self.looping, 
        self.resetWhenDone, 
        self.exportCommands)


# Only needed if you want to add into a dynamic menu
def menu_func_export(self, context):
    self.layout.operator(MC_Export_Operator.bl_idname, text="Minecraft Animation (.json)")


def register():
    bpy.utils.register_class(MC_Export_Operator)
    bpy.types.TOPBAR_MT_file_export.append(menu_func_export)


def unregister():
    bpy.utils.unregister_class(MC_Export_Operator)
    bpy.types.TOPBAR_MT_file_export.remove(menu_func_export)


if __name__ == "__main__":
    register()

    # test call
    bpy.ops.export_test.some_data('INVOKE_DEFAULT')
