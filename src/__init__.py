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

from .constants import SUPPORTED_BINARY_OPERAIONS
from .constants import BASE_OPERATIONS
from .constants import SUPPORTED_FUNCTIONS
from .constants import SUPPORTED_COMPARE_OPERATIONS

from .aliases import color
from .aliases import fill
from .aliases import cls
from .aliases import sin
from .aliases import cos
from .aliases import tan
from .aliases import rnd
from .aliases import background
from .aliases import plot
from .aliases import line
from .aliases import circle

from .expressions import bin_op
from .expressions import call

from .statements import assign
from .statements import create_if

__all__ = [
    'SUPPORTED_BINARY_OPERAIONS',
    'BASE_OPERATIONS',
    'SUPPORTED_FUNCTIONS',
    'SUPPORTED_COMPARE_OPERATIONS',
    'create_if',
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
    'circle',
    'bin_op',
    'call',
    'assign'
]
