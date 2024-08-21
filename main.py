"""MIT License

Copyright (c) 2024 Bananchiki

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE."""

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
