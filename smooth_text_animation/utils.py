"""
Utility functions for smooth_text_animation package
"""

import sys
import time
from typing import List, Tuple


def clear_line():
    """Clear the current line in terminal"""
    sys.stdout.write("\r\033[K")
    sys.stdout.flush()


def move_cursor_up(lines: int = 1):
    """
    Move cursor up by specified number of lines
    
    Args:
        lines (int): Number of lines to move up
    """
    sys.stdout.write(f"\033[{lines}A")
    sys.stdout.flush()


def move_cursor_down(lines: int = 1):
    """
    Move cursor down by specified number of lines
    
    Args:
        lines (int): Number of lines to move down
    """
    sys.stdout.write(f"\033[{lines}B")
    sys.stdout.flush()


def get_terminal_size() -> Tuple[int, int]:
    """
    Get terminal size (width, height)
    
    Returns:
        tuple: (width, height) of terminal
    """
    try:
        import shutil
        size = shutil.get_terminal_size()
        return size.columns, size.lines
    except:
        return 80, 24  # Default fallback


def colorize_text(text: str, color_code: int) -> str:
    """
    Add ANSI color code to text
    
    Args:
        text (str): Text to colorize
        color_code (int): ANSI color code (30-37 for foreground, 90-97 for bright)
    
    Returns:
        str: Colorized text with ANSI codes
    """
    return f"\033[{color_code}m{text}\033[0m"


def validate_delay(delay: float) -> float:
    """
    Validate and clamp delay value
    
    Args:
        delay (float): Delay value to validate
    
    Returns:
        float: Valid delay value (>= 0)
    """
    return max(0.0, float(delay))


def calculate_center_position(text: str, width: int = None) -> int:
    """
    Calculate the starting position to center text
    
    Args:
        text (str): Text to center
        width (int): Terminal width (auto-detected if None)
    
    Returns:
        int: Starting position for centered text
    """
    if width is None:
        width, _ = get_terminal_size()
    
    text_length = len(text)
    if text_length >= width:
        return 0
    
    return (width - text_length) // 2


def repeat_animation(func, *args, times: int = 1, pause: float = 0.5, **kwargs):
    """
    Repeat an animation function multiple times with pause
    
    Args:
        func: Animation function to repeat
        *args: Positional arguments for the function
        times (int): Number of times to repeat
        pause (float): Pause between repetitions in seconds
        **kwargs: Keyword arguments for the function
    """
    for i in range(times):
        func(*args, **kwargs)
        if i < times - 1:  # Don't pause after last iteration
            time.sleep(pause)


def print_centered(text: str, width: int = None):
    """
    Print text centered in terminal
    
    Args:
        text (str): Text to print
        width (int): Terminal width (auto-detected if None)
    """
    if width is None:
        width, _ = get_terminal_size()
    
    padding = calculate_center_position(text, width)
    print(" " * padding + text)


def create_progress_bar(current: int, total: int, width: int = 50, 
                       filled_char: str = "█", empty_char: str = "░") -> str:
    """
    Create a text-based progress bar
    
    Args:
        current (int): Current progress value
        total (int): Total/maximum value
        width (int): Width of progress bar in characters
        filled_char (str): Character for filled portion
        empty_char (str): Character for empty portion
    
    Returns:
        str: Progress bar string
    """
    if total == 0:
        return f"[{empty_char * width}] 0%"
    
    percentage = min(100, int((current / total) * 100))
    filled_width = int((current / total) * width)
    empty_width = width - filled_width
    
    bar = filled_char * filled_width + empty_char * empty_width
    return f"[{bar}] {percentage}%"


def split_text_to_lines(text: str, max_width: int) -> List[str]:
    """
    Split text into multiple lines based on max width
    
    Args:
        text (str): Text to split
        max_width (int): Maximum width per line
    
    Returns:
        list: List of text lines
    """
    words = text.split()
    lines = []
    current_line = []
    current_length = 0
    
    for word in words:
        word_length = len(word)
        
        if current_length + word_length + len(current_line) <= max_width:
            current_line.append(word)
            current_length += word_length
        else:
            if current_line:
                lines.append(" ".join(current_line))
            current_line = [word]
            current_length = word_length
    
    if current_line:
        lines.append(" ".join(current_line))
    
    return lines


def is_terminal_available() -> bool:
    """
    Check if running in a terminal that supports animations
    
    Returns:
        bool: True if terminal supports animations
    """
    return sys.stdout.isatty()


# Color constants for easy use
class Colors:
    """ANSI color codes"""
    BLACK = 30
    RED = 31
    GREEN = 32
    YELLOW = 33
    BLUE = 34
    MAGENTA = 35
    CYAN = 36
    WHITE = 37
    
    BRIGHT_BLACK = 90
    BRIGHT_RED = 91
    BRIGHT_GREEN = 92
    BRIGHT_YELLOW = 93
    BRIGHT_BLUE = 94
    BRIGHT_MAGENTA = 95
    BRIGHT_CYAN = 96
    BRIGHT_WHITE = 97


# Animation timing presets
class AnimationSpeed:
    """Predefined animation speed constants"""
    VERY_SLOW = 0.3
    SLOW = 0.15
    NORMAL = 0.08
    FAST = 0.04
    VERY_FAST = 0.01