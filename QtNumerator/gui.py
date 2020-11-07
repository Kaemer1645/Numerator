# This Python file uses the following encoding: utf-8
import sys
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QApplication, QFileDialog, QPushButton, QLineEdit
from PySide2.QtCore import QFile, QIODevice
from numerator import Numerator

class Main:
    def __init__(self):
        ui_file_name = "dialog.ui"
        ui_file = QFile(ui_file_name)
        if not ui_file.open(QIODevice.ReadOnly):
            print("Cannot open {}: {}".format(ui_file_name, ui_file.errorString()))
            sys.exit(-1)
        loader = QUiLoader()
        self.window = loader.load(ui_file)
        ui_file.close()
        if not self.window:
            print(loader.errorString())
            sys.exit(-1)
        self.window.show()
        #directory:str, first_photo:str, prefix:str, first_number:str, step:str, file_type
        self.engine = Numerator(directory = self.selectDirectory(), first_photo = self.first_photo(),
                                prefix = self.new_file_name(),first_number = self.first_number(),
                                step = self.steps(), file_type = self.file_type)

    #def silnik(self):
        #pass

    def selectDirectory(self):

        #dialog = QFileDialog()
        directory = str(QFileDialog.getExistingDirectory())
        self.lineEdit.setText('{}'.format(directory))


    def first_photo(self):
        label = QLineEdit.le_first_photo.text()
        return label

    def first_number(self):
        number = QLineEdit.le_first_number.text()
        return number

    def new_file_name(self):
        prefix = QLineEdit.le_prefix.text()
        return prefix

    def steps(self):
        steps = QLineEdit.le_step.text()
        return steps
    def file_type(self):
        type = QLineEdit.le_file_type.text()
        return type

    def run(self):

        self.window.clicked.connect(self.selectDirectory)
        #self.window.clicked.connect(self.selectDirectory)



if __name__ == "__main__":
    app = QApplication([])
    inst = Main()
    inst.run()
    sys.exit(app.exec_())
