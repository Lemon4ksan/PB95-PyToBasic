import math
from typing import Union
from random import randint

def color(value: int) -> None:
    """Set color of next graphical elements. Dummy function. Used as an alias for COLOR in PBasic.

    Args:
        value (:obj:`int`): Index of a value. Must be in range from 1 to 16.

    Raises:
        ValueError: Color value out of range.
    """

    if value not in range(1, 17):
        raise ValueError('Color value out of range.')

def fill(x: int, y: int, fill_color: int) -> None:
    """Fill a closed contour of pixels with a specific color. Dummy function. Used as an alias for FILL in PBasic.

    Args:
        x (:obj:`int`): X coordinate.
        y (:obj:`int`): Y coordinate.
        fill_color (:obj:`int`): color index. Must be in range from 1 to 16.

    Raises:
        ValueError: Fill_color value out of range
    """

    if fill_color not in range(1, 17):
        raise ValueError('Color value out of range.')

def cls() -> None:
    """Clear screen. Dummy function. Used as an alias for CLS in PBasic."""

def sin(value: Union[int, float]) -> float:
    """Return the sin of a value. Used as an alias for TAN in PBasic.

    Args:
        value (:obj:`int`): A value to find sin of.

    Returns:
        :obj:`float`: sin of a value.
    """

    return math.sin(value)

def cos(value: Union[int, float]) -> float:
    """Return the cos of a value. Used as an alias for TAN in PBasic.

    Args:
        value (:obj:`int`): A value to find cos of.

    Returns:
        :obj:`float`: cos of a value.
    """

    return math.cos(value)

def tan(value: Union[int, float]) -> float:
    """Return the tan of a value. Used as an alias for TAN in PBasic.

    Args:
        value (:obj:`int`): A value to find tan of.

    Returns:
        :obj:`float`: tan of a value.
    """

    return math.tan(value)

def rnd(value: int) -> int:
    """Generate a random number between 1 and value, including both end points. Used as an alias for RND in PBasic.

    Args:
        value (:obj:`int`):

    Returns:
        :obj:`int`: Random integer.
    """

    return randint(1, value)

def background(value: int) -> None:
    """Set the background color. Dummy function. Used as an alias for BACKGROUND in PBasic.

    Args:
        value (:obj:`int`): Index of a value. Must be in range from 1 to 16.

    Raises:
        ValueError: Color value out of range.
        """

    if value not in range(1, 17):
        raise ValueError('Color value out of range.')

def plot(x: int, y: int) -> None:
    """Create a point at the given coordinates. Dummy function. Used as an alias for PLOT in PBasic.

    Args:
        x (:obj:`int`): X coordinate.
        y (:obj:`int`): Y coordinate.
    """

def line(x1: int, y1: int, x2: int, y2: int) -> None:
    """Create a line from point (x1, y1) to the point (x2, y2). Dummy function, used as an alias for LINE in PBasic.

    Args:
        x1 (:obj:`int`): X1 coordinate.
        y1 (:obj:`int`): Y1 coordinate.
        x2 (:obj:`int`): X2 coordinate.
        y2 (:obj:`int`): Y2 coordinate.
    """

def circle(x: int, y: int, radius: int) -> None:
    """Create a circle at point (x, y) with the given radius. Dummy function, used as an alias for CIRCLE in PBasic.

    Args:
        x (:obj:`int`): X coordinate.
        y (:obj:`int`): Y coordinate.
        radius (:obj:`int`): Radius of a circle.
    """
