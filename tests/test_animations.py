# smooth-text-animation/tests/test_animations.py
"""
Unit tests for smooth_text_animation package
"""

import pytest
from smooth_text_animation import (
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
    glitch_text,
    rainbow_text,
    matrix_reveal,
    typewriter_advanced,
    bounce_text,
    scramble_solve,
    slide_in,
    pulse_text,
    reveal_mask,
    zigzag_text,
    expanding_center,
    neon_flicker,
)


# ---------------------------------------------------------------------------
# Original animations
# ---------------------------------------------------------------------------

class TestOriginalAnimations:
    """Test suite for original animation functions."""

    def test_animated_line(self, capsys):
        animated_line("Hello", delay=0)
        assert "Hello" in capsys.readouterr().out

    def test_animated_line_dual(self, capsys):
        animated_line_dual("Test Text", delay=0)
        assert len(capsys.readouterr().out) > 0

    def test_fade_in_text(self, capsys):
        fade_in_text("Fade Test", delay=0)
        assert "Fade Test" in capsys.readouterr().out

    def test_marquee_text(self, capsys):
        marquee_text("Marquee", width=20, delay=0)
        assert len(capsys.readouterr().out) > 0

    def test_wave_text(self, capsys):
        wave_text("Loading", delay=0, repeat=1)
        assert len(capsys.readouterr().out) > 0

    def test_blinking_text(self, capsys):
        blinking_text("Blink", repeat=2, delay=0)
        assert "Blink" in capsys.readouterr().out

    def test_random_fill(self, capsys):
        random_fill("Random", delay=0)
        assert len(capsys.readouterr().out) > 0

    def test_reverse_text(self, capsys):
        reverse_text("Reverse", delay=0)
        assert len(capsys.readouterr().out) > 0

    def test_rotate_text(self, capsys):
        rotate_text("Rotate", delay=0, cycles=2)
        assert len(capsys.readouterr().out) > 0

    def test_combined_animation_simultaneous(self, capsys):
        combined_animation_simultaneous("Test", delay=0, pause=0)
        assert len(capsys.readouterr().out) >= 0  # completes without error


# ---------------------------------------------------------------------------
# New animations (v0.1.2)
# ---------------------------------------------------------------------------

class TestNewAnimations:
    """Test suite for new animation functions added in v0.1.2."""

    def test_glitch_text(self, capsys):
        glitch_text("Glitch", delay=0, intensity=3)
        out = capsys.readouterr().out
        assert "Glitch" in out

    def test_rainbow_text(self, capsys):
        rainbow_text("Rainbow", delay=0)
        out = capsys.readouterr().out
        assert len(out) > 0

    def test_matrix_reveal(self, capsys):
        matrix_reveal("Matrix", delay=0)
        out = capsys.readouterr().out
        assert "Matrix" in out

    def test_typewriter_advanced(self, capsys):
        typewriter_advanced("Type", delay=0, mistake_probability=0.0)
        out = capsys.readouterr().out
        assert "Type" in out

    def test_typewriter_advanced_with_mistakes(self, capsys):
        # High probability to exercise mistake branch without crashing
        typewriter_advanced("Hello", delay=0, mistake_probability=0.9)
        out = capsys.readouterr().out
        assert len(out) > 0

    def test_bounce_text(self, capsys):
        bounce_text("Bounce", delay=0, bounces=1)
        assert len(capsys.readouterr().out) > 0

    def test_scramble_solve(self, capsys):
        scramble_solve("Scramble", delay=0, iterations=5)
        out = capsys.readouterr().out
        assert "Scramble" in out

    def test_slide_in_left(self, capsys):
        slide_in("Slide", delay=0, direction="left")
        out = capsys.readouterr().out
        assert "Slide" in out

    def test_slide_in_right(self, capsys):
        slide_in("Slide", delay=0, direction="right")
        out = capsys.readouterr().out
        assert "Slide" in out

    def test_slide_in_invalid_direction(self):
        with pytest.raises(ValueError, match="direction"):
            slide_in("Test", direction="up")

    def test_pulse_text(self, capsys):
        pulse_text("Pulse", delay=0, pulses=2)
        out = capsys.readouterr().out
        assert "Pulse" in out

    def test_reveal_mask(self, capsys):
        reveal_mask("Reveal", delay=0)
        out = capsys.readouterr().out
        assert "Reveal" in out

    def test_reveal_mask_custom_char(self, capsys):
        reveal_mask("Test", delay=0, mask_char="*")
        out = capsys.readouterr().out
        assert len(out) > 0

    def test_zigzag_text(self, capsys):
        zigzag_text("Zigzag", delay=0)
        out = capsys.readouterr().out
        assert "Zigzag" in out

    def test_expanding_center(self, capsys):
        expanding_center("Center", delay=0)
        out = capsys.readouterr().out
        assert "Center" in out

    def test_neon_flicker(self, capsys):
        neon_flicker("Neon", delay=0, flickers=5)
        out = capsys.readouterr().out
        assert "Neon" in out


# ---------------------------------------------------------------------------
# Parameter validation
# ---------------------------------------------------------------------------

class TestParameterValidation:
    """Test parameter edge cases and validation."""

    def test_negative_delay_clamped(self, capsys):
        # validate_delay should clamp negative to 0 — no exception
        animated_line("Test", delay=-1)
        assert len(capsys.readouterr().out) > 0

    def test_empty_string(self, capsys):
        animated_line("", delay=0)
        capsys.readouterr()  # completes without error

    def test_empty_string_new_functions(self, capsys):
        for fn in (glitch_text, rainbow_text, matrix_reveal, zigzag_text,
                   expanding_center, reveal_mask, pulse_text, neon_flicker):
            fn("", delay=0)
        capsys.readouterr()

    def test_mistake_probability_clamped(self, capsys):
        # Values outside [0, 1] should be clamped, not raise
        typewriter_advanced("Hi", delay=0, mistake_probability=5.0)
        typewriter_advanced("Hi", delay=0, mistake_probability=-1.0)
        capsys.readouterr()

    def test_single_char_text(self, capsys):
        for fn in (animated_line, reverse_text, random_fill, glitch_text,
                   zigzag_text, expanding_center, reveal_mask):
            fn("X", delay=0)
        capsys.readouterr()


# ---------------------------------------------------------------------------
# Integration
# ---------------------------------------------------------------------------

class TestIntegration:
    """Integration tests: multiple animations in sequence."""

    def test_all_new_animations_in_sequence(self, capsys):
        glitch_text("A", delay=0, intensity=1)
        rainbow_text("B", delay=0)
        matrix_reveal("C", delay=0)
        typewriter_advanced("D", delay=0, mistake_probability=0.0)
        bounce_text("E", delay=0, bounces=1)
        scramble_solve("F", delay=0, iterations=3)
        slide_in("G", delay=0, direction="left")
        pulse_text("H", delay=0, pulses=1)
        reveal_mask("I", delay=0)
        zigzag_text("J", delay=0)
        expanding_center("K", delay=0)
        neon_flicker("L", delay=0, flickers=2)
        assert len(capsys.readouterr().out) > 0


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
