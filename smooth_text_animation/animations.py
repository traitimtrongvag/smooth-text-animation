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
    
def glitch_text(text, delay=0.05, intensity=3):
    """
    Glitch effect with random character replacements
    
    Args:
        text (str): Text to display
        delay (float): Delay between glitch frames (seconds)
        intensity (int): Number of glitch iterations
    """
    glitch_chars = "!@#$%^&*()_+-=[]{}|;:,.<>?"
    
    for _ in range(intensity):
        glitched = list(text)
        num_glitches = random.randint(1, len(text) // 3)
        
        for _ in range(num_glitches):
            pos = random.randint(0, len(text) - 1)
            glitched[pos] = random.choice(glitch_chars)
        
        sys.stdout.write("\r" + "".join(glitched))
        sys.stdout.flush()
        time.sleep(delay)
    
    sys.stdout.write("\r" + text)
    sys.stdout.flush()
    print()


def rainbow_text(text, delay=0.1):
    """
    Rainbow color effect cycling through ANSI colors
    
    Args:
        text (str): Text to display
        delay (float): Delay between color changes (seconds)
    """
    colors = [31, 33, 32, 36, 34, 35]  # Red, Yellow, Green, Cyan, Blue, Magenta
    
    for color in colors:
        sys.stdout.write(f"\r\033[{color}m{text}\033[0m")
        sys.stdout.flush()
        time.sleep(delay)
    print()


def matrix_reveal(text, delay=0.05):
    """
    Matrix-style cascading reveal effect
    
    Args:
        text (str): Text to display
        delay (float): Delay between each character (seconds)
    """
    chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789@#$%"
    result = list(text)
    
    for i in range(len(text)):
        for _ in range(random.randint(3, 8)):
            temp = result.copy()
            temp[i] = random.choice(chars)
            sys.stdout.write("\r" + "".join(temp))
            sys.stdout.flush()
            time.sleep(delay)
        
        result[i] = text[i]
        sys.stdout.write("\r" + "".join(result))
        sys.stdout.flush()
    print()


def typewriter_advanced(text, delay=0.08, mistake_probability=0.15):
    """
    Realistic typewriter effect with occasional mistakes and corrections
    
    Args:
        text (str): Text to display
        delay (float): Base delay between characters (seconds)
        mistake_probability (float): Probability of making a typing mistake
    """
    result = ""
    i = 0
    
    while i < len(text):
        if random.random() < mistake_probability and i > 0:
            wrong_char = random.choice("qwertyuiopasdfghjklzxcvbnm")
            result += wrong_char
            sys.stdout.write("\r" + result)
            sys.stdout.flush()
            time.sleep(delay)
            
            result = result[:-1]
            sys.stdout.write("\r" + result + " ")
            sys.stdout.flush()
            time.sleep(delay * 0.5)
        
        result += text[i]
        sys.stdout.write("\r" + result)
        sys.stdout.flush()
        time.sleep(delay + random.uniform(-0.02, 0.04))
        i += 1
    print()


def bounce_text(text, delay=0.1, bounces=3):
    """
    Bouncing animation effect using spacing
    
    Args:
        text (str): Text to display
        delay (float): Delay between bounce frames (seconds)
        bounces (int): Number of complete bounce cycles
    """
    heights = [0, 1, 2, 3, 2, 1, 0]
    
    for _ in range(bounces):
        for height in heights:
            sys.stdout.write("\r" + "\n" * height + text + "\033[K")
            sys.stdout.flush()
            time.sleep(delay)
            if height > 0:
                sys.stdout.write("\033[F" * height)
    print()


def scramble_solve(text, delay=0.05, iterations=20):
    """
    Scrambled text gradually solving to correct message
    
    Args:
        text (str): Text to display
        delay (float): Delay between solve steps (seconds)
        iterations (int): Number of solving iterations
    """
    chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()"
    current = [random.choice(chars) for _ in range(len(text))]
    solved = [False] * len(text)
    
    for iteration in range(iterations):
        for i in range(len(text)):
            if not solved[i]:
                if random.random() < (iteration / iterations) or iteration == iterations - 1:
                    current[i] = text[i]
                    solved[i] = True
                else:
                    current[i] = random.choice(chars)
        
        sys.stdout.write("\r" + "".join(current))
        sys.stdout.flush()
        time.sleep(delay)
    print()


def slide_in(text, delay=0.05, direction="left"):
    """
    Text slides in from specified direction
    
    Args:
        text (str): Text to display
        delay (float): Delay between slide steps (seconds)
        direction (str): Direction to slide from ('left', 'right')
    """
    length = len(text)
    
    if direction == "left":
        for i in range(length + 1):
            sys.stdout.write("\r" + " " * (length - i) + text[:i])
            sys.stdout.flush()
            time.sleep(delay)
    else:  # right
        for i in range(length + 1):
            sys.stdout.write("\r" + text[length - i:])
            sys.stdout.flush()
            time.sleep(delay)
    print()


def pulse_text(text, delay=0.2, pulses=5):
    """
    Pulsing effect using brightness and bold styling
    
    Args:
        text (str): Text to display
        delay (float): Delay between pulse states (seconds)
        pulses (int): Number of pulse cycles
    """
    styles = [
        f"\033[2m{text}\033[0m",      # Dim
        f"{text}",                      # Normal
        f"\033[1m{text}\033[0m",       # Bold
        f"{text}",                      # Normal
    ]
    
    for _ in range(pulses):
        for style in styles:
            sys.stdout.write("\r" + style)
            sys.stdout.flush()
            time.sleep(delay)
    print()


def reveal_mask(text, delay=0.1, mask_char="█"):
    """
    Text revealed by moving mask effect
    
    Args:
        text (str): Text to display
        delay (float): Delay between reveal steps (seconds)
        mask_char (str): Character used for masking
    """
    for i in range(len(text) + 1):
        display = text[:i] + mask_char * (len(text) - i)
        sys.stdout.write("\r" + display)
        sys.stdout.flush()
        time.sleep(delay)
    print()


def zigzag_text(text, delay=0.08):
    """
    Characters appear in zigzag pattern (alternating positions)
    
    Args:
        text (str): Text to display
        delay (float): Delay between each character (seconds)
    """
    result = [" "] * len(text)
    indices = []
    
    # Create zigzag pattern
    for i in range(0, len(text), 2):
        indices.append(i)
    for i in range(1, len(text), 2):
        indices.append(i)
    
    for idx in indices:
        result[idx] = text[idx]
        sys.stdout.write("\r" + "".join(result))
        sys.stdout.flush()
        time.sleep(delay)
    print()


def expanding_center(text, delay=0.1):
    """
    Text expands outward from center character
    
    Args:
        text (str): Text to display
        delay (float): Delay between expansion steps (seconds)
    """
    center = len(text) // 2
    result = [" "] * len(text)
    result[center] = text[center]
    
    sys.stdout.write("\r" + "".join(result))
    sys.stdout.flush()
    time.sleep(delay)
    
    for offset in range(1, max(center, len(text) - center) + 1):
        if center - offset >= 0:
            result[center - offset] = text[center - offset]
        if center + offset < len(text):
            result[center + offset] = text[center + offset]
        
        sys.stdout.write("\r" + "".join(result))
        sys.stdout.flush()
        time.sleep(delay)
    print()


def neon_flicker(text, delay=0.1, flickers=8):
    """
    Neon sign flicker effect with color variations
    
    Args:
        text (str): Text to display
        delay (float): Delay between flicker states (seconds)
        flickers (int): Number of flicker events
    """
    neon_color = 35  # Magenta for neon effect
    
    for _ in range(flickers):
        if random.random() < 0.3:
            sys.stdout.write("\r" + " " * len(text))
        else:
            brightness = random.choice([0, 1, 2])
            sys.stdout.write(f"\r\033[{brightness};{neon_color}m{text}\033[0m")
        sys.stdout.flush()
        time.sleep(delay)
    
    sys.stdout.write(f"\r\033[1;{neon_color}m{text}\033[0m")
    sys.stdout.flush()
    print()