# Ghost Notes: Requirements Analysis

**Project Name:** Ghost Notes (Ambient Intelligent Clipboard)  
**Target Hardware:** HP OmniBook (Snapdragon® X Series)  
**Platform:** Qualcomm® AI Hub & ONNX Runtime (QNN Execution Provider)  
**Challenge:** Snapdragon® AI Lab Build & Present Challenge  

---

## 1. Functional Requirements (FR)

| Requirement ID | Title | Description | Target Specification |
| :--- | :--- | :--- | :--- |
| **FR-1** | **Global Hotkey Interception** | Non-blocking system-wide background listener for keyboard shortcuts. | - `Ctrl+Alt+1`: Clean Notes & Format Markdown<br>- `Ctrl+Alt+2`: Code Formatter & Debugger<br>- `Ctrl+Alt+3`: Executive TL;DR Summary |
| **FR-2** | **Clipboard Buffer Ingestion** | Safe programmatic ingestion of text payloads from the OS system clipboard. | - Ingest string buffers up to 300+ tokens<br>- Zero truncation or encoding corruption<br>- Handle empty clipboard gracefully |
| **FR-3** | **Contextual Transformation Engine** | Zero-shot prompt template injection enforcing direct structured output. | - Enforce clean Markdown output<br>- Eliminate AI conversational intro/outro boilerplate<br>- Support custom operational modes |
| **FR-4** | **Native Clipboard Re-injection** | Direct programmatic overwrite of the active Windows system clipboard buffer. | - Immediate readiness for `Ctrl+V` pasting in target application (VS Code, Notion, MS Word, Terminal, etc.) |

---

## 2. Non-Functional Requirements (NFR)

| Requirement ID | Title | Description | Target Specification |
| :--- | :--- | :--- | :--- |
| **NFR-1** | **Sub-Second Latency** | Ultra-responsive inference execution on Hexagon NPU hardware. | - First-token latency: **<250ms**<br>- Total execution: **<1.2s** for up to 300 input tokens |
| **NFR-2** | **Energy Efficiency & Thermals** | Low-power, whisper-quiet operation on Snapdragon HP PCs. | - Inference power capped at **~3.5W** on Qualcomm Hexagon NPU<br>- Zero fan spin on HP OmniBook PCs<br>- Daemon idle power draw: **<0.5W** |
| **NFR-3** | **100% On-Device Privacy** | Air-gapped execution ensuring confidential data protection. | - 0% cloud dependence<br>- Zero external API calls or network transmission |
| **NFR-4** | **Memory & Resource Footprint** | Lightweight background service persistence. | - Memory footprint: **~150MB** RAM<br>- Background CPU utilization: **<5%** |

---

## 3. Challenge Rubric Alignment Summary

- **Technical Implementation:** Offloads INT4 quantized Small Language Models (Llama-3.2-1B / Phi-3.5) directly to the Hexagon NPU via Qualcomm AI Hub compiled models and ONNX Runtime `QNNExecutionProvider`.
- **Application Use Case & Innovation:** Ambient, zero-UI clipboard transformer eliminating friction and context switching.
- **Deployment & Accessibility:** Lightweight daemon running natively on Windows on ARM (Snapdragon X Elite / Plus).
- **Presentation & Documentation:** Clean, modular repository layout with architecture blueprints, reproducible setup steps, and video demo guidelines.
