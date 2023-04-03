# Material Group Expander
**_This add-on is alpha code. It works well enough to be passable for the author's personal use and is not tested beyond that. It supports only Value and Color input sockets, and DOES NOT PRESERVE NODE LAYOUTS. It may contain bugs. Save a copy of your work._**

A Blender add-on that expands (un-groups) node groups in materials, preserving default values for input sockets. This is useful for exporting complex materials to GLTF, as [the GLTF exporter doesn't seem to support node groups](https://github.com/KhronosGroup/glTF-Blender-IO/issues/830).

This add-on was hacked together over a weekend with no prior experience writing Blender add-ons. It was designed for my own use exporting some models from Blender to GLTF, and has some issues I know about (see the issue tracker). It may well have others I don't know about. Please use with caution.

# Installing
Use the "Install" button from the Add-Ons panel in the Blender Preferences dialog, and point it to the expand_groups.py file.
