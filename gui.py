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


    #def silnik(self):
        #test = (self.selectDirectory(), self.first_file(),self.new_file_name(),self.first_number(), self.steps(),self.file_type())
        #return print(test)

    def engine(self):
        #print(self.directory())
        self.numerator = Numerator(directory=self.directory(), first_file=self.first_file(),
                                   prefix=self.new_file_name(), first_number=self.first_number(),
                                   step=self.steps(), file_type=self.file_type())
        self.numerator.run()
        #print(self.directory())
    def selectDirectory(self):

        #dialog = QFileDialog()
        directory = str(QFileDialog.getExistingDirectory())
        self.window.le_dir.setText('{}'.format(directory))
        #return print(directory)
    # def print_dir(self):
    #     pri = self.window.le_dir.text()
    #     return print(pri)

    def directory(self):
        dir_text = self.window.le_dir.text()
        return dir_text

    def first_file(self):
        label = self.window.le_first_file.text()
        return label

    def first_number(self):
        number = self.window.le_file_number.text()
        return number

    def new_file_name(self):
        prefix = self.window.le_prefix.text()
        return prefix

    def steps(self):
        steps = self.window.le_step.text()
        return steps
    def file_type(self):
        type = self.window.le_file_type.text()
        return type

    def run(self):

        self.window.pb_dir.clicked.connect(self.selectDirectory)
        #self.window.pb_dir.clicked.connect(self.silnik)
        self.window.pb_run.clicked.connect(self.engine)
        #self.window.pb_run.clicked.connect(self.print_dir)



if __name__ == "__main__":
    app = QApplication([])
    inst = Main()
    inst.run()
    sys.exit(app.exec_())
