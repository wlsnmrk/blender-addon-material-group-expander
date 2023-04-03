bl_info = {
    "name": "Expand Material Groups",
    "description": "Expand all node groups in a material, preserving input values.",
    "author": "Mark Wilson",
    "version": (0, 0, 1),
    "location": "Node Editor > Node > Expand All Groups",
    "warning": "Alpha release. Will not preserve node layout. Limited input types.",
    "tracker_url": "",
    "blender": (3, 5, 0),
    "category": "Material",
}

import bpy
import mathutils


class SafeMaterialGroupExpander(bpy.types.Operator):
    """Material-Group Expander with Input Preservation"""
    bl_idname = "material.group_expander"
    bl_label = "Expand All Groups"
    bl_options = {'REGISTER', 'UNDO'}
    
    @classmethod
    def poll(cls, context):
        space = context.space_data
        return space.type == "NODE_EDITOR"

    def execute(self, context):
        space = context.space_data
        if space is None or space.node_tree is None:
            return {'CANCELLED'}
        made_change = False
        while True:
            groups = []
            for node in space.node_tree.nodes:
                if isinstance(node, bpy.types.ShaderNodeGroup):
                    height = node.height
                    total_new_node_height = 0
                    max_new_node_width = 0
                    new_nodes = []
                    for input in node.inputs:
                        if not input.is_linked:
                            if isinstance(input, bpy.types.NodeSocketColor):
                                new_node = space.node_tree.nodes.new("ShaderNodeRGB")
                                made_change = True
                            elif isinstance(input, bpy.types.NodeSocketFloat):
                                new_node = space.node_tree.nodes.new("ShaderNodeValue")
                                made_change = True
                            else:
                                raise RuntimeError("Unrecognized input type {}".format(type(input)))
                            new_node.name = "Default " + input.name
                            new_node.label = input.name
                            new_node.outputs[0].default_value = input.default_value
                            space.node_tree.links.new(new_node.outputs[0], input)
                            new_node.hide = True
                            if (new_node.width) > max_new_node_width:
                                max_new_node_width = new_node.width
                            total_new_node_height += new_node.height + 5
                            new_nodes.append(new_node)
                    pos_x = node.location[0] - max_new_node_width - 40
                    mid_y = node.location[1] + (node.height / 2)
                    start_y = mid_y + (total_new_node_height / 2)
                    used_height = 0
                    for i in range(len(new_nodes)):
                        new_nodes[i].location = mathutils.Vector((pos_x, start_y - used_height))
                        used_height += new_nodes[i].height + 5
                    groups.append(node)
                # end if node-group
            # end for node_tree loop
            if len(groups) == 0:
                break
            for node_group in groups:
                space.node_tree.nodes.active = node_group
                print("Ungrouping {}".format(node_group.name))
                bpy.ops.node.group_ungroup()
        # end while-node-groups loop
        return {'FINISHED'} if made_change else {'CANCELLED'}


def menu_func(self, context):
    self.layout.operator(SafeMaterialGroupExpander.bl_idname)


def register():
    bpy.utils.register_class(SafeMaterialGroupExpander)
    bpy.types.NODE_MT_node.append(menu_func)


def unregister():
    bpy.utils.unregister_class(SafeMaterialGroupExpander)


if __name__ == "__main__":
    register()
