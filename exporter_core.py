from maya import cmds
import pymel.core as pymel
from maya import OpenMaya
import maya.OpenMayaUI as omui
import logging

log = logging.getLogger('maya_game_fbx_anim_exporter')

TOOL_PREFIX_STRING = 'mgfe_' # For maya game fbx exporter

class GameFbxExporterCore():
    """
    Core class of the exporter. Intended to be use standalone for batch purpose
    """
    def __init__(self):
        pass

    #
    ## Static functions, mostly related to data network and tools
    #

    @staticmethod
    def get_data_network():
        """
        Gather all the different exporter data network found in a scene
        :return:
        """

        all_net = pymel.ls(TOOL_PREFIX_STRING + 'net_data')
        # Support namespace
        all_net.extend(pymel.ls('*:' + TOOL_PREFIX_STRING + 'net_data'))
        # TODO - Remove me please asap
        # This is totally ugly, but got case where namespace was embedded in node name
        all_net.extend(pymel.ls('*' + TOOL_PREFIX_STRING + 'net_data'))
        if all_net:
            return all_net
        else:
            return None

    @staticmethod
    def create_data_network():
        """
        Create the new data network that can be used by the exporter
        :return:
        """

        net = pymel.createNode('network', name=TOOL_PREFIX_STRING + 'net_data')
        pymel.addAttr(net, longName='tag_as_root', at='message')
        pymel.addAttr(net, longName='tag_as_sk', at='message')
        return net

    @staticmethod
    def tag_selection_as_root(selection):
        """
        :param selection: Selection of node to tag

        Use the data network found in the scene to tag root joint
        :return:
        """

        net = GameFbxExporterCore.get_data_network()
        # TODO: Support multiple data network
        if net:
            net = net[0]
        else:
            net = GameFbxExporterCore.create_data_network()

        for sel in selection:
            if pymel.general.nodeType(sel) != 'joint':
                pymel.displayWarning("Can't tag root joint on another node than a joint ({0})".format(sel))
                break
            if sel not in net.tag_as_root.listConnections():
                pymel.connectAttr(sel.message, net.tag_as_root, f=True)

    @staticmethod
    def tag_selection_as_sk(selection):
        """
        :param selection: Selection of node to tag

        Use the data network found in the scene to tag root joint
        :return:
        """

        print selection

        net = GameFbxExporterCore.get_data_network()
        # TODO: Support multiple data network
        if net:
            net = net[0]
        else:
            net = GameFbxExporterCore.create_data_network()

        for sel in selection:
            # at the moment, we support only mesh type node, so we need to ensure we have the too shape type
            shape = None
            try:
                shape = sel.getShape()
            except:
                pymel.displayWarning("Can't tag skeletal mesh if no shape are found on the node ({0})".format(sel))
                break

            if not pymel.general.nodeType(shape) == 'mesh':
                pymel.displayWarning("Can't tag skeletal mesh on another node than with a mesh shape ({0})".format(sel))
                break
            if not shape.listConnections(t='skinCluster'):
                pymel.displayWarning("Can't tag skeletal mesh if not skin is connected on it ({0})".format(sel))
                break
            if not shape in net.tag_as_sk.listConnections():
                pymel.connectAttr(shape.message, net.tag_as_sk, f=True)