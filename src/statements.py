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
    result = []
    condition = ['IF']
    else_stmt = []
    if_stmt = []

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

        condition.append(f'{left}{SUPPORTED_COMPARE_OPERATIONS[type(obj.test.ops[0])]}{right}')

    for else_obj in obj.orelse:

        if isinstance(else_obj, ast.Assign):
            for inst in assign(else_obj):
                else_stmt.append(inst)

        if isinstance(else_obj, ast.Expr):
            if isinstance(else_obj.value, ast.Call):
                for inst in call(else_obj.value):
                    else_stmt.append(inst)

        if isinstance(else_obj, ast.If):
            for inst in create_if(else_obj):
                else_stmt.append(inst)

        if isinstance(else_obj, ast.For):
            for inst in create_for(else_obj):
                else_stmt.append(inst)

    for if_obj in obj.body:

        if isinstance(if_obj, ast.Assign):
            for inst in assign(if_obj):
                if_stmt.append(inst)

        if isinstance(if_obj, ast.Expr):
            if isinstance(if_obj.value, ast.Call):
                for inst in call(if_obj.value):
                    if_stmt.append(inst)

        if isinstance(if_obj, ast.If):
            for inst in create_if(if_obj):
                if_stmt.append(inst)

        if isinstance(if_obj, ast.For):
            for inst in create_for(if_obj):
                if_stmt.append(inst)

    if len(else_stmt) == 1 and len(if_stmt) == 1:
        condition.append(f'THEN {if_stmt[0]}')
        result.append(" ".join(condition))
        result.append(f'ELSE {else_stmt[0]}')
    else:
        condition.append(f'THEN GOTO {len(else_stmt) + 2}')
        result.append(" ".join(condition))

        for else_obj in else_stmt:
            result.append(else_obj)

        result.append(f"GOTO {len(if_stmt) + 1}")

        for if_obj in if_stmt:
            result.append(if_obj)

        result.append("REM *ELSE EXIT*")

    return result

def create_for(obj: ast.For) -> list[str]:

    result = []
    body = []

    if not isinstance(obj.iter, ast.Call):
        raise NotImplementedError("Can only use range() created iterators.")
    elif obj.iter.func.id != 'range':
        raise NotImplementedError("Can only use range() created iterators.")
    elif obj.orelse:
        raise NotImplementedError("Can't use else statement in for loops.")

    if len(obj.iter.args) == 2:
        result.append(f"FOR {obj.target.id}={obj.iter.args[0].value} TO {obj.iter.args[1].value - 1}")  # Decreasing by 1 to match results with python
    else:
        result.append(f"FOR {obj.target.id}=0 TO {obj.iter.args[0].value}")

    for body_obj in obj.body:

        if isinstance(body_obj, ast.Break):
            raise NotImplementedError("Can't use break statement.")

        if isinstance(body_obj, ast.Assign):
            for inst in assign(body_obj):
                body.append(inst)

        if isinstance(body_obj, ast.Expr):
            if isinstance(body_obj.value, ast.Call):
                for inst in call(body_obj.value):
                    body.append(inst)

        if isinstance(body_obj, ast.If):
            for inst in create_if(body_obj):
                body.append(inst)

        if isinstance(body_obj, ast.For):
            for inst in create_for(body_obj):
                body.append(inst)

    for body_obj in body:
        result.append(body_obj)

    result.append(f"NEXT {obj.target.id}")

    return result
