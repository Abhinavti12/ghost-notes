# GHOST NOTES: Ambient Intelligent Clipboard

**NPU-Accelerated Smart Transformer Daemon for Snapdragon®-Powered HP PCs**  
*Submitted for the Snapdragon® AI Lab Build & Present Challenge*

---

## 1. Executive Summary & Challenge Alignment

The **Snapdragon® AI Lab Build & Present Challenge** calls for innovative on-device AI applications tailored specifically to Snapdragon-powered HP PCs. Everyday PC productivity suffers from cognitive fragmentation: professionals, students, and engineers frequently copy messy notes, confusing terminal traces, unformatted code, and disjointed research fragments into external browser-based AI chats. This breaks workflow momentum and exposes private data to cloud servers.

**Ghost Notes** is an ambient, zero-latency, privacy-preserving clipboard transformer daemon. Running silently in the background, Ghost Notes monitors configurable global hotkeys (`Ctrl+Alt+1/2/3`), intercepts clipboard content, executes deterministic transformations using a quantized Small Language Model (SLM) on the **Qualcomm® Hexagon™ NPU**, and re-injects the formatted text into the system clipboard in sub-second time.

### Evaluation Rubric Alignment

- **Technical Implementation:** Offloads quantized SLMs (`Llama-3.2-1B-Instruct` or `Phi-3.5`) directly to the Hexagon NPU via Qualcomm AI Hub and ONNX Runtime with `QNNExecutionProvider`.
- **Application Use Case & Innovation:** Completely removes friction by offering ambient, zero-UI AI acceleration directly in the user's workflow.
- **Deployment & Accessibility:** Lightweight daemon footprint (~150MB memory), minimal idle power draw (<0.5W), and instant out-of-the-box readiness.
- **Presentation & Documentation:** Clean modular architecture, clear demo narrative, and high visual contrast for screen recordings.

---

## 2. Implementation Plan & Milestones

| Phase | Deliverables | Technical Scope | Timeline |
| :--- | :--- | :--- | :--- |
| **Phase 1: Model Setup** | Pre-compiled ONNX model targeting Hexagon NPU | Authenticate via Qualcomm AI Hub CLI, pull `llama_v3_2_1b_instruct`, compile with INT4 quantization for Snapdragon compute. | Days 1 - 3 |
| **Phase 2: Core Daemon** | Python clipboard pipeline | Build prompt presets, clipboard capture/overwrite with `pyperclip`, and wire QNN execution provider in ONNX Runtime. | Days 4 - 6 |
| **Phase 3: Integration** | Background daemon & hotkeys | Bind global hotkeys (`keyboard`), implement debounce locks, and verify background persistence without CPU spikes. | Days 7 - 9 |
| **Phase 4: Submission** | Demo Video & Documentation | Record side-by-side demo showing instant transformations and Task Manager NPU utilization; write final submission report. | Days 10 - 12 |

---

## 3. Submission Strategy & Judging Optimization

- **Live Demo Strategy (2-Minute Video):** Showcase side-by-side execution with Windows Task Manager open. When the shortcut is triggered, highlight the spike in the Hexagon NPU while the CPU stays calm and idle (<5%). This visually proves true on-device acceleration.
- **Licensing:** Published under the open-source **MIT License**, including clear setup documentation on pulling models from Qualcomm AI Hub via `qai-hub pull`.
- **Extensibility:** Propose future multimodal support, such as parsing screenshot images on the clipboard via Qualcomm AI Hub vision models.
