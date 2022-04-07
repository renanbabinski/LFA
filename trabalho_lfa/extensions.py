import pandas as pd
import string

def gen_alpha():
    alpha = ['EMPTY']
    carry = 0
    while True:
        for letter in string.ascii_uppercase:            # While alphabet has not reached the end
            alpha[-1] = letter
            alpha_str = ''.join([str(letter) for letter in alpha])
            yield alpha_str
        carry = 1
        for i in range(len(alpha)-1, -1, -1):
            if alpha[i] == 'Z' and carry == 1:
                alpha[i] = 'A'
            elif carry == 1:
                alpha[i] = increment(alpha[i])
                carry = 0
            else:
                continue

        if carry == 1:
            alpha.append('EMPTY')


def increment(letter:str()) -> str():
    letter = chr(ord(letter) + 1)
    return letter



class Afnd:
    def __init__(self) -> None:
        self.afnd_table = pd.DataFrame(['S'], columns=['Ø'])
        self.iterator = gen_alpha()

    def show_table(self):
        print(self.afnd_table.to_markdown(index=False))

    def append_row(self, data=[]):
        row = pd.DataFrame([f'{next(self.iterator)}'], columns=['Ø'])
        self.afnd_table = pd.concat([self.afnd_table, row], ignore_index=True)

    
class File:
    def __init__(self, file_path) -> None:
        with open(file_path, 'r', encoding='utf-8') as file:
            self.file = file.readlines()

    def get_line(self):
        for line in self.file:
            yield line

    def show_file_lines(self):
        print(self.file)