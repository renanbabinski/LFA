### Para instalar as dependencias utilize:
### python3.8 -m pip install -r requirements.txt 
### Linux or Windows Power Shell

import pandas as pd
from extensions import Afnd, File
import os

file_path = "trabalho_lfa/input.txt"


def main():
    file = File(file_path)
    # file.show_file_lines()
    
    load_tokens(file)


    afnd = Afnd()
    afnd.show_table()


def load_tokens(file:File):
    for line in file.get_line():
        print(line.strip())


if __name__ == "__main__":
    main()