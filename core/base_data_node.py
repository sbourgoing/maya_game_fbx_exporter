from maya import cmds
import pymel.core as pymel
from maya import OpenMaya
import maya.OpenMayaUI as omui
import abc
import logging

log = logging.getLogger('maya_game_fbx_exporter')

class BaseDataNode(object):
    """
    Class representing a base data node that will use by the tool and save in the scene using libSerialization.
    This base node is intended to be used as an abstract class to force inherited class to implement certain
    functionnality
    """

    def __init__(self, node=''):
        """
        Base data node init
        """
        _version = [0,1,0]

    @abc.abstractmethod
    def is_valid(self):
        """
        Check if the node is valid for serialization

        :return: True or False depending of if the node is valid or not
        """

        raise NotImplementedError('Validation functionality is needed for export data node network')

    '''
    def __getNetworkName__(self):
        """
        Determine the name of the maya network.
        Override this to customize.
        Returns: The desired network name for this instance.
        """
    '''