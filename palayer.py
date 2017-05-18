from yowsup.layers.protocol_media.mediadownloader import MediaDownloader
from yowsup.layers.interface import YowInterfaceLayer, ProtocolEntityCallback
from yowsup.layers.protocol_messages.protocolentities import TextMessageProtocolEntity
import shutil, os
import re
from glob import glob

basepath = "files"

def nextSequenceNumber():
    key=lambda filename: int(os.path.basename(filename)[0:-4])
    files=glob(os.path.join(basepath, "*.jpg"))
    if len(files)==0:
        return 0
    files.sort(key=key)
    cur_num=key(files[-1])
    return cur_num + 1

class PictureArchiverLayer(YowInterfaceLayer):

    @ProtocolEntityCallback("message")
    def onMessage(self, messageProtocolEntity):
        if messageProtocolEntity.getType() == 'text':
            self.onTextMessage(messageProtocolEntity)
        elif messageProtocolEntity.getType() == 'media':
            self.onMediaMessage(messageProtocolEntity)

        self.toUpper(messageProtocolEntity)
        self.toLower(messageProtocolEntity.ack(True))

    @ProtocolEntityCallback("receipt")
    def onReceipt(self, entity):
        self.toLower(entity.ack())

    def onTextMessage(self,messageProtocolEntity):
	body = messageProtocolEntity.getBody()
	match = re.match("^!del (.*)$", body)
	if match:
	    basename = os.path.basename(match.group(1))
	    filename = "files/%s" % basename
	    if os.path.isfile(filename):
                os.remove(filename)
                self.toLower(TextMessageProtocolEntity("Foto geloescht", to = messageProtocolEntity.getFrom()))
	    else:
	        self.toLower(TextMessageProtocolEntity("Foto nicht gefunden", to = messageProtocolEntity.getFrom()))

    def onMediaMessage(self, messageProtocolEntity):
        if messageProtocolEntity.getMediaType() == "image":
            self.tmpto = messageProtocolEntity.getFrom()
            data = messageProtocolEntity.getMediaContent()
            outPath = os.path.join("files", "%d.jpg" % nextSequenceNumber())
            f = open(outPath, 'wb')
            f.write(data)
            f.close()
            self.onSuccess(outPath)

    def onError(self):
	self.toLower(TextMessageProtocolEntity("Foto konnte nicht gespeichert werden", to = self.tmpto))

    def onSuccess(self, path):
        self.toLower(TextMessageProtocolEntity("Foto gespeichert (%s)" % (os.path.basename(path)), to = self.tmpto))

    def onProgress(self, progress):
	pass

