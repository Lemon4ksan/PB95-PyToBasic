import ast
from .constants import SUPPORTED_OPERAIONS

def bin_op(obj: ast.BinOp, operaion_stack=None) -> str:
    if type(obj.op) not in SUPPORTED_OPERAIONS:
        raise NotImplementedError(f'Operaion {type(obj.op)} is not implemented')

    if operaion_stack is None:
        operation_stack = []

    if isinstance(obj.right, ast.BinOp):
        operation_stack.append(bin_op(obj.right, operaion_stack))

        right = ''
        for operation in operation_stack:
            right += operation
        return f'{str(obj.left.value)} + {right}'

    else:
        right = obj.right
        return f'{str(obj.left.value)} + {str(right.value)}'
