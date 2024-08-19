import ast
from src.statements import assign
from src.expressions import call

def read_ast(body: list, instructions_list: list):
    for obj in body:

        if isinstance(obj, ast.Assign):
            for inst in assign(obj):
                instructions_list.append(inst)

        if isinstance(obj, ast.Expr):
            if isinstance(obj.value, ast.Call):
                instructions_list.append(call(obj.value))
