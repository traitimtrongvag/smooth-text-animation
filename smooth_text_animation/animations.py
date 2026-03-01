# smooth-text-animation/smooth_text_animation/animations.py
"""
Main animation functions for text effects
"""

import sys
import time
import random

from .utils import validate_delay, colorize_text, clear_line


def animated_line(text, delay=0.05):
    """
    Typing effect animation from left to right.

    Args:
        text (str): Text to display.
        delay (float): Delay between each character (seconds).
    """
    delay = validate_delay(delay)
    for i in range(len(text) + 1):
        sys.stdout.write("\r" + text[:i])
        sys.stdout.flush()
        time.sleep(delay)
    print()


def animated_line_dual(text, delay=0.1):
    """
    Animation appearing from both sides to center.

    Args:
        text (str): Text to display.
        delay (float): Delay between each step (seconds).
    """
    delay = validate_delay(delay)
    length = len(text)
    for i in range(length // 2 + 1):
        left_part = text[:i]
        right_part = text[length - i:]
        sys.stdout.write(
            "\r" + left_part
            + " " * (length - len(left_part) - len(right_part))
            + right_part
        )
        sys.stdout.flush()
        time.sleep(delay)
    print()


def fade_in_text(text, delay=0.2):
    """
    Text fade-in effect from dim to bright.

    Args:
        text (str): Text to display.
        delay (float): Delay between brightness levels (seconds).
    """
    delay = validate_delay(delay)
    brightness_levels = [90, 37, 97]
    for level in brightness_levels:
        sys.stdout.write(f"\r{colorize_text(text, level)}")
        sys.stdout.flush()
        time.sleep(delay)
    print(text)


def marquee_text(text, width=30, delay=0.1):
    """
    Scrolling text effect from right to left.

    Args:
        text (str): Text to display.
        width (int): Display screen width.
        delay (float): Delay between each step (seconds).
    """
    delay = validate_delay(delay)
    padded_text = " " * width + text + " " * width
    for i in range(len(padded_text) - width + 1):
        sys.stdout.write("\r" + padded_text[i:i + width])
        sys.stdout.flush()
        time.sleep(delay)
    print()


def wave_text(text, delay=0.1, repeat=3):
    """
    Loading effect with dots.

    Args:
        text (str): Text to display.
        delay (float): Delay between each step (seconds).
        repeat (int): Number of times to repeat the effect.
    """
    delay = validate_delay(delay)
    wave = ["", ".", "..", "..."]
    for _ in range(repeat):
        for w in wave:
            sys.stdout.write("\r" + text + w + " " * (3 - len(w)))
            sys.stdout.flush()
            time.sleep(delay)
    print()


def blinking_text(text, repeat=5, delay=0.3):
    """
    Blinking warning effect.

    Args:
        text (str): Text to display.
        repeat (int): Number of blinks.
        delay (float): Delay between each blink (seconds).
    """
    delay = validate_delay(delay)
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
    Characters appear randomly one by one.

    Args:
        text (str): Text to display.
        delay (float): Delay between each character (seconds).
    """
    delay = validate_delay(delay)
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
    Text appears from right to left.

    Args:
        text (str): Text to display.
        delay (float): Delay between each character (seconds).
    """
    delay = validate_delay(delay)
    reversed_text = text[::-1]
    for i in range(len(text) + 1):
        sys.stdout.write("\r" + reversed_text[:i][::-1])
        sys.stdout.flush()
        time.sleep(delay)
    print()


def rotate_text(text, delay=0.2, cycles=10):
    """
    Loading effect with rotating characters | / - \\.

    Args:
        text (str): Text to display.
        delay (float): Delay between each frame (seconds).
        cycles (int): Number of complete rotation cycles.
    """
    delay = validate_delay(delay)
    rotations = ["|", "/", "-", "\\"]
    for _ in range(cycles):
        for rot in rotations:
            sys.stdout.write(f"\r{rot} {text}")
            sys.stdout.flush()
            time.sleep(delay)
    print()


def _animated_fade_dual(text, delay=0.1):
    """Fade-in effect appearing from both ends to center."""
    length = len(text)
    brightness_levels = [90, 37, 97]
    num_brightness_levels = len(brightness_levels)

    for i in range(length // 2 + 1):
        brightness = brightness_levels[min(i, num_brightness_levels - 1)]
        left_part = text[:i]
        right_part = text[length - i:]
        clear_line()
        sys.stdout.write(
            f"\033[{brightness}m"
            + left_part
            + " " * (length - len(left_part) - len(right_part))
            + right_part
            + "\033[0m"
        )
        sys.stdout.flush()
        time.sleep(delay)


def _fade_out_dual(text, delay=0.1):
    """Fade-out effect disappearing from center to both ends."""
    length = len(text)
    for i in range(length // 2 + 1):
        left_part = text[:length // 2 - i]
        right_part = text[length // 2 + i:]
        clear_line()
        sys.stdout.write(
            left_part
            + " " * (length - len(left_part) - len(right_part))
            + right_part
        )
        sys.stdout.flush()
        time.sleep(delay)
    clear_line()


def combined_animation_simultaneous(text, delay=0.1, pause=0.5):
    """
    Combined appear and disappear effect (both sides).

    Args:
        text (str): Text to display.
        delay (float): Delay between each step (seconds).
        pause (float): Pause time between fade-in and fade-out (seconds).
    """
    _animated_fade_dual(text, delay=validate_delay(delay))
    time.sleep(validate_delay(pause))
    _fade_out_dual(text, delay=validate_delay(delay))


def glitch_text(text, delay=0.05, intensity=3):
    """
    Digital glitch effect with random character swaps.

    Args:
        text (str): Text to display.
        delay (float): Delay between glitch frames (seconds).
        intensity (int): Number of glitch iterations before resolving.
    """
    delay = validate_delay(delay)
    glitch_chars = "!@#$%^&*()_+-=[]{}|;:,.<>?"

    for _ in range(intensity):
        glitched = list(text)
        num_glitches = random.randint(1, max(1, len(text) // 3))
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
    Cycles through rainbow colors using ANSI codes.

    Args:
        text (str): Text to display.
        delay (float): Delay between color changes (seconds).
    """
    delay = validate_delay(delay)
    colors = [31, 33, 32, 36, 34, 35]  # Red, Yellow, Green, Cyan, Blue, Magenta
    for color in colors:
        sys.stdout.write(f"\r{colorize_text(text, color)}")
        sys.stdout.flush()
        time.sleep(delay)
    print()


def matrix_reveal(text, delay=0.05):
    """
    Matrix-style cascading reveal effect.

    Args:
        text (str): Text to display.
        delay (float): Delay between each character scramble step (seconds).
    """
    delay = validate_delay(delay)
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
    Realistic typing with occasional mistakes and corrections.

    Args:
        text (str): Text to display.
        delay (float): Base delay between characters (seconds).
        mistake_probability (float): Probability of making a typing mistake (0.0–1.0).
    """
    delay = validate_delay(delay)
    mistake_probability = max(0.0, min(1.0, mistake_probability))
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
        # Clamp jitter so sleep is always non-negative
        jitter = random.uniform(-0.02, 0.04)
        time.sleep(max(0.0, delay + jitter))
        i += 1
    print()


def bounce_text(text, delay=0.1, bounces=3):
    """
    Bouncing animation using vertical spacing.

    Args:
        text (str): Text to display.
        delay (float): Delay between bounce frames (seconds).
        bounces (int): Number of complete bounce cycles.
    """
    delay = validate_delay(delay)
    heights = [0, 1, 2, 3, 2, 1, 0]

    for _ in range(bounces):
        for height in heights:
            sys.stdout.write("\r" + "\n" * height + text + "\033[K")
            sys.stdout.flush()
            time.sleep(delay)
            if height > 0:
                sys.stdout.write(f"\033[{height}A")
    print()


def scramble_solve(text, delay=0.05, iterations=20):
    """
    Scrambled text gradually resolving to the correct message.

    Args:
        text (str): Text to display.
        delay (float): Delay between solve steps (seconds).
        iterations (int): Number of solving iterations.
    """
    delay = validate_delay(delay)
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
    Text slides in from the specified direction.

    Args:
        text (str): Text to display.
        delay (float): Delay between slide steps (seconds).
        direction (str): Direction to slide from — ``'left'`` or ``'right'``.

    Raises:
        ValueError: If *direction* is not ``'left'`` or ``'right'``.
    """
    if direction not in ("left", "right"):
        raise ValueError(f"direction must be 'left' or 'right', got {direction!r}")

    delay = validate_delay(delay)
    length = len(text)

    if direction == "left":
        for i in range(length + 1):
            sys.stdout.write("\r" + " " * (length - i) + text[:i])
            sys.stdout.flush()
            time.sleep(delay)
    else:
        for i in range(length + 1):
            sys.stdout.write("\r" + text[length - i:])
            sys.stdout.flush()
            time.sleep(delay)
    print()


def pulse_text(text, delay=0.2, pulses=5):
    """
    Pulsing brightness effect cycling dim → normal → bold.

    Args:
        text (str): Text to display.
        delay (float): Delay between pulse states (seconds).
        pulses (int): Number of pulse cycles.
    """
    delay = validate_delay(delay)
    styles = [
        f"\033[2m{text}\033[0m",   # Dim
        text,                        # Normal
        f"\033[1m{text}\033[0m",   # Bold
        text,                        # Normal
    ]
    for _ in range(pulses):
        for style in styles:
            sys.stdout.write("\r" + style)
            sys.stdout.flush()
            time.sleep(delay)
    print()


def reveal_mask(text, delay=0.1, mask_char="█"):
    """
    Reveal effect with a moving mask uncovering text left to right.

    Args:
        text (str): Text to display.
        delay (float): Delay between reveal steps (seconds).
        mask_char (str): Character used as the mask.
    """
    delay = validate_delay(delay)
    for i in range(len(text) + 1):
        display = text[:i] + mask_char * (len(text) - i)
        sys.stdout.write("\r" + display)
        sys.stdout.flush()
        time.sleep(delay)
    print()


def zigzag_text(text, delay=0.08):
    """
    Characters appear in zigzag pattern — even indices first, then odd.

    Args:
        text (str): Text to display.
        delay (float): Delay between each character (seconds).
    """
    delay = validate_delay(delay)
    result = [" "] * len(text)
    indices = list(range(0, len(text), 2)) + list(range(1, len(text), 2))

    for idx in indices:
        result[idx] = text[idx]
        sys.stdout.write("\r" + "".join(result))
        sys.stdout.flush()
        time.sleep(delay)
    print()


def expanding_center(text, delay=0.1):
    """
    Text expands outward from the center character.

    Args:
        text (str): Text to display.
        delay (float): Delay between expansion steps (seconds).
    """
    delay = validate_delay(delay)
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
    Neon-style flicker effect with color and brightness variation.

    Args:
        text (str): Text to display.
        delay (float): Delay between flicker states (seconds).
        flickers (int): Number of flicker events before settling.
    """
    delay = validate_delay(delay)
    neon_color = 35  # Magenta

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
