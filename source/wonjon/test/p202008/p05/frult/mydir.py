import os
from .file import File

class Mydir:
    def __init__(self, dir):
        self.dir = dir
        self.files = []
        self.read_files()

    def read_files(self):
        with os.scandir(self.dir) as entries:
            for entry in entries:
                self.files.append( File(entry.name) )


