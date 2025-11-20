# smooth-text-animation/smooth_text_animation/animations.py
"""
Main animation functions for text effects
"""

import sys
import time
import random


def animated_line(text, delay=0.05):
    """
    Typing effect animation from left to right
    
    Args:
        text (str): Text to display
        delay (float): Delay between each character (seconds)
    """
    for i in range(len(text) + 1):
        sys.stdout.write("\r" + text[:i])
        sys.stdout.flush()
        time.sleep(delay)
    print()


def animated_line_dual(text, delay=0.1):
    """
    Animation appearing from both sides to center
    
    Args:
        text (str): Text to display
        delay (float): Delay between each step (seconds)
    """
    length = len(text)
    for i in range(length // 2 + 1):
        left_part = text[:i]
        right_part = text[length - i:]
        sys.stdout.write("\r" + left_part + " " * (length - len(left_part) - len(right_part)) + right_part)
        sys.stdout.flush()
        time.sleep(delay)
    print()


def fade_in_text(text, delay=0.2):
    """
    Text fade-in effect from dim to bright
    
    Args:
        text (str): Text to display
        delay (float): Delay between brightness levels (seconds)
    """
    brightness_levels = [90, 37, 97]
    
    for level in brightness_levels:
        sys.stdout.write(f"\033[{level}m{text}\033[0m\r")
        sys.stdout.flush()
        time.sleep(delay)
    print(text)


def marquee_text(text, width=30, delay=0.1):
    """
    Scrolling text effect from right to left
    
    Args:
        text (str): Text to display
        width (int): Display screen width
        delay (float): Delay between each step (seconds)
    """
    padded_text = " " * width + text + " " * width
    for i in range(len(padded_text) - width + 1):
        sys.stdout.write("\r" + padded_text[i:i+width])
        sys.stdout.flush()
        time.sleep(delay)
    print()


def wave_text(text, delay=0.1, repeat=3):
    """
    Loading effect with dots
    
    Args:
        text (str): Text to display
        delay (float): Delay between each step (seconds)
        repeat (int): Number of times to repeat the effect
    """
    wave = ["", ".", "..", "..."]
    for _ in range(repeat):
        for w in wave:
            sys.stdout.write("\r" + text + w + " " * (3 - len(w)))
            sys.stdout.flush()
            time.sleep(delay)
    print()


def blinking_text(text, repeat=5, delay=0.3):
    """
    Blinking warning effect
    
    Args:
        text (str): Text to display
        repeat (int): Number of blinks
        delay (float): Delay between each blink (seconds)
    """
    for _ in range(repeat):
        sys.stdout.write("\r" + text)
        sys.stdout.flush()
        time.sleep(delay)
        sys.stdout.write("\r" + " " * len(text))
        sys.stdout.flush()
        time.sleep(delay)
    print(text)


def random_fill(text, delay=0.1):
    """
    Characters appear randomly one by one
    
    Args:
        text (str): Text to display
        delay (float): Delay between each character (seconds)
    """
    result = [" "] * len(text)
    indices = list(range(len(text)))
    while indices:
        idx = random.choice(indices)
        result[idx] = text[idx]
        sys.stdout.write("\r" + "".join(result))
        sys.stdout.flush()
        indices.remove(idx)
        time.sleep(delay)
    print()


def reverse_text(text, delay=0.2):
    """
    Text appears from right to left
    
    Args:
        text (str): Text to display
        delay (float): Delay between each character (seconds)
    """
    reversed_text = text[::-1]
    for i in range(len(text) + 1):
        sys.stdout.write("\r" + reversed_text[:i][::-1])
        sys.stdout.flush()
        time.sleep(delay)
    print()


def rotate_text(text, delay=0.2, cycles=10):
    """
    Loading effect with rotating characters | / - \\
    
    Args:
        text (str): Text to display
        delay (float): Delay between each character (seconds)
        cycles (int): Number of times to repeat the effect
    """
    rotations = ["|", "/", "-", "\\"]
    for _ in range(cycles):
        for rot in rotations:
            sys.stdout.write(f"\r{rot} {text}")
            sys.stdout.flush()
            time.sleep(delay)
    print()


def _animated_fade_dual(text, delay=0.1):
    """
    Fade-in effect appearing from both ends to center
    """
    length = len(text)
    brightness_levels = [90, 37, 97]
    num_brightness_levels = len(brightness_levels)

    for i in range(length // 2 + 1):
        brightness = brightness_levels[min(i, num_brightness_levels - 1)]
        left_part = text[:i]
        right_part = text[length - i:]
        
        sys.stdout.write("\r\033[K")
        sys.stdout.write(
            f"\033[{brightness}m" + left_part + " " * (length - len(left_part) - len(right_part)) + right_part + "\033[0m"
        )
        sys.stdout.flush()
        time.sleep(delay)


def _fade_out_dual(text, delay=0.1):
    """
    Fade-out effect disappearing from center to both ends
    """
    length = len(text)
    for i in range(length // 2 + 1):
        left_part = text[:length // 2 - i]
        right_part = text[length // 2 + i:]
        
        sys.stdout.write("\r\033[K")
        sys.stdout.write(
            left_part + " " * (length - len(left_part) - len(right_part)) + right_part
        )
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write("\r\033[K")
    sys.stdout.flush()


def combined_animation_simultaneous(text, delay=0.1, pause=0.5):
    """
    Combined appear and disappear effect (both sides)
    
    Args:
        text (str): Text to display
        delay (float): Delay between each step (seconds)
        pause (float): Pause time between fade-in and fade-out (seconds)
    """
    _animated_fade_dual(text, delay=delay)
    time.sleep(pause)
    _fade_out_dual(text, delay=delay)