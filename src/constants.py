import ast

SUPPORTED_BINARY_OPERAIONS = [ast.Add, ast.Sub, ast.Mult, ast.Div, ast.Mod, ast.Pow]

SUPPORTED_FUNCTIONS = [
    'print',
    'input',
    'color',
    'fill',
    'cls',
    'sin',
    'cos',
    'tan',
    'rnd',
    'background',
    'plot',
    'line',
    'circle'
]

BASE_OPERATIONS = {
    ast.Add: '+',
    ast.Sub: '-',
    ast.Mult: '*',
    ast.Div: '/',
}
