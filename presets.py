"""
Prompt Presets for Ghost Notes Clipboard Transformations.
"""

from typing import Dict

PROMPT_PRESETS: Dict[str, str] = {
    "clean_notes": (
        "You are an ambient text formatter. Clean typos, grammar, and format "
        "the input into clean, structured Markdown bullet points. Return ONLY "
        "the formatted text with no conversational intro:\n{text}"
    ),
    "code_fix": (
        "You are an expert engineer. Review the following code snippet. Fix syntax "
        "errors, clean indentation, add concise docstrings, and format it cleanly. "
        "Return ONLY the clean executable code block:\n{text}"
    ),
    "tldr": (
        "You are an executive assistant. Distill the following content into "
        "exactly two concise, high-impact bullet points. Return ONLY bullets:\n{text}"
    ),
}

def get_formatted_prompt(mode: str, text: str) -> str:
    """Retrieves and formats the prompt template for the given mode."""
    if mode not in PROMPT_PRESETS:
        raise ValueError(f"Unknown prompt mode: {mode}. Available: {list(PROMPT_PRESETS.keys())}")
    return PROMPT_PRESETS[mode].format(text=text)
