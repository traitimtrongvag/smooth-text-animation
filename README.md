# Smooth Text Animation 🎨

Beautiful and smooth text animations for terminal output in Python.

## Features ✨

- **10+ animation effects** for terminal text
- **Easy to use** - just import and call
- **Lightweight** - no external dependencies
- **Customizable** - adjust speed and behavior
- **Cross-platform** - works on Windows, macOS, and Linux

## Installation 📦

```bash
pip install smooth-text-animation
```

## Quick Start 🚀

```python
from smooth_text_animation import animated_line, wave_text, blinking_text

# Typing effect
animated_line("Hello, World!", delay=0.1)

# Loading effect
wave_text("Loading", delay=0.3)

# Blinking warning
blinking_text("Warning!", repeat=5, delay=0.5)
```

## Available Animations 🎭

### 1. Animated Line (Typing Effect)
```python
from smooth_text_animation import animated_line
animated_line("This text appears character by character!", delay=0.05)
```

### 2. Dual Side Animation
```python
from smooth_text_animation import animated_line_dual
animated_line_dual("Text appears from both sides!", delay=0.1)
```

### 3. Fade In Effect
```python
from smooth_text_animation import fade_in_text
fade_in_text("This text fades in gradually!", delay=0.2)
```

### 4. Marquee Text (Scrolling)
```python
from smooth_text_animation import marquee_text
marquee_text("This text scrolls across the screen!", width=30, delay=0.1)
```

### 5. Wave Loading
```python
from smooth_text_animation import wave_text
wave_text("Loading", delay=0.3, repeat=3)
```

### 6. Blinking Text
```python
from smooth_text_animation import blinking_text
blinking_text("ALERT!", repeat=5, delay=0.3)
```

### 7. Random Fill
```python
from smooth_text_animation import random_fill
random_fill("Characters appear randomly!", delay=0.1)
```

### 8. Reverse Text
```python
from smooth_text_animation import reverse_text
reverse_text("Text appears from right to left!", delay=0.2)
```

### 9. Rotate Loading
```python
from smooth_text_animation import rotate_text
rotate_text("Processing", delay=0.2, cycles=10)
```

### 10. Combined Animation
```python
from smooth_text_animation import combined_animation_simultaneous
combined_animation_simultaneous("Fade in and out!", delay=0.1)
```

## Parameters 🎛️

Most functions accept these common parameters:

- `text` (str): The text to animate
- `delay` (float): Delay between animation steps in seconds
- `repeat` (int): Number of times to repeat the animation (for some effects)

## Examples 💡

### Progress Indicator
```python
from smooth_text_animation import wave_text
import time

for i in range(1, 6):
    wave_text(f"Processing step {i}/5", delay=0.2, repeat=2)
    time.sleep(1)
```

### Alert System
```python
from smooth_text_animation import blinking_text

blinking_text("⚠️ System Alert!", repeat=3, delay=0.5)
```

### Welcome Message
```python
from smooth_text_animation import animated_line_dual, fade_in_text

animated_line_dual("=== Welcome to My App ===", delay=0.05)
fade_in_text("Loading your dashboard...", delay=0.3)
```

## Requirements 📋

- Python 3.7+
- No external dependencies!

## License 📄

MIT License - feel free to use in your projects!

## Contributing 🤝

Contributions are welcome! Please feel free to submit a Pull Request.

## Author ✍️

traitimtrongvag - tbinh831@gmail.com

## Links 🔗

- [GitHub Repository](https://github.com/traitimtrongvag/smooth-text-animation)
- [PyPI Package](https://pypi.org/project/smooth-text-animation/)
- [Report Issues](https://github.com/traitimtrongvag/smooth-text-animation/issues)

---

Made with ❤️ for the Python community# smooth-text-animation
