# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

bl_info = {
    "name" : "Minecraft Animation Tools",
    "author" : "Igrium",
    "description" : "Tools for animation in adventure maps",
    "blender" : (2, 80, 0),
    "version" : (0, 0, 1),
    "location" : "View3D",
    "warning" : "",
    "category" : "Import-Export"
}

import bpy

from . import operator_export_json
from . import operator_mc_transform

def register():
    operator_export_json.register()
    operator_mc_transform.register()

def unregister():
    operator_export_json.unregister()
    operator_mc_transform.unregister()