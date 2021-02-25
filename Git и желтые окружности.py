import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QButtonGroup
from PyQt5.QtWidgets import QMainWindow, QLabel, QLineEdit
from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from random import randint
import glob


class mw(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('Git и желтые окружности.ui', self)
        self.initUI()

    def initUI(self):
        self.do_paint = False
        self.btn.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_flag(qp)
            qp.end()

    def paint(self):
        self.do_paint = True
        self.repaint()

    def draw_flag(self, qp):
        qp.setBrush(QColor(255, 255, 0))
        for i in range(randint(2, 50)):
            r = randint(10, 100)
            x = randint(0, 800)
            y = randint(0, 800)
            qp.drawEllipse(x, y, r, r)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = mw()
    ex.show()
    sys.exit(app.exec())
