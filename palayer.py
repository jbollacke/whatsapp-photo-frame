from yowsup.layers.protocol_media.mediadownloader import MediaDownloader
from yowsup.layers.interface import YowInterfaceLayer, ProtocolEntityCallback
from yowsup.layers.protocol_messages.protocolentities import TextMessageProtocolEntity
import shutil, os
import re

class PictureArchiverLayer(YowInterfaceLayer):

    @ProtocolEntityCallback("message")
    def onMessage(self, messageProtocolEntity):
        if messageProtocolEntity.getType() == 'text':
            self.onTextMessage(messageProtocolEntity)
        elif messageProtocolEntity.getType() == 'media':
            self.onMediaMessage(messageProtocolEntity)

        self.toUpper(messageProtocolEntity)
        self.toLower(messageProtocolEntity.ack())
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
            self.downloadMedia(messageProtocolEntity.getMediaUrl())

    def downloadMedia(self, url):
        downloader = MediaDownloader(self.onSuccess, self.onError, self.onProgress)
        downloader.download(url)

    def onError(self):
	self.toLower(TextMessageProtocolEntity("Foto konnte nicht gespeichert werden", to = self.tmpto))

    def onSuccess(self, path):
        outPath = "files/%s.jpg" % os.path.basename(path)
        shutil.copyfile(path, outPath)
        self.toLower(TextMessageProtocolEntity("Foto gespeichert (%s)" % (os.path.basename(outPath)), to = self.tmpto))

    def onProgress(self, progress):
	pass

