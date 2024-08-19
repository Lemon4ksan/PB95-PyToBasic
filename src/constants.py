import ast

SUPPORTED_OPERAIONS = [ast.Add, ast.Sub, ast.Mult, ast.Div, ast.Mod, ast.Pow]

BASE_OPERATIONS = {
    ast.Add: '+',
    ast.Sub: '-',
    ast.Mult: '*',
    ast.Div: '/',
}
