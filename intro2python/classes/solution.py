class FileReader:
    def __init__(self, file_path):
        self.file_path = file_path

    def read(self):
        try:
            with open(self.file_path) as file:
                content = file.read()
                return content
        except IOError:
            return ""

#reader = FileReader("example")
#print(reader.read())