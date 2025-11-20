# smooth-text-animation/smooth_text_animation/__init__.py
"""
Smooth Text Animation - Beautiful text animations for terminal
"""

__version__ = "0.1.0"
__author__ = "traitimtrongvag"
__email__ = "tbinh831@gmail.com"

from .animations import (
    animated_line,
    animated_line_dual,
    fade_in_text,
    marquee_text,
    wave_text,
    blinking_text,
    random_fill,
    reverse_text,
    rotate_text,
    combined_animation_simultaneous,
)

__all__ = [
    "animated_line",
    "animated_line_dual",
    "fade_in_text",
    "marquee_text",
    "wave_text",
    "blinking_text",
    "random_fill",
    "reverse_text",
    "rotate_text",
    "combined_animation_simultaneous",
]