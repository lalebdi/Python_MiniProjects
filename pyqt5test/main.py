#!/usr/bin/python3

import os, sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtQuick import *
from PyQt5.Qt import *

if __name__== "__main__":
    app = QGuiApplication(sys.argv)

    # Creating an engine
    engine = QQmlEngine()