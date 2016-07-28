from yowsup.layers.network import YowNetworkLayer
from yowsup.layers import YowLayerEvent
from yowsup.stacks import YowStackBuilder
from palayer import PictureArchiverLayer
from config import CREDENTIALS

if __name__==  "__main__":
    stackbuilder = YowStackBuilder()

    stack = stackbuilder.pushDefaultLayers(True).push(PictureArchiverLayer).build()

    stack.setCredentials(CREDENTIALS)
    stack.broadcastEvent(YowLayerEvent(YowNetworkLayer.EVENT_STATE_CONNECT))

    stack.loop()

