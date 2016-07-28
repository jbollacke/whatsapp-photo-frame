from yowsup.layers.auth import YowAuthenticationProtocolLayer
from yowsup.layers.network import YowNetworkLayer
from yowsup.layers.coder import YowCoderLayer
from yowsup.common import YowConstants
from yowsup.layers import YowLayerEvent
from yowsup.stacks import YowStack, YOWSUP_CORE_LAYERS, YOWSUP_PROTOCOL_LAYERS_FULL
from yowsup.layers.axolotl import YowAxolotlLayer
from yowsup.stacks import YowStackBuilder
from palayer import PictureArchiverLayer
from config import CREDENTIALS

if __name__==  "__main__":
    stackbuilder = YowStackBuilder()

    stack = stackbuilder.pushDefaultLayers(True).push(PictureArchiverLayer).build()

    stack.setCredentials(CREDENTIALS)
    stack.broadcastEvent(YowLayerEvent(YowNetworkLayer.EVENT_STATE_CONNECT))

    stack.loop()

