from maya import cmds
import pymel.core as pymel
from maya import OpenMaya
import maya.OpenMayaUI as omui
import logging
from base_data_node import BaseDataNode

log = logging.getLogger('maya_game_fbx_exporter')

class CharacterDataNode(BaseDataNode):
    """
    Class representing a character data node used by the tool. It will be used to define and stock
    character information for the tool directly in the scene using libSerialization
    """

    def __init__(self):
        """
        Character data node init
        """
        super(CharacterDataNode, self).__init__()

        self.character_name = 'Unknown' # Name of the character
        self.root_node = None # Root node associated to the character
        self.skeletal_meshes = []

    # TODO - Probably implement an interface for the different network node
    def is_valid(self):
        """
        Check if the node is valid for serialization

        :return: True or False depending of if the node is valid or not
        """

        if not self.root_node:
            log.warning("Couldn't save character {0} since no valid root have been set on it".
                        format(self.character_name))
            return False

        return True

    def set_root_node(self, new_root):
        """
        Setup a root node for this character. Must be a joint

        :param new_root: The new node to set as root
        :return: True or False depending of if the new root is a valid one
        """

        if pymel.general.nodeType(new_root) != 'joint':
            log.warning("Can't set root joint if this is not a joint type node ({0})".format(new_root))
            return False

        self.root_node = new_root
        return True

    def add_skeletal_mesh(self, meshes):
        """
        Add mesh node to the list of meshes used by this character

        :param meshes: List of the different meshes to add
        """

        for sel in meshes:
            # at the moment, we support only mesh type node, so we need to ensure we have the too shape type
            shape = None
            try:
                shape = sel.getShape()
            except:
                log.warning("Can't add skeletal mesh if no shape are found on the node ({0})".format(sel))

            if pymel.general.nodeType(shape) != 'mesh':
                log.warning("Can't add skeletal mesh if the current node doesn't have a a mesh shape ({0})".format(sel))
                break
            if not shape.listConnections(t='skinCluster'):
                log.warning("Can't add skeletal mesh if not skin is connected on it ({0})".format(sel))
                break
            # TODO - Possibly add a check to ensure that the skin joints match the root hierarchy
            if not sel in self.skeletal_meshes:
                self.skeletal_meshes.append(sel)