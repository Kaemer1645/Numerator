# This Python file uses the following encoding: utf-8
import sys, shutil
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QApplication, QFileDialog, QPushButton, QLineEdit
from PySide2 import QtXml
from PySide2.QtCore import QFile, QIODevice
from PySide2 import QtXml
from numerator import Numerator#, Numerator_run
import webbrowser

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
        check = self.numerator.run() #to musimy zapisac w miejscu, bo jak zrobimy z tego for'a nizej, to zrobi nam petle podwojnie
        for file in check:
            print('Change from "%s" to "%s"'% (file[0],file[1]))
        '''for single_print in self.numerator.run():
            print(single_print)'''
            
    def execution(self):
        self.exec = Numerator(directory=self.directory(), first_file=self.first_file(),
                                   prefix=self.new_file_name(), first_number=self.first_number(),
                                   step=self.steps(), file_type=self.file_type())
        change = self.exec.run()

        for exec_file in change:
            print('Change from "%s" to "%s"'% (exec_file[0],exec_file[1]))
            shutil.move(exec_file[0],exec_file[1])
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
        return int(number)

    def new_file_name(self):
        prefix = self.window.le_prefix.text()
        return prefix

    def steps(self):
        steps = self.window.le_step.text()
        return int(steps)

    def file_type(self):
        type = self.window.le_file_type.text()
        return type

    def github(self):
        open = webbrowser.open('https://github.com/Kaemer1645/Numerator')
        return open

    def run(self):
        self.window.pb_dir.clicked.connect(self.selectDirectory)
        #self.window.pb_dir.clicked.connect(self.silnik)
        self.window.pb_test.clicked.connect(self.engine)
        #self.window.pb_run.clicked.connect(self.print_dir)
        self.window.pb_run.clicked.connect(self.execution)
        self.window.pb_github.clicked.connect(self.github)


if __name__ == "__main__":
    app = QApplication([])
    inst = Main()
    inst.run()
    sys.exit(app.exec_())
