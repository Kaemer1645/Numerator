# -*- coding: utf-8 -*-
import os, shutil
from pathlib import Path

class Numerator():
    def __init__(self, directory:str, first_file:str, prefix:str, first_number:str, step:str, file_type):

        self.directory = directory
        self.first_photo = first_photo
        self.prefix = prefix
        self.file_type = file_type
        self.first_number = first_number
        self.step = step


    def run(self):
        os.chdir(Path(self.directory))
        self.first_number = 1
        for file in os.listdir(Path(self.directory)):
            self.first_number += 1
            if files >= self.first_photo:
                changed = self.prefix + str(self.first_number) + self.file_type
                print('Change from "%s" to "%s"'% (file,changed))
                #shutil.move(zdjecia,strona)
