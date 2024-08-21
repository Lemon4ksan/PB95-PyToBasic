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
from .constants import SUPPORTED_BINARY_OPERAIONS, BASE_OPERATIONS, SUPPORTED_FUNCTIONS

def bin_op(obj: ast.BinOp, operation_stack=None) -> str:
    """Handle binary operation. Supports + - * /

    Explanation:
        If left or right part is another binary operation, we recursively parse it and add to the operation stack.

        If current operation is - and right bin_op doesn't contain * or / :: we add braces to set right execution order.

        If current operation is both * or / and right bin_op contains both * or / :: we add braces to set right execution order.

        If current operaion is both * or / and left bin_op contains both + or - :: we add braces to set right execution order.
    """

    if type(obj.op) not in SUPPORTED_BINARY_OPERAIONS:
        raise NotImplementedError(f"Operaion {type(obj.op)} is not implemented")
    elif any([isinstance(obj.left, ast.Str), isinstance(obj.right, ast.Str)]):
        raise TypeError("Can't concatonate strings in PBasic")

    left = ''
    right = ''

    if operation_stack is None:
        operation_stack = []

    if isinstance(obj.left, ast.BinOp):
        operation_stack.append(bin_op(obj.left, operation_stack))

        for operation in operation_stack:
            if type(obj.op) in [ast.Mult, ast.Div] and any(['+' in operation, '-' in operation]):
                left += f'({operation})'
            else:
                left += operation
        operation_stack.clear()
    elif isinstance(obj.left, ast.Call):
        left = call(obj.left)[0]
    else:
        left = obj.left.value

    if isinstance(obj.right, ast.BinOp):
        operation_stack.append(bin_op(obj.right, operation_stack))

        for operation in operation_stack:
            if type(obj.op) in [ast.Sub] and all(['*' not in operation, '/' not in operation])\
                    or type(obj.op) in [ast.Mult, ast.Div] and any(['*' in operation, '/' in operation]):
                right += f'({operation})'
            else:
                right += operation
        operation_stack.clear()
    elif isinstance(obj.right, ast.Call):
        right = call(obj.right)[0]
    else:
        right = obj.right.value

    return f"{left} {BASE_OPERATIONS[type(obj.op)]} {right}"

def call(obj: ast.Call) -> list[str]:
    """Create a function call.

    If function is not supported, NotImplementedError will be raised.
    """

    if obj.func.id not in SUPPORTED_FUNCTIONS:
        raise NotImplementedError(f'Function {type(obj.func.id)} is not implemented')

    result = []

    for arg in obj.args:
        if isinstance(arg, ast.Name):
            result.append(f"{obj.func.id.upper()} {str(arg.id)}")

        elif isinstance(arg, ast.Constant):

            if isinstance(arg.value, str):
                result.append(f"{obj.func.id.upper()} {repr(arg.value).replace("'", '"')}")
            else:
                result.append(f"{obj.func.id.upper()} {str(arg.value)}")

        elif isinstance(arg, ast.BinOp):
            result.append(f"{obj.func.id.upper()} {bin_op(arg)}")

        elif isinstance(arg, ast.Call):
            line = []
            for inst in call(arg):
                line.append(inst)

            result.append(f"{obj.func.id.upper()} {' '.join(line)}")

    return result
