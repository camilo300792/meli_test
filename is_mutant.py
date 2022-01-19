
def is_mutant(dna):
    print(dna)
    sequences = 0
    for k, line in enumerate(dna):
        for j, letter in enumerate(line):
            sequences = sequences + rigth_sequence(k, j, dna)
            sequences = sequences + bottom_sequence(k, j, dna)
            sequences = sequences + backslash_sequence(k, j, dna)
            sequences = sequences + slash_sequence(k, j, dna)        

    return sequences > 1

def rigth_sequence(index, seq, matrix):
    try:
        letter_1 = matrix[index][seq]
        letter_2 = matrix[index][seq + 1]
        letter_3 = matrix[index][seq + 2]
        letter_4 = matrix[index][seq + 3]
        if (letter_1 == letter_2 and letter_2 == letter_3 and letter_3 == letter_4):
            print('RIGTH',letter_1, letter_2,letter_3, letter_4)
            return 1
    except IndexError:
        pass
    return 0

def bottom_sequence(index, seq, matrix):
    try:
        letter_1 = matrix[index][seq]
        letter_2 = matrix[index + 1][seq]
        letter_3 = matrix[index + 2][seq]
        letter_4 = matrix[index + 3][seq]
        if (letter_1 == letter_2 and letter_2 == letter_3 and letter_3 == letter_4):
            print('BOTTOM',letter_1, letter_2,letter_3, letter_4)
            return 1
    except IndexError:
        pass
    return 0

def backslash_sequence(index, seq, matrix):
    try:
        letter_1 = matrix[index][seq]
        letter_2 = matrix[index + 1][seq + 1]
        letter_3 = matrix[index + 2][seq + 2]
        letter_4 = matrix[index + 3][seq + 3]
        if (letter_1 == letter_2 and letter_2 == letter_3 and letter_3 == letter_4):
            print('BACKSLASH',letter_1, letter_2,letter_3, letter_4)
            return 1
    except IndexError:
        pass
    return 0

def slash_sequence(index, seq, matrix):
    try:
        letter_1 = matrix[index][seq]
        letter_2 = matrix[index + 1][seq - 1]
        letter_3 = matrix[index + 2][seq - 2]
        letter_4 = matrix[index + 3][seq - 3]
        if (letter_1 == letter_2 and letter_2 == letter_3 and letter_3 == letter_4):
            print('SLASH',letter_1, letter_2,letter_3, letter_4)
            return 1
    except IndexError:
        pass
    return 0
