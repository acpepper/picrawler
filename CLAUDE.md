# PiCrawler Documentation Repository

## Project Identity

| Field | Value |
|---|---|
| **Product** | SunFounder PiCrawler — Raspberry Pi quadruped robot kit |
| **Repository** | `git@github.com:sunfounder/picrawler.git` |
| **Documentation** | Sphinx + ReadTheDocs (`sphinx_rtd_theme`) |
| **Published at** | `https://docs.sunfounder.com/projects/pi-crawler/<lang>/latest/` |
| **Company** | SunFounder (service@sunfounder.com) |
| **License** | GPL v2 |

This repository contains **only documentation** for the PiCrawler robot kit. The Python library code (`picrawler`, `robot_hat`, `vilib`) lives in separate repositories. This repo builds a multi-language Sphinx documentation site via ReadTheDocs.

---

## Branch Strategy: Multi-Language Documentation

The `main` branch holds the kit code/examples. **All documentation lives on language-specific branches:**

| Branch | Language | Role |
|---|---|---|
| `docs-v3-en` | English | **SOURCE OF TRUTH** — all new content originates here |
| `docs-v3-de` | German | Translation target |
| `docs-v3-cn` | Chinese (zh-cn) | Translation target |
| `docs-v3-fr` | French | Translation target |
| `docs-v3-es` | Spanish | Translation target |
| `docs-v3-it` | Italian | Translation target |
| `docs-v3-ja` | Japanese | Translation target |
| `docs-v2-en` | English (v2) | Legacy, frozen |

### Cardinal Rule

> **`docs-v3-en` is the single source of truth.** All new content, structural changes, and configuration updates start on `docs-v3-en` and propagate to the translation branches. Never add new sections or restructure toctrees directly on a translation branch — do it on `docs-v3-en` first, then mirror to others.

### Translation Branch Sync Flow

```
docs-v3-en (write new content)
    │
    ├─→ docs-v3-de  (translate, keep German text)
    ├─→ docs-v3-cn  (translate, keep Chinese text)
    ├─→ docs-v3-fr  (translate, keep French text)
    ├─→ docs-v3-es  (translate, keep Spanish text)
    ├─→ docs-v3-it  (translate, keep Italian text)
    └─→ docs-v3-ja  (translate, keep Japanese text)
```

### What Gets Synced

When propagating from `docs-v3-en` to a translation branch:

1. **Copy as-is**: All image files (`img/`, `ai_interaction/img/`, `img/openclaw/`)
2. **Translate**: All `.rst` content files — descriptive text must be in the target language
3. **Merge carefully**: `index.rst` and `conf.py` — preserve translated UI text while adding new entries
4. **Code blocks**: Keep Python/bash code and file paths as-is (they are language-agnostic)
5. **RST directives**: Keep `.. image::`, `.. code-block::`, `.. note::`, `.. warning::`, `.. important::` structural markup intact
6. **Reference labels**: Keep `.. _ref_label:` and `:ref:`target`` references intact (they are cross-document identifiers, not user-visible text)

### Language-Specific Configuration

Each translation branch's `conf.py` differs in:
- Link text in `rst_epilog` substitutions (e.g., German "OpenAI Plattform" vs English "OpenAI Platform")
- The `language` variable (set to the appropriate locale code when translations exist)

The `index.rst` in each branch has:
- Translated header/intro text
- Translated section descriptions
- Same toctree structure as `docs-v3-en`
- May preserve legacy content unique to that language (e.g., `openai.rst` in `docs-v3-de`)

---

## Repository Layout

```
picrawler/
├── .readthedocs.yaml          # RTD build config (Sphinx 7.3.7, Python 3.11, Ubuntu 22.04)
├── .gitignore                 # Ignores: .vscode, build/, secret files, .claude/
├── .gitmodules                # Submodule: docs/source/_shared → sf-shared.git
├── LICENSE                    # GPL v2
├── README.md                  # Kit overview (buy link, updates, troubleshooting)
├── show                       # License/warranty display script
├── CLAUDE.md                  # This file — AI assistant guidance
└── docs/
    ├── requirements.txt       # sphinx==7.3.7, sphinx_rtd_theme==3.0.1, sphinx_copybutton
    ├── Makefile / make.bat    # Sphinx build (SOURCEDIR=source, BUILDDIR=build)
    └── source/
        ├── conf.py            # Sphinx config: extensions, theme, JS/CSS, rst_epilog links
        ├── index.rst          # Root toctree — 3 chapters + appendix + hardware + FAQ
        ├── openclaw.rst       # OpenClaw AI agent control tutorial (EN only for now)
        ├── assemble_video.rst # Assembly video links
        ├── servo_zeroing.rst  # Servo calibration guide
        ├── appendix.rst       # Appendix
        ├── faq.rst            # Frequently asked questions
        ├── list_and_assembly.rst  # Parts list + assembly
        ├── _shared/           # Git submodule: shared SunFounder doc assets (sf-shared)
        ├── _templates/        # Sphinx HTML templates (layout.html)
        ├── img/               # Top-level images (picrawler.jpg, robot_hat_pic.png, etc.)
        │   ├── openclaw/      # OpenClaw installation screenshots (20 images)
        │   └── apt_*.png      # GPT-4O / Assistant API screenshots
        ├── python/            # Python programming chapter
        │   ├── play_with_python.rst    # Chapter toctree + intro
        │   ├── install_all_modules.rst # Module installation guide
        │   ├── python_move.rst         # Lesson: basic movement
        │   ├── python_*.rst            # Lessons: twist, avoid, vision, sound, etc.
        │   ├── python_action_gallery.rst # Lesson: pre-programmed action demo
        │   ├── calibrate.rst / py_servo_adjust.rst  # Calibration guides
        │   └── img/                    # Python chapter screenshots
        ├── ezblock/           # Ezblock (graphical programming) chapter
        │   ├── play_with_ezblock.rst   # Chapter toctree + intro
        │   ├── quick_guide_on_ezblock.rst # Getting started
        │   ├── ezblock_move.rst        # Lesson: movement
        │   ├── ezblock_*.rst           # Lessons: twist, avoid, vision, sound, etc.
        │   ├── calibrate.rst           # Ezblock calibration
        │   └── img/                    # Ezblock chapter screenshots
        ├── hardware/          # Hardware reference chapter
        │   ├── cpn_hardware.rst        # Chapter toctree
        │   ├── cpn_robot_hat.rst       # Robot HAT intro
        │   ├── cpn_battery.rst         # Battery guide
        │   ├── cpn_camera.rst          # Camera setup
        │   ├── cpn_ultrasonic.rst      # Ultrasonic sensor
        │   └── img/                    # Hardware photos
        └── ai_interaction/    # AI Interaction chapter (NEW — EN branch only as of 2025)
            ├── ai_interaction.rst      # Chapter toctree + intro
            ├── python_stt.rst          # Lesson: Speech-to-Text
            ├── python_tts.rst          # Lesson: Text-to-Speech (Piper/Espeak)
            ├── python_online_llms.rst  # Multi-provider LLM setup (OpenAI, Gemini, Qwen, DeepSeek, Grok, Doubao)
            ├── python_voice_gpt.rst    # Voice chat with GPT (wake word "Hey Buddy")
            ├── python_voice_doubao.rst # Voice chat with Doubao (wake word "旺财")
            ├── python_voice_ollama.rst # Local voice chat with Ollama (offline)
            └── img/                    # LLM setup screenshots (41 images across 6 providers)
```

---

## Documentation Conventions

### RST Reference Labels

Cross-document references use Sphinx `:ref:` roles. Each `.rst` file defines a unique label at the top (after the Facebook note). These labels **must remain consistent across all language branches** — they are the linking mechanism.

| Label | File | Content |
|---|---|---|
| `play_python` | `play_with_python.rst` | Python chapter entry point |
| `play_ezblock` | `play_with_ezblock.rst` | Ezblock chapter entry point |
| `play_ai` | `ai_interaction.rst` | AI chapter entry point |
| `install_all_modules` | `install_all_modules.rst` | Module installation prerequisite |
| `py_stt` | `python_stt.rst` | STT lesson |
| `py_tts` | `python_tts.rst` | TTS lesson |
| `py_online_llm` | `python_online_llms.rst` | Online LLM setup |
| `py_voice_active_gpt` | `python_voice_gpt.rst` | GPT voice chat |
| `py_voice_doubao` | `python_voice_doubao.rst` | Doubao voice chat |
| `py_voice_ollama` | `python_voice_ollama.rst` | Ollama voice chat |
| `py_action_gallery` | `python_action_gallery.rst` | Action gallery |
| `py_move` ~ `py_twist` | `python_*.rst` | Individual Python lessons |
| `ezb_move` ~ `ezb_twist` | `ezblock_*.rst` | Individual Ezblock lessons |
| `install_ezblock` | `get_start_app.rst` | Ezblock app setup |
| `picrawler_skill` | `openclaw.rst` | OpenClaw PiCrawler skill |

### RST File Boilerplate

Every lesson file starts with a Facebook community note (translated to the target language), followed by the reference label:

```rst
.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 ...
    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

.. _py_example:

NN. Lesson Title
====================================
```

### Link Substitutions (`rst_epilog` in `conf.py`)

All external links live as RST substitutions in `conf.py` under `rst_epilog`. This centralizes URL management. Pattern:
```python
.. |link_something| raw:: html

    <a href="https://example.com" target="_blank">Link Text</a>
```

When adding a new external link, add the `|link_xxx|` definition to `conf.py` on `docs-v3-en` **first**, then propagate to translation branches (translating only the link text, not the URL).

### Image Paths

- Top-level images: `/img/<name>.png` (prefixed with `/` for root-relative paths in some contexts)
- Chapter-specific: `img/<name>.png` (relative to the chapter's directory)
- OpenClaw images: `/img/openclaw/<name>.png`
- Python/Ezblock/Hardware: `img/<name>.png` within their respective directories

### File Naming

- Python lessons: `python_<topic>.rst` (snake_case)
- Ezblock lessons: `ezblock_<topic>.rst` (snake_case)
- Hardware components: `cpn_<component>.rst` (snake_case)
- AI interaction: `python_<topic>.rst` (shares `python_` prefix — these are Python-code-based AI lessons)

---

## Submodule: `docs/source/_shared`

Points to `https://github.com/sunfounder/sf-shared.git` (branch `main`). Contains shared SunFounder documentation assets reused across all product repos. When checking out this repo, run:

```bash
git submodule update --init --recursive
```

The `.readthedocs.yaml` includes `submodules: include: all` with `recursive: true`.

---

## Build & Preview

### Local Build (Sphinx)

```bash
cd docs
pip install -r requirements.txt
make html          # Output: docs/build/html/index.html
```

On Windows:
```batch
cd docs
make.bat html
```

### ReadTheDocs

Builds automatically on push to any branch. Configuration in `.readthedocs.yaml`:
- OS: Ubuntu 22.04, Python 3.11
- Sphinx config: `docs/source/conf.py`
- Builds all formats (HTML, PDF, ePub)
- Submodules: included recursively

### Published URLs

Each language branch maps to:
```
https://docs.sunfounder.com/projects/pi-crawler/<lang>/latest/
```
Where `<lang>` corresponds to the branch suffix: `en`, `de`, `zh-cn`, `fr`, `es`, `it`, `ja`.

---

## Common Maintenance Tasks

### Adding a New Lesson / Documentation Page

1. Create the `.rst` file on `docs-v3-en` in the appropriate chapter directory
2. Define a unique `.. _ref_label:` at the top
3. Add the file to the parent chapter's `.. toctree::` directive
4. If new external links are needed, add `|link_xxx|` definitions to `conf.py`
5. Build locally to verify: `cd docs && make html`
6. Commit on `docs-v3-en`
7. Propagate to translation branches (translate text, keep structure/labels/code)

### Syncing Content to a Translation Branch

1. Identify what's new/missing vs `docs-v3-en`:
   ```bash
   git diff docs-v3-en --name-only  # if on translation branch with EN as remote tracking
   ```
2. Copy image assets directly (no translation needed)
3. For each new/missing `.rst` file:
   - Copy the structure and code blocks as-is
   - Translate all descriptive/navigational text to the target language
   - Keep `.. _ref_label:`, `:ref:`, `.. image::`, `.. code-block::` directives unchanged
4. For `index.rst`: merge new toctree entries, translate new section descriptions
5. For `conf.py`: add new `|link_xxx|` definitions from EN branch (translate link text only)
6. Build locally to verify no broken references

### Updating the toctree Structure

The root toctree is in `index.rst`. Chapter-level toctrees are in:
- `python/play_with_python.rst`
- `ezblock/play_with_ezblock.rst`
- `ai_interaction/ai_interaction.rst`
- `hardware/cpn_hardware.rst`

When reordering or adding entries, ensure the same structure propagates to all language branches.

### Adding Support for a New LLM Provider

1. Add provider section to `python_online_llms.rst` (API key setup + test code)
2. Add any new screenshots to `ai_interaction/img/`
3. Add `|link_newprovider|` to `conf.py` `rst_epilog`
4. If a full voice chat example is needed, create a new `python_voice_<provider>.rst` and add it to `ai_interaction/ai_interaction.rst` toctree
5. Propagate to translation branches

### Handling Legacy Content in Translation Branches

Some translation branches may have pages not present in `docs-v3-en` (e.g., `openai.rst` in `docs-v3-de`). When syncing:
- **Keep** legacy pages in the toctree if they still provide value to that language's audience
- **Do not** add legacy pages to `docs-v3-en` unless they're being promoted to canonical status
- Legacy pages may need link updates if `conf.py` substitutions change

---

## Notes for AI Assistants

When working on this repository:

1. **Always identify the current branch first.** If it's not `docs-v3-en`, ask whether the change should start on `docs-v3-en` instead.
2. **The Facebook community note** at the top of every `.rst` file must be translated to the target language — use the existing translation from `index.rst` on that branch as a template.
3. **`conf.py` link substitutions** are the single source of external URLs. Never hardcode external links in `.rst` files — use `|link_xxx|` substitutions.
4. **Reference labels** (`.. _label:`) are code identifiers, not human-readable text. Never translate them.
5. **Code blocks** (Python, bash) are never translated. Comments within code blocks may be translated if they are user-facing, but variable names, function names, and command strings stay as-is.
6. **The `_shared` submodule** should not be modified directly — changes to shared assets go through the `sf-shared` repo.
7. **`.gitignore` already excludes** `.vscode`, `build*`, `secret*` files, and `.claude/` — do not commit these.
8. **Build output** goes to `docs/build/` and is gitignored — never commit build artifacts.
9. **When in doubt about language coverage**, check all `docs-v3-*` branches to understand what's been translated and what's lagging.
10. **The `show` script** at the repo root is a license/warranty display utility — it's not part of the documentation build.
