import tempfile
import os

class File:
    def __init__(self, file_path):
        self.abs_path = file_path
        self.cur_line = 0
        try:
            with open(file_path, 'r') as f:
                self.lines = f.readlines()

        except FileNotFoundError:
            self.lines = []
        self.lines_n = len(self.lines)

    def write(self, text):
        with open(self.abs_path, 'w') as f:
            f.write(text)

    def __add__(self, file_obj):
        dir = tempfile.gettempdir()
        with open(self.abs_path, 'r') as f1:
            content1 = f1.read()

        with open(file_obj.abs_path, 'r') as f2:
            content2 = f2.read()

        newfile_path = os.path.join(dir, "new_file.txt")
        with open(newfile_path, 'w') as f3:
            f3.write(content1)
            f3.write(content2)

        return File(newfile_path)

    def __iter__(self):
        return self

    def __next__(self):
        if self.cur_line < self.lines_n:
            line = self.lines[self.cur_line]
            self.cur_line += 1
            return line
        else:
            raise StopIteration


    def __str__(self):
        return self.abs_path


# f1 = File('/tmp/file.txt')
# f1.write('this is some text\nsecond line\nthird line')
# f2 = File('/tmp/file2.txt')
#
# print(f1.lines)
# new_obj = f1 + f2
#
# print(type(new_obj))
#
# for l in f1:
#     print('line = ', l)
#
# print(new_obj.lines)