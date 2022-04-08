### Para instalar as dependencias utilize:
### python3.8 -m pip install -r requirements.txt 
### Linux or Windows Power Shell

import pandas as pd
from extensions import Afnd, File

file_path = "trabalho_lfa/input.txt"


def main():
    file = File(file_path)
    # file.show_file_lines()

    afnd = Afnd()
    # afnd.show_table()
    
    load_tokens(file, afnd)
    # afnd.append_row('e', 'A', 'B')

    # print(afnd.afnd_table['e'].isnull()["->S'"])

    afnd.fill_na_values()
    print('\n\n')
    afnd.show_table()

    


    
    
def load_tokens(file:File, afnd:Afnd):
    next_state = next(afnd.iterator)
    for line in file.get_line():
        line = line.strip()
        for i, terminal in enumerate(line):
            if i == 0:                # first terminal from token
                next_state = afnd.terminal_insert_head(terminal, current_state=next_state)
                # print(next_state)
            elif i == len(line) - 1:  # last terminal from token
                next_state = afnd.terminal_insert_tail(terminal, current_state=next_state)
            else:                     # middle terminal from token
                next_state = afnd.terminal_insert_middle(terminal, current_state=next_state)
                # print(next_state)

            afnd.show_table()
            print(f"iteration number {i}")



if __name__ == "__main__":
    main()