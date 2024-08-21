import ast
from src.statements import assign, create_if, create_for
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
                for inst in call(obj.value):
                    instructions_list.append(inst.upper())

        if isinstance(obj, ast.If):
            for inst in create_if(obj):
                instructions_list.append(inst.upper())

        if isinstance(obj, ast.For):
            for inst in create_for(obj):
                instructions_list.append(inst.upper())

if __name__ == '__main__':
    instructions_list = []
    main()
    for index, instruction in enumerate(instructions_list, start=1):
        if "GOTO " in instruction:
            goto_i = instruction.index('GOTO ') + 5
            instruction = instruction[:goto_i] + f"{int(instruction[goto_i:]) + index:02d}"
            print(f'{index:02d} {instruction}')
        else:
            print(f'{index:02d} {instruction}')
