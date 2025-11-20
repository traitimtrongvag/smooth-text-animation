# smooth-text-animation/tests/test_animations.py
"""
Unit tests for smooth_text_animation package
"""

import pytest
import sys
from io import StringIO
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
)


class TestAnimations:
    """Test suite for animation functions"""
    
    def test_animated_line(self, capsys):
        """Test animated_line function"""
        text = "Hello"
        animated_line(text, delay=0.01)
        captured = capsys.readouterr()
        assert text in captured.out
    
    def test_animated_line_dual(self, capsys):
        """Test animated_line_dual function"""
        text = "Test Text"
        animated_line_dual(text, delay=0.01)
        captured = capsys.readouterr()
        # Kiểm tra text xuất hiện trong output
        assert len(captured.out) > 0
    
    def test_fade_in_text(self, capsys):
        """Test fade_in_text function"""
        text = "Fade Test"
        fade_in_text(text, delay=0.01)
        captured = capsys.readouterr()
        assert text in captured.out
    
    def test_marquee_text(self, capsys):
        """Test marquee_text function"""
        text = "Marquee"
        marquee_text(text, width=20, delay=0.01)
        captured = capsys.readouterr()
        assert len(captured.out) > 0
    
    def test_wave_text(self, capsys):
        """Test wave_text function"""
        text = "Loading"
        wave_text(text, delay=0.01, repeat=1)
        captured = capsys.readouterr()
        assert len(captured.out) > 0
    
    def test_blinking_text(self, capsys):
        """Test blinking_text function"""
        text = "Blink"
        blinking_text(text, repeat=2, delay=0.01)
        captured = capsys.readouterr()
        assert text in captured.out
    
    def test_random_fill(self, capsys):
        """Test random_fill function"""
        text = "Random"
        random_fill(text, delay=0.01)
        captured = capsys.readouterr()
        assert len(captured.out) > 0
    
    def test_reverse_text(self, capsys):
        """Test reverse_text function"""
        text = "Reverse"
        reverse_text(text, delay=0.01)
        captured = capsys.readouterr()
        assert len(captured.out) > 0
    
    def test_rotate_text(self, capsys):
        """Test rotate_text function"""
        text = "Rotate"
        rotate_text(text, delay=0.01, cycles=2)
        captured = capsys.readouterr()
        assert len(captured.out) > 0


class TestParameters:
    """Test parameter validation"""
    
    def test_delay_parameter(self):
        """Test that delay parameter works"""
        # Should not raise any exceptions
        animated_line("Test", delay=0.01)
        animated_line("Test", delay=0.5)
    
    def test_empty_string(self, capsys):
        """Test handling of empty string"""
        animated_line("", delay=0.01)
        captured = capsys.readouterr()
        # Should complete without error


class TestIntegration:
    """Integration tests"""
    
    def test_multiple_animations(self, capsys):
        """Test running multiple animations"""
        animated_line("First", delay=0.01)
        wave_text("Second", delay=0.01, repeat=1)
        blinking_text("Third", repeat=1, delay=0.01)
        captured = capsys.readouterr()
        assert len(captured.out) > 0


if __name__ == "__main__":
    pytest.main([__file__, "-v"])