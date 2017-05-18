from yowsup.layers.network import YowNetworkLayer
from yowsup.stacks import YowStackBuilder
from palayer import PictureArchiverLayer
from config import CREDENTIALS
from yowsup.layers.axolotl.props import PROP_IDENTITY_AUTOTRUST

stackbuilder = YowStackBuilder()

stack = stackbuilder.pushDefaultLayers(True).push(PictureArchiverLayer).build()

stack.setCredentials(CREDENTIALS)
stack.setProp(PROP_IDENTITY_AUTOTRUST, True)
while True:
    stack.getLayerInterface(YowNetworkLayer).connect()
    stack.loop()

