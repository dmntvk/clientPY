from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtWidgets
from editorbd import editor
import sys
import os


class edi(QWidget, editor):
    def __init__(self):
        super(edi, self).__init__()
        self.setupUi(self)