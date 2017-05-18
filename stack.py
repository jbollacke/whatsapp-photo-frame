from yowsup.layers.network import YowNetworkLayer
from yowsup.stacks import YowStackBuilder
from palayer import PictureArchiverLayer
from config import CREDENTIALS

stackbuilder = YowStackBuilder()

stack = stackbuilder.pushDefaultLayers(True).push(PictureArchiverLayer).build()

stack.setCredentials(CREDENTIALS)
while True:
    stack.getLayerInterface(YowNetworkLayer).connect()
    stack.loop()

