__author__ = 'Benni'

import sys

from PyQt4 import QtGui, QtCore

import Aspect
from Window import Ui_dialogAspector as Dlg


class Aspector(QtGui.QDialog, Dlg):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.setupUi(self)

aspectGraph = Aspect.makeGraph()
app = QtGui.QApplication(sys.argv)
dialog = Aspector()
tintedPixmaps = {}

def tintPixmap(pixmap, color):
    painter = QtGui.QPainter(pixmap)
    painter.setCompositionMode(painter.CompositionMode_DestinationAtop)
    painter.fillRect(pixmap.rect(), color)
    painter.end()
    return pixmap

for aspect in Aspect.aspects:
    color = QtGui.QColor(Aspect.aspects[aspect]["color"]) #such code, very facepalm
    px = tintPixmap(QtGui.QPixmap("aspects/"+aspect+".png"), color)
    tintedPixmaps[aspect] = px

    itm = QtGui.QListWidgetItem(aspect)
    itm.setIcon(QtGui.QIcon(px))
    dialog.listWidgetFrom.addItem(itm)

    itm2 = QtGui.QListWidgetItem(aspect)
    itm2.setIcon(QtGui.QIcon(px))
    dialog.listWidgetTo.addItem(itm2)



def showAspectPath(path):
    frame = QtGui.QFrame(dialog.scrollAreaWidgetContents)
    sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(frame.sizePolicy().hasHeightForWidth())

    frame.setSizePolicy(sizePolicy)
    #frame.setFrameShape(QtGui.QFrame.HLine)
    #frame.setObjectName("frame")

    horizontalLayout = QtGui.QHBoxLayout(frame)
    horizontalLayout.setContentsMargins(0, 6, 0, 6)
    #horizontalLayout.setObjectName("horizontalLayout")

    #TODO: create a model for the lists, instead of adding labels manually
    for aspect in path:
        pictureLabel = QtGui.QLabel(frame)
        pictureLabel.setToolTip(aspect)
        pictureLabel.setText(aspect)
        pictureLabel.setPixmap(tintedPixmaps[aspect])
        #pictureLabel.setObjectName("label_5")
        horizontalLayout.addWidget(pictureLabel)

    dialog.verticalLayout.addWidget(frame)

def clearPaths():
    for i in range(dialog.verticalLayout.count()):
        dialog.verticalLayout.itemAt(i).widget().close()

@QtCore.pyqtSlot()
def on_click():
    clearPaths()

    startAspect = dialog.listWidgetFrom.currentItem().text()
    endAspect = dialog.listWidgetTo.currentItem().text()
    length = dialog.spinBox.value()
    paths = Aspect.findPaths(aspectGraph, startAspect, endAspect, length)

    for path in paths:
        showAspectPath(path)


dialog.pushButtonGo.clicked.connect(on_click)

dialog.show()
sys.exit(app.exec_())