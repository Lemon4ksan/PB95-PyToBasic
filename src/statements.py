import ast
from .expressions import bin_op, call
from .constants import SUPPORTED_COMPARE_OPERATIONS

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
            result.append(f"LET {str(target.id)}={repr(obj.value.value).replace("'", '"')}")

        elif isinstance(target, ast.Name) and isinstance(obj.value, ast.Name):  # ex. 3
            result.append(f"LET {str(target.id)}={str(obj.value.id)}")

        elif isinstance(target, ast.Tuple) and isinstance(obj.value, ast.Tuple):  # ex. 4
            for elt_name, elt_value in zip(target.elts, obj.value.elts):

                if isinstance(elt_value, ast.Constant):  # ex. 4.1
                    result.append(f"LET {str(elt_name.id)}={repr(elt_value.value).replace("'", '"')}")

                elif isinstance(elt_value, ast.Name):  # ex. 4.2
                    if isinstance(elt_value.ctx, ast.Load):
                        result.append(f"LET {str(elt_name.id)}={str(elt_value.id)}")
                    else:
                        result.append(f"LET {str(elt_name.id)}={repr(elt_value.id).replace("'", '"')}")

        elif isinstance(obj.value, ast.BinOp):  # ex. 5
            result.append(f"LET {str(target.id)}={bin_op(obj.value)}")

        elif isinstance(obj.value, ast.Call):
            if obj.value.func.id == 'input':
                result.append(f"INPUT {target.id}")
            else:
                result.append(f"{target.id}={call(obj.value)}")

    return result

def create_if(obj: ast.If) -> list[str]:
    line = ['IF']
    result = []
    temp = []

    if isinstance(obj.test, ast.Compare):
        if type(obj.test.ops[0]) not in SUPPORTED_COMPARE_OPERATIONS:
            raise NotImplementedError(f"Operaion {type(obj.test.ops[0])} is not implemented")
        if len(obj.test.comparators) > 1:
            raise NotImplementedError("Can't use more than 1 comparison in an if statement in PBasic")
        if any([isinstance(obj.test.left, ast.Str), isinstance(obj.test.comparators[0], ast.Str)]):
            raise NotImplementedError(f"Can't compare strings in PBasic")

        if isinstance(obj.test.left, ast.Name):
            left = str(obj.test.left.id)
        elif isinstance(obj.test.left, ast.Constant):
            left = str(obj.test.left.value)

        if isinstance(obj.test.comparators[0], ast.Name):
            right = str(obj.test.comparators[0].id)
        elif isinstance(obj.test.comparators[0], ast.Constant):
            right = str(obj.test.comparators[0].id)

        line.append(f'{left}{SUPPORTED_COMPARE_OPERATIONS[type(obj.test.ops[0])]}{right}')

    for else_obj in obj.orelse:

        if isinstance(else_obj, ast.Assign):
            for inst in assign(else_obj):
                temp.append(inst)

        if isinstance(else_obj, ast.Expr):
            if isinstance(else_obj.value, ast.Call):
                temp.append(call(else_obj.value))

        if isinstance(else_obj, ast.If):
            for inst in create_if(else_obj):
                temp.append(inst)

    line.append(f'THEN GOTO {len(temp) + 2}')
    result.append(" ".join(line))
    for temp_obj in temp:
        result.append(temp_obj)
    temp.clear()

    for if_obj in obj.body:

        if isinstance(if_obj, ast.Assign):
            for inst in assign(if_obj):
                temp.append(inst)

        if isinstance(if_obj, ast.Expr):
            if isinstance(if_obj.value, ast.Call):
                temp.append(call(if_obj.value))

        if isinstance(if_obj, ast.If):
            for inst in create_if(if_obj):
                temp.append(inst)

    result.append(f"GOTO {len(temp) + 1}")
    for temp_obj in temp:
        result.append(temp_obj)
    result.append("REM *ELSE EXIT*")

    return result
