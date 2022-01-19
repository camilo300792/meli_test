import json
from is_mutant import is_mutant


def main():

    data = json.loads('{"dna":["ATGCGA","CAGTGC","TTATGT","AGAAGG","CCCCTA","TCACTG"]}')

    print(is_mutant(data['dna']))

if __name__ == '__main__':
    main()