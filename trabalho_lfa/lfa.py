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

    load_gr(file, afnd)

    # print(afnd.afnd_table['e'].isnull()["->S'"])

    afnd.fill_na_values()
    print('\n\n')
    print("------------ AFND ------------\n")
    afnd.show_table()

    # print(afnd.afnd_table.columns)

    # afd = Afd(afnd)
    # print()
    # afd.show_table()
    # print()

    # determinization(afnd, afd)


    # print('\n\n\n')
    # print("------------ AFD ------------\n")
    # afd.show_table()





def load_gr(file:File, afnd:Afnd):
    mapping = dict()
    for line in file.get_line():
        if line[0] != '<':
            continue
        line = line.strip()
        # print(line)
        head = ''
        productions = []
        head = line.split('::=')[0].strip()
        productions = line.split('::=')[1]
        head = head.replace("<", '')
        head = head.replace(">", '')
        productions = productions.split('|')
        productions = [x.strip() for x in productions]  #Clean blank spaces
        print(head, productions)

        if head == 'S':    # First GR
            for prod in productions:
                # print(f"Terminal: {prod.split('<')[0]}" )
                # print(f"Produção: {prod.split('<')[1].replace('>', '')}" )
                terminal = prod.split('<')[0]
                production_state = prod.split('<')[1].replace('>', '')
                if production_state not in mapping.keys():
                    # print(f"A produção {production_state} não está no mapeamento!")
                    new_map = {production_state: afnd.next_state}
                    mapping.update(new_map)
                afnd.next_state = afnd.terminal_insert_head(terminal=terminal, current_state=mapping[production_state])
                print(mapping)
        else:
            



def determinization(afnd:Afnd, afd:Afd):
    afd.copy_first_row(afnd)
    i = 0
    
    while True:
        try:
            current_index = afd.afd_table.index[i]
        except:
            print(f"Não foi possivel achar um index na posição {i}")
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
    for line in file.get_line():
        if line == '\n':
            break
        line = line.strip()
        for i, terminal in enumerate(line):
            if i == 0:                # first terminal from token
                afnd.next_state = afnd.terminal_insert_head(terminal, current_state=afnd.next_state)
            elif i == len(line) - 1:  # last terminal from token
                afnd.next_state = afnd.terminal_insert_tail(terminal, current_state=afnd.next_state)
            else:                     # middle terminal from token
                afnd.next_state = afnd.terminal_insert_middle(terminal, current_state=afnd.next_state)
                # print(next_state)

            afnd.show_table()
            print(f"iteration number {i}")



if __name__ == "__main__":
    main()