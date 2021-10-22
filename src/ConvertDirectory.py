from os import listdir, chdir
from os.path import isfile, isdir, join
from src.ParseText import ParseText

class ConvertDirectory:

    parse_text = ParseText()

    def read_file(self,path):
        try:
            with open(path, encoding="utf8") as file:
                text = file.read()
        except:
            print("read_file",path)
            raise
        return text

    def get_files(self, path):
        return [f for f in listdir(path) if isfile(join(path, f))]

    def get_directories(self, path):
        return [d for d in listdir(path) if isdir(join(path, d))]

    def convert_files(self, path):
        files = self.get_files(path)
        chdir(path)
        for file in files:
            if file[-3:] == ".py":
                text = self.read_file(file)
                #print(self.parse_text.convert(text))
                self.write_to_file(file, self.parse_text.convert(text))
        directories = self.get_directories(path)
        for directory in directories:
            self.convert_files(join(path,directory))

    def write_to_file(self, file, text):
        try:
            with open(file, "w",  encoding="utf8") as open_file:
                open_file.write(text)
        except:
            print("write_to_file",file)
            raise