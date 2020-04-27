import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtGui import *
import qimage2ndarray
import numpy as np
import cv2

image = cv2.imread('Lenna.png')

basic_ui = uic.loadUiType("homework_ui.ui")[0]

class WindowClass(QMainWindow, basic_ui):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.image = None

        self.flip.clicked.connect(lambda: self.flip_image(self.image))
        self.open.clicked.connect(lambda : self.imageshow())

    def imageshow(self):
        fileName, _ = QFileDialog.getOpenFileName(self, "Open File", ".")

        if fileName:
            self.image = QImage(fileName)

            if self.image.isNull():
                QMessageBox.information(self, "Image Viewer", "Cannot load %s." % fileName)
                return

            qPixmapYar = QPixmap.fromImage(self.image)
            qPixmapYar = qPixmapYar.scaled(256,256)
            self.label.setPixmap(qPixmapYar)
            self.show()

    def flip_image(self,image):
        if (image == None):
            print('please load image first!!')
            return

        image_array = qimage2ndarray.rgb_view(image)
        image_array = np.flip(image_array, 0)
        self.image = qimage2ndarray.array2qimage(image_array, normalize = False)

        qPixmapYar = QPixmap.fromImage(self.image)
        qPixmapYar = qPixmapYar.scaled(256, 256)
        self.label.setPixmap(qPixmapYar)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)

    myWindow = WindowClass()
    myWindow.show()
    app.exec_()