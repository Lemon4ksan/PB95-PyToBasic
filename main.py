import ast
from src.utils import read_ast

def main():
    with open('programm.py', 'r') as file:
        tree = ast.parse(file.read())

    read_ast(tree.body, instructions_list)

if __name__ == '__main__':
    instructions_list = []
    main()
    for index, instruction in enumerate(instructions_list, start=1):
        print(f'{index:02d} {instruction.upper()}')
