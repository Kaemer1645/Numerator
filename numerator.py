# -*- coding: utf-8 -*-
import os, sys
from pathlib import Path

class Numerator():
    def __init__(self, directory:str, first_file:str, prefix:str, first_number:int, step:str, file_type):

        self.directory = directory
        self.first_file = first_file
        self.prefix = prefix
        self.file_type = file_type
        self.first_number = first_number
        self.step = step
        self.end = None


    def run(self):

        #reszta kodu jest pisana w gui.py
        
        #print('dir',self.directory)
        os.chdir(Path(self.directory))
        #print('dada',os.getcwd())
        #self.first_number =
        iterator = 0
        print_files = []
        for self.file in os.listdir(self.directory):
            #print(self.file)
            #print(self.directory)
            if iterator == 0:
                self.changed = self.prefix + str(self.first_number) + self.file_type
                #print('lol+1',str(self.first_number))
                #print('Change from "%s" to "%s"'% (self.file,self.changed))
                #shutil.move(file,changed)
                print_files.append((str(self.file),str(self.changed)))
                iterator+=1
            elif iterator >= 1:
                self.first_number += self.step
                self.changed = self.prefix + str(self.first_number) + self.file_type
                #print('2Change from "%s" to "%s"'% (self.file,self.changed))
                print_files.append((str(self.file),str(self.changed)))
        return print_files
                #shutil.move(file,changed)
        #self.end = input('Write "end" in the cmnd window to exit')
        #if self.end == 'end':
            #sys.exit()

    #zrobic returna z file i changed i dodac do nowej funkcji move it
    #def run(self):

'''class Numerator_run(Numerator):
    def run(self):
        Numerator.check(self)
        for self.file in os.listdir(self.directory):
            print('Numerator run','Change2 %s to %s' %(self.file,self.changed))'''
    
        
