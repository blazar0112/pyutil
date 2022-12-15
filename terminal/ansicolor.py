"""
Simple utility to add ansi color
Use Colorama if you can prepare venv or pip install.
This is for code that can only use standard env.
See wiki for terminology.
https://en.wikipedia.org/wiki/ANSI_escape_code
"""

import enum
import re

# CSI (Control Sequence Introducer) sequences
_CSI = '\033['
# SGR (Select Graphic Rendition) parameters
_SGR = 'm'
_ANSI_ESCAPE = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')

class Style(enum.Enum):
    """
    Models single digit style code in SGR parameters
    """
    RESET       = 0
    BOLD        = 1
    FAINT       = 2
    ITALIC      = 3
    UNDERLINE   = 4
    SLOW_BLINK  = 5
    RAPID_BLINK = 6
    INVERT      = 7
    CONSEAL     = 8
    CROSSED_OUT = 9

class Color(enum.Enum):
    """
    Models color code x in SGR parameters 3x, 4x, 9x, 10x
    """
    BLACK       = 0
    RED         = 1
    GREEN       = 2
    YELLOW      = 3
    BLUE        = 4
    MAGENTA     = 5
    CYAN        = 6
    WHITE       = 7

def gen_ansi_sgr(
    fg_color: Color,
    bg_color: Color=None,
    fg_bright: bool=False,
    bg_bright: bool=False,
    style: Style=None
    ) -> str:
    """
    gen_ansi_sgr
    """
    code_list = []
    if style is not None:
        code_list.append(str(style.value))
    if fg_color is not None:
        if not fg_bright:
            code_list.append('3'+str(fg_color.value))
        else:
            code_list.append('9'+str(fg_color.value))
    if bg_color is not None:
        if not bg_bright:
            code_list.append('4'+str(bg_color.value))
        else:
            code_list.append('10'+str(bg_color.value))
    return _CSI+';'.join(code_list)+_SGR

def reset_ansi_sgr():
    """
    reset_ansi_sgr
    """
    return _CSI+_SGR

def strip_ansi_sgr(ansi_sgr_text):
    """
    strip_ansi_sgr
    """
    return _ANSI_ESCAPE.sub('', ansi_sgr_text)

def len_ansi_sgr(ansi_sgr_text):
    """
    len_ansi_sgr
    """
    return len(ansi_sgr_text)-len(strip_ansi_sgr(ansi_sgr_text))
