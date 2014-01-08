import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtWebKit import *

app = QApplication(sys.argv)

web = QWebView()
web.load(QUrl("/home/radek/pszt/my/bar1.svg"))
web.show()

sys.exit(app.exec_())
