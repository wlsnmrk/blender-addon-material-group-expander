# Material Group Expander
**_This add-on is alpha code and is not tested beyond light use on a personal project. It supports only Value and Color input sockets, and DOES NOT PRESERVE NODE LAYOUTS. Save a copy of your work and use with caution._**

A Blender add-on that expands (un-groups) node groups in materials, preserving default values for input sockets. This is useful for exporting complex materials to GLTF, as [the GLTF exporter doesn't support node groups](https://github.com/KhronosGroup/glTF-Blender-IO/issues/830).

# Installation
Use the "Install" button from the Add-Ons panel in the Blender Preferences dialog, and point it to the expand_groups.py file.

# Usage
In the Node Editor, open the Node menu and select the "Expand All Groups" item.
