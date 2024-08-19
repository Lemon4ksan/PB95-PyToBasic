import ast
from .constants import SUPPORTED_BINARY_OPERAIONS, BASE_OPERATIONS, SUPPORTED_FUNCTIONS

def bin_op(obj: ast.BinOp, operation_stack=None) -> str:
    """Binary operaion. Supports + - * /

    Explanation:
        If left or right part is another binary operation, we recursively parse it and add to the operation stack.
        If current operation is - and right bin_op doesn't contain * or / (we must say that subscription must happen
        after other operation but not when it will happen anyway) OR current operation is * or /
        and right bin_op contains * or / (we must say that next operation of division/multiplication must happen first,
        but not when it will happen anyway) :: we add braces to set right execution order.

        To exclude unnecessary braces, we simply don't add them when bin_op is in left part,
        since it will execute first anyway.
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

def call(obj: ast.Call) -> str:
    if obj.func.id not in SUPPORTED_FUNCTIONS:
        raise NotImplementedError(f'Function {type(obj.func.id)} is not implemented')

    result = []

    match obj.func.id:
        case 'print':
            result.append('PRINT')
            for arg in obj.args:
                if isinstance(arg, ast.Name):
                    result.append(str(arg.id))
                elif isinstance(arg, ast.Constant):

                    if isinstance(arg.value, str):
                        result.append(repr(arg.value).replace("'", '"'))
                    else:
                        result.append(str(arg.value))
                elif isinstance(arg, ast.BinOp):
                    result.append(bin_op(arg))

    return ' '.join(result)
