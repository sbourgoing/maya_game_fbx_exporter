from maya import cmds
import pymel.core as pymel
from maya import OpenMaya
import maya.OpenMayaUI as omui
import logging
from maya_game_fbx_exporter.vendor import libSerialization
reload(libSerialization)
import character_data_node
reload(character_data_node)
from character_data_node import CharacterDataNode
import animation_data_node
reload(animation_data_node)
from animation_data_node import AnimationDataNode

log = logging.getLogger('maya_game_fbx_exporter')

TOOL_PREFIX_STRING = 'mgfe_' # For maya game fbx exporter

class GameFbxExporterCore(object):
    """
    Core class of the exporter. Intended to be use standalone for batch purpose
    """
    def __init__(self):
        self.character_nodes = []
        self.anim_nodes = []

    def setup_new_character(self, name, root_node):
        """
        Create a new character data in the scene and add it to the character list
        :return: The new CharacterDataNode
        """

        # Ensure the root is not already used by another character
        for char in self.character_nodes:
            if char.root_node == root_node:
                log.error('Root node {0} is already used by another character {1}. '
                          'Please choose another root node'.format(root_node, char.character_name))
                return None
            if char.character_name == name:
                log.error('Character named {0} already exist. Please choose another name'.format(name))
                return None

        new_char = CharacterDataNode()
        new_char.character_name = name
        new_char.root_node = root_node

        self.character_nodes.append(new_char)

        libSerialization.export_network(new_char)

        return new_char

    def find_data_network(self):
        """
        Gather all network node related to the tool using libSerialization

        :return: All the network found in the scene
        """
        all_net = []

        char_networks = libSerialization.get_networks_from_class('CharacterDataNode')
        anim_networks = libSerialization.get_networks_from_class('AnimationDataNode')

        all_net.extend(char_networks)
        all_net.extend(anim_networks)

        return all_net

    def load_all_data_network(self):
        """
        Gather all the different exporter data network found in a scene
        :return:
        """

        char_networks = libSerialization.get_networks_from_class('CharacterDataNode')
        self.character_nodes = [libSerialization.import_network(network) for network in char_networks]
        self.character_nodes = filter(None, self.character_nodes)  # Prevent un-serializable networks from passing through.

        anim_networks = libSerialization.get_networks_from_class('AnimationDataNode')
        self.anim_nodes = [libSerialization.import_network(network) for network in anim_networks]
        self.anim_nodes = filter(None, self.anim_nodes)  # Prevent un-serializable networks from passing through.

    def save_data_network(self, data_node):
        """
        Save a specific network to the scene using libSerialization

        :param network: The network to save
        :return:
        """

        try:
            network = data_node._network
            if network and network.exists():
                pymel.delete(network)
            if data_node.is_valid():
                libSerialization.export_network(data_node)
        except AttributeError:
            pass


    def save_all_data_network(self):
        """
        Save all the data network information in the scene
        :return:
        """

        # Clear the existing network and resave everything if node is valid

        try:
            for char in self.character_nodes:
                network = char._network
                if network and network.exists():
                    pymel.delete(network)
                if char.is_valid():
                    libSerialization.export_network(char)
        except AttributeError:
            pass

        try:
            for anim in self.anim_nodes:
                network = anim._network
                if network and network.exists():
                    pymel.delete(network)
                if anim.is_valid():
                    libSerialization.export_network(anim)
        except AttributeError:
            pass
