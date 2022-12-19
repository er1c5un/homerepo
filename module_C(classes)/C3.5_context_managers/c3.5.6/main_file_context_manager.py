class FileWorker:
    def __init__(self, path_to_file, mode):
        self.path_to_file = path_to_file
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.path_to_file, self.mode)
        print(f'Opened file {self.path_to_file} with mode {self.mode}')
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()
        print(f'Closed file {self.path_to_file}')


file = 'C:\\Users\\radjuk\\PycharmProjects\\SkillFactory\\module_C(classes)\\C3.5_context_managers\\c3.5.6\\test.txt'
with FileWorker(file, 'w') as f:
    f.write('Test line 1')
