"""
Unit tests for Ghost Notes daemon, preset formatting, and NPU engine fallback.
"""

import unittest
import sys
import os

# Ensure project root is in sys.path
sys.path.insert(0, os.path.abspath(os.path.dirname(os.path.dirname(__file__))))

from unittest.mock import MagicMock, patch
from ghost_notes.presets import PROMPT_PRESETS, get_formatted_prompt
from ghost_notes.npu_engine import NPUEngine
from ghost_notes.daemon import GhostNotesDaemon


class TestGhostNotes(unittest.TestCase):

    def test_presets_exist(self):
        """Verify all three required prompt modes are defined."""
        self.assertIn("clean_notes", PROMPT_PRESETS)
        self.assertIn("code_fix", PROMPT_PRESETS)
        self.assertIn("tldr", PROMPT_PRESETS)

    def test_get_formatted_prompt(self):
        """Test prompt formatting substitution."""
        input_text = "sample messy text"
        prompt = get_formatted_prompt("clean_notes", input_text)
        self.assertIn(input_text, prompt)
        self.assertIn("ambient text formatter", prompt)

    def test_invalid_mode_raises(self):
        """Test invalid mode throws ValueError."""
        with self.assertRaises(ValueError):
            get_formatted_prompt("invalid_mode", "text")

    def test_npu_engine_fallback(self):
        """Test NPU Engine returns response in simulation mode."""
        engine = NPUEngine()
        response = engine.run_inference("Test prompt for NPU")
        self.assertIn("Processed Privately on Snapdragon", response)

    @patch("ghost_notes.daemon.pyperclip")
    def test_process_clipboard_clean_notes(self, mock_pyperclip):
        """Test processing clipboard for clean_notes mode."""
        mock_pyperclip.paste.return_value = "Meeting notes raw"
        daemon = GhostNotesDaemon()
        daemon.process_clipboard("clean_notes")
        mock_pyperclip.copy.assert_called_once()
        copied_val = mock_pyperclip.copy.call_args[0][0]
        self.assertIn("Processed Privately on Snapdragon", copied_val)

    @patch("ghost_notes.daemon.pyperclip")
    def test_empty_clipboard_skipped(self, mock_pyperclip):
        """Test empty clipboard is handled without crashing or copying."""
        mock_pyperclip.paste.return_value = "   "
        daemon = GhostNotesDaemon()
        daemon.process_clipboard("clean_notes")
        mock_pyperclip.copy.assert_not_called()


if __name__ == "__main__":
    unittest.main()
