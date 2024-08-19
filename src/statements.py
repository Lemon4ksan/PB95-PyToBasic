import ast
from .expressions import bin_op, call

def assign(obj: ast.Assign) -> list[str]:
    """Assign statement.

    Examples:
        1:: a = 10:
            obj.targets = [Name(id='a')], obj.value = Constant(value=10)
        2:: a = b = 10:
            obj.targets = [Name(id='a'), Name(id='b')], obj.value = Constant(value=10)
        3:: a = b:
            obj.targets = [Name(id='a')], obj.value = Name(id='b')
        4.1:: a, b = 10, 20:
            obj.targets = [Tuple(elts[Name(id='a'), Name(id='b')])],
            obj.value = [Tuple(elts[Constant(value=10), Constant(value=20)])]
        4.2:: a, b = c, 10:
            obj.targets = [Tuple(elts[Name(id='a'), Name(id='b')])],
            obj.value = [Tuple(elts[Name(id='c'), Constant(value=10)])]
        5:: a = 15 + 10:
            obj.targets = [Name(id='a')], obj.value = BinOp(left=Constant(value=15)
                                                            op=Add()
                                                            right=Constant(value=10)
        6:: a = input():
            obj.targets = [Name(id='a')]
            obj.value = Call(func=Name(id='input'), args=[], kwargs=[])
    """

    result = []
    for target in obj.targets:
        # target: ast.Name

        if isinstance(target, ast.Name) and isinstance(obj.value, ast.Constant):  # ex. 1-2
            result.append(f"LET {str(target.id)} = {repr(obj.value.value).replace("'", '"')}")

        elif isinstance(target, ast.Name) and isinstance(obj.value, ast.Name):  # ex. 3
            result.append(f"LET {str(target.id)} = {str(obj.value.id)}")

        elif isinstance(target, ast.Tuple) and isinstance(obj.value, ast.Tuple):  # ex. 4
            for elt_name, elt_value in zip(target.elts, obj.value.elts):

                if isinstance(elt_value, ast.Constant):  # ex. 4.1
                    result.append(f"LET {str(elt_name.id)} = {repr(elt_value.value).replace("'", '"')}")

                elif isinstance(elt_value, ast.Name):  # ex. 4.2
                    if isinstance(elt_value.ctx, ast.Load):
                        result.append(f"LET {str(elt_name.id)} = {str(elt_value.id)}")
                    else:
                        result.append(f"LET {str(elt_name.id)} = {repr(elt_value.id).replace("'", '"')}")

        elif isinstance(obj.value, ast.BinOp):  # ex. 5
            result.append(f"LET {str(target.id)} = {bin_op(obj.value)}")

        elif isinstance(obj.value, ast.Call):
            if obj.value.func.id == 'input':
                result.append(f"INPUT {target.id}")
            else:
                result.append(f"{target.id} = {call(obj.value)}")

    return result
