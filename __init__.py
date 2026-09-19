"""
Ghost Notes: Ambient Intelligent Clipboard
NPU-Accelerated Smart Transformer Daemon for Snapdragon®-Powered HP PCs.
"""

__version__ = "0.1.0"
__author__ = "Snapdragon AI Lab Team"

from .daemon import GhostNotesDaemon
from .presets import PROMPT_PRESETS
from .npu_engine import NPUEngine

__all__ = ["GhostNotesDaemon", "PROMPT_PRESETS", "NPUEngine"]
