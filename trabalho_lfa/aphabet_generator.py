
from time import sleep


def gen_alpha() -> list():
    alpha = ['@']
    while True:
        while alpha[-1] != 'Z':             # While alphabet has not reached the end
            alpha[-1] = increment(alpha[-1])
            alpha_str = ''.join([str(letter) for letter in alpha])
            sleep(0.01)
            yield alpha_str
        for i in range(len(alpha)-1, -1, -1):
            if i != 0 and alpha[i-1] != 'Z' and alpha[i] == 'Z' and i == len(alpha)-1:
                alpha[i] = '@'
                alpha[i-1] = increment(alpha[i-1])
                continue
            if i != 0 and alpha[i] == 'Z' and i == len(alpha)-1:
                alpha[i] = '@'
                continue
            if i != 0 and alpha[i] == 'Z':
                alpha[i] = 'A'
                alpha[i-1] = increment(alpha[i-1])
                continue
            if i == 0 and alpha[i] == 'Z' and len(alpha) == 1:
                alpha[i] = 'A'
                if alpha[-1] == '@':
                    alpha[-1] = 'A'
                    alpha.append('@')  ## If we reached the head of list
                else:
                    alpha.append('@')  ## If we reached the head of list
            elif i == 0 and alpha[i] == '[':
                alpha[i] = 'A'
                if alpha[-1] == '@':
                    alpha[-1] = 'A'
                    alpha.append('@')  ## If we reached the head of list
                else:
                    alpha.append('@')  ## If we reached the head of list




            # if i == 0 and alpha[i] == 'Z' and len(alpha) == 1:
           
            #     continue
            # if i < len(alpha)-1 and alpha[i+1] == 'Z':
            #     alpha[i] = increment(alpha[i])
            #     alpha[i+1] = '@'
                



            # print(i)
            # if i == 0:
            
            
            
            




def increment(letter:str()) -> str():
    letter = chr(ord(letter) + 1)
    return letter



if __name__ == "__main__":
    # alpha = gen_alpha()
    for i in gen_alpha():
        print(i)
        