### To install dependencies:
### python3.8 -m pip install -r requirements.txt 
### Linux or Windows Power Shell

import pandas as pd
from extensions import Afnd, File, Afd

file_path = "trabalho_lfa/input.txt"

def main():
    file = File(file_path)
    afnd = Afnd()
    
    load_tokens(file, afnd) # Call function to load tokens into AFND

    load_gr(file, afnd) # Call function to load GR

    afnd.fill_na_values() # Convert "nan" values to ''
   
    print("------------ AFND ------------")
    afnd.show_table()

    print()

    print("------------ AFD ------------")
    afd = Afd(afnd)

    determinization(afnd, afd)
   
    afd.show_table()



def load_gr(file:File, afnd:Afnd):
    mapping = dict()
    for line in file.get_line():
        if line[0] != '<':
            continue
        line = line.strip()
        head = ''
        productions = []
        head = line.split('::=')[0].strip()
        productions = line.split('::=')[1]
        head = head.replace("<", '')
        head = head.replace(">", '')
        productions = productions.split('|')
        productions = [x.strip() for x in productions]  #Clean blank spaces

        if head == 'S':    # First GR
            is_final = False
            for prod in productions:
                if '<' in prod:
                    terminal = prod.split('<')[0]
                    production_state = prod.split('<')[1].replace('>', '')
                
                else:
                    afnd.next_state = afnd.terminal_insert_tail(terminal=prod, current_state=afnd.next_state, is_final=True)
                if production_state not in mapping.keys():
                    new_map = {production_state: afnd.next_state}
                    mapping.update(new_map)
                    afnd.next_state = afnd.terminal_insert_middle(terminal='empty', current_state=mapping[production_state], is_final=is_final)
                afnd.next_state = afnd.terminal_insert_head(terminal=terminal, current_state=mapping[production_state])
        else:
            if 'ε' in productions:
                    is_final = True
            for prod in productions:
                if '<' in prod:
                    terminal = prod.split('<')[0]
                    production_state = prod.split('<')[1].replace('>', '')
                else:
                    pass

                if production_state not in mapping.keys():
                    new_map = {production_state: afnd.next_state}
                    mapping.update(new_map)
                    afnd.next_state = afnd.terminal_insert_middle(terminal=None, current_state=mapping[production_state])
                afnd.next_state = afnd.terminal_update_prod(terminal=terminal, head_state=mapping[head], dest_state=mapping[production_state])
                is_final = False



def determinization(afnd:Afnd, afd:Afd):
    afd.copy_first_row(afnd)
    i = 0
    
    while True:
        try:
            current_index = afd.afd_table.index[i]
        except:
            break
        for value in afd.afd_table.loc[current_index]:
            if value != '':
                if value in afd.afd_table.index:
                    pass
                else:
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


if __name__ == "__main__":
    main()