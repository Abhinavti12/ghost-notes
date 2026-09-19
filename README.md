# GHOST NOTES: Ambient Intelligent Clipboard

> **NPU-Accelerated Smart Transformer Daemon for Snapdragon®-Powered HP PCs**  
> *Developed for the Snapdragon® AI Lab Build & Present Challenge*

---

## Executive Summary

Everyday PC productivity suffers from cognitive fragmentation: professionals, students, and engineers frequently copy messy notes, confusing terminal traces, unformatted code, and disjointed research fragments into external browser-based AI chats. This context switching breaks momentum and exposes private data to cloud servers.

**Ghost Notes** is an ambient, zero-latency, privacy-preserving clipboard transformer daemon. Running silently in the background, Ghost Notes monitors global hotkeys (`Ctrl+Alt+1/2/3`), intercepts clipboard content, executes deterministic transformations using a quantized Small Language Model (SLM) on the **Qualcomm® Hexagon™ NPU**, and re-injects formatted text back into system clipboard in sub-second time.

---

## Quick Features & Hotkeys

| Hotkey | Operational Mode | Description |
| :--- | :--- | :--- |
| `Ctrl + Alt + 1` | **Clean Notes** | Cleans typos, fixes grammar, and formats input into clean Markdown bullet points. |
| `Ctrl + Alt + 2` | **Code Formatter** | Reviews code snippets, fixes syntax/indentation, adds docstrings, and outputs executable code blocks. |
| `Esc` | **Exit Daemon** | Safely terminates background hotkey listeners. |

---

## Repository Structure

```
ghost_notes/
├── README.md                   # Primary project overview & usage guide
├── REQUIREMENTS.md             # Functional & Non-Functional requirements (FR-1..4, NFR-1..3)
├── ARCHITECTURE.md             # System design blueprint & data flow diagrams
├── PROPOSAL.md                 # Snapdragon AI Lab proposal & submission strategy document
├── requirements.txt            # Dependencies (pyperclip, keyboard, onnxruntime)
├── pyproject.toml              # Modern Python project configuration
├── main.py                     # CLI launcher script
├── ghost_notes/                # Core Python package
│   ├── __init__.py             # Package init & version metadata
│   ├── daemon.py               # Main daemon orchestrator & hotkey listener
│   ├── presets.py              # Transformation prompt presets
│   └── npu_engine.py           # ONNX QNNExecutionProvider / Hexagon NPU bridge
└── tests/                      # Unit test suite
    ├── __init__.py
    └── test_daemon.py          # Unit tests for daemon and prompt formatting
```

---

## Quickstart Guide

### Prerequisites
- **OS:** Windows 11 on ARM (Snapdragon® X Elite / Plus) or Windows 10/11 x64 (Simulation Mode).
- **Python:** Python 3.9+
- **Privileges:** Administrator terminal required for global keyboard hook registration on Windows.

### 1. Installation

Clone the repository and install dependencies:

```bash
git clone https://github.com/your-username/ghost_notes.git
cd ghost_notes
pip install -r requirements.txt
```

### 2. Running the Daemon

Launch the daemon service (run terminal as Administrator for global hotkey support):

```bash
python main.py
```

Console Output:
```
=======================================================
 Ghost Notes Daemon Active (Snapdragon AI Lab)
 Hotkeys:
   [Ctrl + Alt + 1] -> Clean & Format Notes
   [Ctrl + Alt + 2] -> Code Formatter & Debugger
   [Ctrl + Alt + 3] -> Executive TL;DR Summary
   [Esc]            -> Terminate Daemon
=======================================================
```

---

## Qualcomm® AI Hub Model Compilation (Optional / NPU Deployment)

To compile and optimize models for the Qualcomm Hexagon NPU:

```bash
# Install Qualcomm AI Hub CLI
pip install qai-hub

# Authenticate with Qualcomm AI Hub
qai-hub configure --api_token <YOUR_API_TOKEN>

# Export Llama 3.2 1B Instruct targeting Snapdragon X Elite NPU
qai-hub submit-compile \
  --model llama_v3_2_1b_instruct \
  --device "Snapdragon X Elite CRD" \
  --output_dir models/llama-3.2-1b-qnn
```

When deployed on Snapdragon HP PCs, ONNX Runtime automatically binds to `QnnHtp.dll` via `QNNExecutionProvider`.

---

## Running Unit Tests

Run the test suite to verify prompt preset formatting and NPU fallback execution:

```bash
python tests/test_daemon.py
```

---

## Attribution

Developed for the **Snapdragon® AI Lab Build & Present Challenge**.
