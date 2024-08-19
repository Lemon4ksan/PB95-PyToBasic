import ast
from .constants import SUPPORTED_OPERAIONS, BASE_OPERATIONS, PLACE_BRACKETS_WHEN

def bin_op(obj: ast.BinOp, operation_stack=None) -> str:
    if type(obj.op) not in SUPPORTED_OPERAIONS:
        raise NotImplementedError(f'Operaion {type(obj.op)} is not implemented')

    left = ''
    right = ''

    if operation_stack is None:
        operation_stack = []

    if isinstance(obj.left, ast.BinOp):
        operation_stack.append(bin_op(obj.left, operation_stack))

        for operation in operation_stack:
            if type(obj.op) in []:
                left += f'({operation})'
            else:
                left += operation
        operation_stack.clear()
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
    else:
        right = obj.right.value

    return f"{left} {BASE_OPERATIONS[type(obj.op)]} {right}"
