import ast

SUPPORTED_BINARY_OPERAIONS = [ast.Add, ast.Sub, ast.Mult, ast.Div, ast.Pow]

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

SUPPORTED_COMPARE_OPERATIONS = {
    ast.Eq: '==',
    ast.Gt: '>',
    ast.Lt: '<'
}

BASE_OPERATIONS = {
    ast.Add: '+',
    ast.Sub: '-',
    ast.Mult: '*',
    ast.Div: '/',
}
