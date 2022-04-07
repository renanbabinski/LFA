
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



if __name__ == "__main__":
    # alpha = gen_alpha()
    iterator = gen_alpha()
    for i in range(100):
        print(next(iterator))
        