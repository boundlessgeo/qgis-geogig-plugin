# -*- coding: utf-8 -*-
#
# (c) 2016 Boundless, http://boundlessgeo.com
# This code is licensed under the GPL 2.0 license.
#
from PyQt4 import QtGui

class CommitDialog(QtGui.QDialog):

    def __init__(self, repo, parent = None):
        super(CommitDialog, self).__init__(parent)
        self.repo = repo
        self._closing = False
        self.initGui()

    def initGui(self):
        self.resize(600, 250)
        self.setWindowTitle('GeoGig')

        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setMargin(5)

        self.msgLabel = QtGui.QLabel("Message to describe this update")
        self.verticalLayout.addWidget(self.msgLabel)

        self.text = QtGui.QPlainTextEdit()
        self.verticalLayout.addWidget(self.text)

        self.buttonBox = QtGui.QDialogButtonBox(QtGui.QDialogButtonBox.Ok)
        self.verticalLayout.addWidget(self.buttonBox)
        self.buttonBox.button(QtGui.QDialogButtonBox.Ok).setEnabled(False)
        self.setLayout(self.verticalLayout)

        self.buttonBox.accepted.connect(self.okPressed)

        self.text.textChanged.connect(self.textHasChanged)
        if self.repo.ismerging():
            self.text.setPlainText(self.repo.mergemessage())

    def textHasChanged(self):
        self.buttonBox.button(QtGui.QDialogButtonBox.Ok).setEnabled(self.text.toPlainText() != "")

    def getMessage(self):
        return self.text.toPlainText()

    def okPressed(self):
        self.closeDialog()

    def closeDialog(self):
        self._closing = True
        self.close()

    def closeEvent(self, evnt):
        if self._closing:
            super(CommitDialog, self).closeEvent(evnt)
        else:
            evnt.ignore()
