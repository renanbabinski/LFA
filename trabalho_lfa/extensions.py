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


def increment(letter:str) -> str:
    letter = chr(ord(letter) + 1)
    return letter

def transform_list(string:str):
    # split = string.split(',')
    return '[' + string + ']'


class Afnd:
    def __init__(self) -> None:
        self.afnd_table = pd.DataFrame(["->S'"], columns=['Ø'])
        self.afnd_table.set_index('Ø', drop=True, inplace=True)
        self.iterator = gen_alpha()

    def show_table(self):
        print(self.afnd_table.to_markdown(index=True))

    def append_row(self, terminal_column=None, current_state=None, next_state=None):
        if terminal_column:
            data = {
                'Ø': [current_state],
                terminal_column: [next_state]
            }
        else:
            data = {
                'Ø': [f"{current_state}*"]
            }
        row = pd.DataFrame(data)
        row.set_index('Ø', drop=True, inplace=True)
        print("APPEND!")
        print(row.to_markdown())
        self.afnd_table = pd.concat([self.afnd_table, row])

    def terminal_insert_head(self, terminal:str, current_state:str) ->str:
        if terminal not in self.afnd_table.columns:
            print(f"Terminal {terminal} not in columns!")
            self.afnd_table.loc["->S'", [terminal]] = current_state
            return current_state
        else:
            print(f"Terminal {terminal} is in columns!")
            if self.afnd_table[terminal].isnull()["->S'"]:
                self.afnd_table.loc["->S'", [terminal]] = current_state
            else:
                self.afnd_table.loc["->S'", [terminal]] += ',' + current_state
            return current_state

    def terminal_insert_middle(self, terminal:str, current_state:str):
        print(f"Terminal {terminal} not in columns!")
        next_state = next(self.iterator)
        self.append_row(terminal, current_state, next_state)
        return next_state
        

    def terminal_insert_tail(self, terminal:str, current_state:str):
            next_state = next(self.iterator)
            self.append_row(terminal, current_state, next_state)
            current_state = next_state
            next_state = next(self.iterator)
            self.append_row(current_state=current_state)
            return next_state

    def fill_na_values(self):
        self.afnd_table =  self.afnd_table.fillna('')

class Afd:
    def __init__(self, afnd:Afnd) -> None:
        columns = ['Ø']
        for column in afnd.afnd_table.columns:
            columns.append(column)
        # print(columns)
        self.afd_table = pd.DataFrame([], columns=columns)
        self.afd_table.set_index('Ø', drop=True, inplace=True)
        # self.iterator = gen_alpha()

    def show_table(self):
        print(self.afd_table.to_markdown(index=True))

    def copy_first_row(self, afnd:Afnd):
        columns = ['Ø']
        values = ["->S'"]
        for column, value in zip(afnd.afnd_table.columns, afnd.afnd_table.loc["->S'"]):
            columns.append(column)
            if len(value) > 1:
                values.append(transform_list(value))
            else:
                values.append(value)
            
        row = pd.DataFrame([values], columns=columns)
        row.set_index('Ø', drop=True, inplace=True)
        self.afd_table = pd.concat([self.afd_table, row])

    def merge_afnd_rows(self, afnd:Afnd, states):
        print('\n MERGE DEBUG \n')
        columns = ['Ø']
        master_values = [states]
        is_final = False
        values = [None] * len(self.afd_table.columns)
        for state in states:
            if state not in [',', '[', ']']:
                if state not in afnd.afnd_table.index:
                    is_final = True
                    state += '*'
               
                for i, value in enumerate(afnd.afnd_table.loc[state]):
                    if not values[i]:
                        values[i] = value
                    else:
                        values[i] += ',' + value
                        values[i] = transform_list(values[i])

        if is_final:
            master_values[0] += '*'

        master_values.extend(values)
        columns.extend(self.afd_table.columns)

        row = pd.DataFrame([master_values], columns=columns)
        row.set_index('Ø', drop=True, inplace=True)
        self.afd_table = pd.concat([self.afd_table, row])
                    


class File:
    def __init__(self, file_path) -> None:
        with open(file_path, 'r', encoding='utf-8') as file:
            self.file = file.readlines()

    def get_line(self):
        for line in self.file:
            yield line

    def show_file_lines(self):
        print(self.file)