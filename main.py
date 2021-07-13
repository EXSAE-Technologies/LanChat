from PyQt5.QtWidgets import (
    QWidget,
    QApplication,
    QVBoxLayout,
    QSplitter,
    QListWidget,
    QListWidgetItem,
    QTextEdit,
    QLineEdit
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
import sys

class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("Lan")
        self.setWindowIcon(QIcon('icon.png'))

        layout = QVBoxLayout()
        self.setLayout(layout)

        splitter = QSplitter()
        splitter.setOrientation(Qt.Horizontal)
        layout.addWidget(splitter)

        list = QListWidget()
        splitter.addWidget(list)

        for i in range(20):
            a = QListWidgetItem()
            a.setText(str(i))
            list.addItem(a)
        
        splitter2 = QSplitter()
        splitter2.setOrientation(Qt.Vertical)
        splitter.addWidget(splitter2)

        textView = QTextEdit()
        textView.setHtml("<h1>Hello World</h1>")
        textView.setReadOnly(True)
        splitter2.addWidget(textView)

        lineEdit = QLineEdit()
        splitter2.addWidget(lineEdit)

app = QApplication(sys.argv)
screen = Window()
screen.show()

sys.exit(app.exec_())