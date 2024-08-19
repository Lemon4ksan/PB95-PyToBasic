import ast

SUPPORTED_BINARY_OPERAIONS = [ast.Add, ast.Sub, ast.Mult, ast.Div, ast.Mod, ast.Pow]

SUPPORTED_FUNCTIONS = ['print']

BASE_OPERATIONS = {
    ast.Add: '+',
    ast.Sub: '-',
    ast.Mult: '*',
    ast.Div: '/',
}
