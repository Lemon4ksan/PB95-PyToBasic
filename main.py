import ast
from src.statements import assign
from src.expressions import call

def main():
    with open('programm.py', 'r') as file:
        tree = ast.parse(file.read())

    for obj in tree.body:

        if isinstance(obj, ast.Assign):
            for inst in assign(obj):
                instructions_list.append(inst.upper())

        if isinstance(obj, ast.Expr):
            if isinstance(obj.value, ast.Call):
                instructions_list.append(call(obj.value).upper())

if __name__ == '__main__':
    instructions_list = []
    main()
    for index, instruction in enumerate(instructions_list):
        print(f'{index + 1:02d} {instruction}')
