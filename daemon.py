"""
Core Ghost Notes Daemon - Clipboard Interceptor & Global Hotkey Listener.
"""

import time
import threading
import sys
from typing import Optional

try:
    import pyperclip  # type: ignore
except ImportError:
    pyperclip = None

try:
    import keyboard  # type: ignore
except ImportError:
    keyboard = None

from .presets import PROMPT_PRESETS, get_formatted_prompt
from .npu_engine import NPUEngine


class GhostNotesDaemon:
    """
    Ambient Intelligent Clipboard Daemon for Snapdragon®-Powered PCs.
    Monitors global hotkeys, intercepts system clipboard content, transforms
    text payloads on Hexagon NPU, and updates OS clipboard buffer.
    """

    def __init__(self, model_path: str = "models/llama-3.2-1b-qnn"):
        self.model_path = model_path
        self.is_processing = False
        self.lock = threading.Lock()
        print("[Ghost Notes] Initializing Ghost Notes Daemon...")
        self.npu_engine = NPUEngine(model_path=self.model_path)

    def run_npu_inference(self, prompt: str) -> str:
        """Bridge method invoking NPU transformation pipeline."""
        return self.npu_engine.run_inference(prompt)

    def process_clipboard(self, mode: str) -> None:
        """
        Thread-safe handler for hotkey triggers. Reads clipboard, dispatches to NPU,
        and re-injects formatted result.
        """
        if self.is_processing:
            print("[Ghost Notes] Busy processing previous payload. Skipping.")
            return

        with self.lock:
            self.is_processing = True
            try:
                if pyperclip is None:
                    print("[Ghost Notes] Error: 'pyperclip' library is not available.")
                    return

                raw_text = pyperclip.paste()
                if not raw_text or len(raw_text.strip()) == 0:
                    print("[Ghost Notes] Clipboard is empty.")
                    return

                print(f"[Ghost Notes] Intercepted payload ({len(raw_text)} chars). Mode: {mode}")
                prompt = get_formatted_prompt(mode, raw_text)

                # Execute inference on Hexagon NPU
                transformed_text = self.run_npu_inference(prompt)

                # Re-write directly into system clipboard
                pyperclip.copy(transformed_text)
                print("[Ghost Notes] Clipboard updated successfully! Ready to paste.")

            except Exception as err:
                print(f"[Ghost Notes] Error during processing: {err}")
            finally:
                self.is_processing = False

    def start_listeners(self, block: bool = True) -> None:
        """
        Registers global OS hotkeys and blocks main thread waiting for triggers or termination signal.
        """
        banner = "=" * 55
        print(f"\n{banner}")
        print(" Ghost Notes Daemon Active (Snapdragon AI Lab)")
        print(" Hotkeys:")
        print("   [Ctrl + Alt + 1] -> Clean & Format Notes")
        print("   [Ctrl + Alt + 2] -> Code Formatter & Debugger")
        print("   [Ctrl + Alt + 3] -> Executive TL;DR Summary")
        print("   [Esc]            -> Terminate Daemon")
        print(f"{banner}\n")

        if keyboard is None:
            print("[Ghost Notes] Warning: 'keyboard' library unavailable. Hotkey registration skipped.")
            return

        try:
            keyboard.add_hotkey('ctrl+alt+1', lambda: self.process_clipboard("clean_notes"))
            keyboard.add_hotkey('ctrl+alt+2', lambda: self.process_clipboard("code_fix"))
            keyboard.add_hotkey('ctrl+alt+3', lambda: self.process_clipboard("tldr"))

            if block:
                keyboard.wait('esc')
                print("[Ghost Notes] Daemon stopped cleanly.")
        except Exception as e:
            print(f"[Ghost Notes] Hotkey listener notice: {e}")
            print("Note: Global hotkeys require elevated/Administrator privileges on Windows.")
