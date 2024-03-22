from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QPushButton, QSizePolicy,
    QWidget)

class Ui_Cell(QWidget):
    # setupUi
    def setupUi(self):
        if not self.objectName():
            self.setObjectName(u"Cell")
        self.resize(0, 0)
        self.setStyleSheet(u"QWidget{\n"
"	border:3px solid rgba(255, 255, 255, 0);\n"
"}")
        
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        
        
        self.setSizePolicy(sizePolicy)
        
        self.gridLayout = QGridLayout(self)
        self.gridLayout.setObjectName(u"gridLayout")
        self.pushButton = QPushButton(self)
        self.pushButton.setObjectName(u"pushButton")
        
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        
        self.pushButton.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(150)
        font.setBold(True)
        self.pushButton.setFont(font)

        self.gridLayout.addWidget(self.pushButton, 0, 0, 1, 1)

        self.retranslateUi()

        QMetaObject.connectSlotsByName(self)

    # retranslateUi
    def retranslateUi(self):
        self.setWindowTitle(QCoreApplication.translate("Cell", u"Form", None))
        self.pushButton.setText(QCoreApplication.translate("Cell", u"", None))
        
    def set_state(self, state):
        if state == "X":
            self.pushButton.setText("×")
            self.pushButton.setStyleSheet("color: rgb(35, 138, 239)")
        elif state == "O":
            self.pushButton.setText("O")
            self.pushButton.setStyleSheet("color: rgb(231, 69, 55)")
        else:
            self.pushButton.setText("")
    

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    ui = Ui_Cell()
    ui.setupUi()
    ui.set_state("O")
    ui.show()
    sys.exit(app.exec())
