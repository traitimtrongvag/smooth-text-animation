# Smooth Text Animation 🎨

Beautiful and smooth text animations for terminal output in Python.

## Features ✨

- **22 animation effects** for terminal text
- **Easy to use** — just import and call
- **Lightweight** — no external dependencies
- **Customizable** — adjust speed and behavior
- **Cross-platform** — works on Windows, macOS, and Linux

## Installation 📦

```bash
pip install smooth-text-animation
```

## Quick Start 🚀

```python
from smooth_text_animation import animated_line, wave_text, glitch_text

# Typing effect
animated_line("Hello, World!", delay=0.1)

# Loading effect
wave_text("Loading", delay=0.3)

# Glitch effect
glitch_text("SYSTEM ERROR", delay=0.05, intensity=5)
```

## Available Animations 🎭

### Original (v0.1.0)

#### 1. Animated Line — Typing Effect
```python
from smooth_text_animation import animated_line
animated_line("This text appears character by character!", delay=0.05)
```

#### 2. Dual Side Animation
```python
from smooth_text_animation import animated_line_dual
animated_line_dual("Text appears from both sides!", delay=0.1)
```

#### 3. Fade In Effect
```python
from smooth_text_animation import fade_in_text
fade_in_text("This text fades in gradually!", delay=0.2)
```

#### 4. Marquee Text — Scrolling
```python
from smooth_text_animation import marquee_text
marquee_text("This text scrolls across the screen!", width=30, delay=0.1)
```

#### 5. Wave Loading
```python
from smooth_text_animation import wave_text
wave_text("Loading", delay=0.3, repeat=3)
```

#### 6. Blinking Text
```python
from smooth_text_animation import blinking_text
blinking_text("ALERT!", repeat=5, delay=0.3)
```

#### 7. Random Fill
```python
from smooth_text_animation import random_fill
random_fill("Characters appear randomly!", delay=0.1)
```

#### 8. Reverse Text
```python
from smooth_text_animation import reverse_text
reverse_text("Text appears from right to left!", delay=0.2)
```

#### 9. Rotate Loading
```python
from smooth_text_animation import rotate_text
rotate_text("Processing", delay=0.2, cycles=10)
```

#### 10. Combined Animation
```python
from smooth_text_animation import combined_animation_simultaneous
combined_animation_simultaneous("Fade in and out!", delay=0.1, pause=0.5)
```

---

### New in v0.1.2

#### 11. Glitch Text
```python
from smooth_text_animation import glitch_text
glitch_text("SYSTEM GLITCH", delay=0.05, intensity=5)
```
Digital glitch effect — random characters replace parts of the text before resolving to the original.

#### 12. Rainbow Text
```python
from smooth_text_animation import rainbow_text
rainbow_text("Colorful!", delay=0.1)
```
Cycles the text through red, yellow, green, cyan, blue, and magenta.

#### 13. Matrix Reveal
```python
from smooth_text_animation import matrix_reveal
matrix_reveal("Hello, Neo", delay=0.05)
```
Each character is revealed through a cascade of random symbols, Matrix-style.

#### 14. Typewriter Advanced
```python
from smooth_text_animation import typewriter_advanced
typewriter_advanced("Realistic typing...", delay=0.08, mistake_probability=0.15)
```
Realistic typing effect with occasional wrong characters that are immediately corrected.

#### 15. Bounce Text
```python
from smooth_text_animation import bounce_text
bounce_text("Boing!", delay=0.1, bounces=3)
```
Text bounces up and down using vertical spacing.

#### 16. Scramble Solve
```python
from smooth_text_animation import scramble_solve
scramble_solve("Decoded", delay=0.05, iterations=20)
```
Starts as scrambled characters that gradually resolve to the correct message.

#### 17. Slide In
```python
from smooth_text_animation import slide_in
slide_in("→ Slide from left", delay=0.05, direction="left")
slide_in("Slide from right ←", delay=0.05, direction="right")
```
Text slides in from the left or right edge. Raises `ValueError` for invalid direction.

#### 18. Pulse Text
```python
from smooth_text_animation import pulse_text
pulse_text("Pulsing...", delay=0.2, pulses=5)
```
Cycles dim → normal → bold, creating a breathing/pulsing effect.

#### 19. Reveal Mask
```python
from smooth_text_animation import reveal_mask
reveal_mask("Revealed!", delay=0.1, mask_char="█")
```
Text is hidden behind a block mask that sweeps left to right to reveal the content.

#### 20. Zigzag Text
```python
from smooth_text_animation import zigzag_text
zigzag_text("ZigZag!", delay=0.08)
```
Characters appear in a zigzag pattern — even-indexed positions first, then odd.

#### 21. Expanding Center
```python
from smooth_text_animation import expanding_center
expanding_center("Expand!", delay=0.1)
```
Text grows outward from the center character.

#### 22. Neon Flicker
```python
from smooth_text_animation import neon_flicker
neon_flicker("NEON SIGN", delay=0.1, flickers=8)
```
Simulates a neon sign flickering before settling to a steady glow.

---

## Parameters 🎛️

Common parameters across most functions:

| Parameter | Type | Description |
|-----------|------|-------------|
| `text` | `str` | The text to animate |
| `delay` | `float` | Delay between steps in seconds (clamped to `>= 0`) |
| `repeat` / `pulses` / `bounces` | `int` | Repetition count for cyclic effects |

Negative `delay` values are silently clamped to `0`.

## Examples 💡

### Progress Indicator
```python
from smooth_text_animation import wave_text
for i in range(1, 6):
    wave_text(f"Processing step {i}/5", delay=0.2, repeat=2)
```

### Alert System
```python
from smooth_text_animation import blinking_text, neon_flicker
blinking_text("⚠️ System Alert!", repeat=3, delay=0.5)
neon_flicker("CRITICAL", delay=0.08, flickers=10)
```

### Welcome Screen
```python
from smooth_text_animation import matrix_reveal, slide_in, fade_in_text

matrix_reveal("=== SYSTEM BOOT ===", delay=0.04)
slide_in("Welcome, Agent.", delay=0.05, direction="left")
fade_in_text("Loading your dashboard...", delay=0.3)
```

## Requirements 📋

- Python 3.7+
- No external dependencies

## Changelog 📝

### v0.1.2
- Added 12 new animation effects (glitch, rainbow, matrix_reveal, typewriter_advanced, bounce, scramble_solve, slide_in, pulse, reveal_mask, zigzag, expanding_center, neon_flicker)
- `validate_delay` applied to all functions — negative delays clamped to 0
- `slide_in` raises `ValueError` for invalid direction
- `typewriter_advanced` jitter clamped to prevent negative sleep
- `colorize_text` from utils now used in fade_in and rainbow effects

### v0.1.1
- Internal code improvements and function updates

### v0.1.0
- Initial release with 10 animation effects

## License 📄

MIT License — feel free to use in your projects!

## Contributing 🤝

Contributions are welcome! Please feel free to submit a Pull Request.

## Author ✍️

traitimtrongvag — tbinh831@gmail.com

## Links 🔗

- [GitHub Repository](https://github.com/traitimtrongvag/smooth-text-animation)
- [PyPI Package](https://pypi.org/project/smooth-text-animation/)
- [Report Issues](https://github.com/traitimtrongvag/smooth-text-animation/issues)

---

Made with ❤️ for the Python community
