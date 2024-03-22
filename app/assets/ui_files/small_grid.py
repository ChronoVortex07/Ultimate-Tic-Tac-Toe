# -*- coding: utf-8 -*-
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QSizePolicy, QWidget)

from cell import Ui_Cell

class Ui_Small_Grid(QWidget):
    # setupUi
    def setupUi(self):
        if not self.objectName():
            self.setObjectName(u"Small_Grid")
        self.resize(895, 575)
        self.setStyleSheet(u"QWidget{\n"
"	border:3px solid rgba(255, 255, 255, 0);\n"
"}")
        self.gridLayout = QGridLayout(self)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.retranslateUi()

        QMetaObject.connectSlotsByName(self)
    
    # retranslateUi
    def retranslateUi(self):
        self.setWindowTitle(QCoreApplication.translate("Small_Grid", u"Small_Grid", None))
        
    def setup_cells(self, cells):
        for i in range(3):
            for j in range(3):
                ui = Ui_Cell()
                ui.setupUi()
                ui.setStyleSheet("\n".join([
                    'border-top-color: rgb(255, 255, 255);' if i != 0 else '',
                    'border-bottom-color: rgb(255, 255, 255);' if i != 2 else '',
                    'border-left-color: rgb(255, 255, 255);' if j != 0 else '',
                    'border-right-color: rgb(255, 255, 255);' if j != 2 else '',                                     
                ]))
                ui.set_state(cells[i][j])
                self.gridLayout.addWidget(ui, i, j, 1, 1)
                
if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    ui = Ui_Small_Grid()
    ui.setupUi()
    cells = [["X", "O", ""], ["O", "X", ""], ["", "", "X"]]
    ui.setup_cells(cells)
    ui.show()
    sys.exit(app.exec())
                
    