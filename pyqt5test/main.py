#!/usr/bin/python3

import sys
from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QGuiApplication
from PyQt5.QtQml import QQmlComponent, QQmlApplicationEngine


# Create the application instance.
app = QGuiApplication(sys.argv)

# Create a QML engine.
engine = QQmlApplicationEngine()

# Create a component factory and load the QML script.
component = QQmlComponent(engine)
component.loadUrl(QUrl('main.qml'))

# Create the objects from the QML
window = component.create()
window.show()

sys.exit(app.exec_())



# if __name__ == "__main__":
#     # create the application instance
#     app = QGuiApplication(sys.argv)
#
#     # Creating a QML engine
#     engine = QQmlEngine()
#     engine.load(QUrl.fromLocalFile("main.qml"))
#
#     window = engine.rootObjects()[0]
#     window.show()
#
#     sys.exit(app.exec_())