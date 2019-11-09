from maya import cmds
import pymel.core as pymel
from maya import OpenMaya
import maya.OpenMayaUI as omui
import logging
from base_data_node import BaseDataNode

log = logging.getLogger('maya_game_fbx_exporter')

class AnimationDataNode(BaseDataNode):
    """
    Class representing an animation data node used by the tool. It will be used to define and stock
    animation information for the tool directly in the scene using libSerialization
    """

    def __init__(self, node=''):
        """
        Anim data node init
        """
        super(AnimationDataNode, self).__init__()

        self.character_data = None # Will point on a character_data_node instance that is linked to the animation
        self.anim_base_name = '' # Will mostly be initialized with the scene name

    def is_valid(self):
        """
        Check if the node is valid for serialization

        :return: True or False depending of if the node is valid or not
        """

        if not self.character_data:
            log.warning("Couldn't save animation information {0} since no valid character have been found".
                        format(self))
            return False

        return True