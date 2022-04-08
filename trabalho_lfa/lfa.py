### Para instalar as dependencias utilize:
### python3.8 -m pip install -r requirements.txt 
### Linux or Windows Power Shell

import pandas as pd
from extensions import Afnd, File, Afd

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
    print("------------ AFND ------------\n")
    afnd.show_table()

    # print(afnd.afnd_table.columns)

    afd = Afd(afnd)
    print()
    afd.show_table()
    print()

    determinization(afnd, afd)


    print('\n\n\n')
    print("------------ AFD ------------\n")
    afd.show_table()


    
def determinization(afnd:Afnd, afd:Afd):
    afd.copy_first_row(afnd)
    # for index in afd.afd_table.index:
    #     print(afd.afd_table.index[0])
    i = 0
    

    while True:
        try:
            current_index = afd.afd_table.index[i]
        except:
            print(f"Não foi possivel achar um inddex na posição {i}")
            break

        print(current_index)
        for value in afd.afd_table.loc[current_index]:
            # print(value)
            if value != '':
                if value in afd.afd_table.index:
                    print("Estado já está no indice!")
                else:
                    print("Estado ainda não está no indice!")
                    row = pd.DataFrame()
                    afd.merge_afnd_rows(afnd, value)
        i += 1

    
    
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