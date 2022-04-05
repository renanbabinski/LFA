import pandas as pd

class Afnd:
    def __init__(self) -> None:
        self.afnd_table = pd.DataFrame(['S'], columns=['Ø'])

    def show_table(self):
        print(self.afnd_table.to_markdown(index=False))

    
class File:
    def __init__(self, file_path) -> None:
        with open(file_path, 'r', encoding='utf-8') as file:
            self.file = file.readlines()

    def get_line(self):
        for line in self.file:
            yield line

    def show_file_lines(self):
        print(self.file)