# Snip Tool (OCR to Markdown/KaTeX)

A Python utility that automatically converts images (like screenshots) into Markdown with KaTeX math formatting using an LLM (via OpenRouter). The result is copied directly to your clipboard.

Designed to be used with automation tools like **Hazel**, **macOS Folder Actions**, or **BetterTouchTool** to streamline your workflow:
1. Take a screenshot of a math formula or text.
2. Save it to a specific folder.
3. The tool runs automatically.
4. Paste the converted Markdown/KaTeX anywhere.

## Prerequisites

- Python 3.x
- An [OpenRouter](https://openrouter.ai/) API Key.

## Installation

1. **Clone or download** this repository:
   ```bash
   git clone https://github.com/YOUR_USERNAME/snip-tool.git
   cd snip-tool
   ```

2. **Create a virtual environment** (recommended):
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Configuration**:
   Create a `.env` file in the project root:
   ```bash
   OPENROUTER_API_KEY=sk-or-v1-your-api-key...
   ```

   Optionally, edit `config.yaml` to change the model or prompt:
   ```yaml
   model_name: "gpt-4o-mini" # or "google/gemini-2.0-flash-001"
   ```

## Usage

### Manual Usage
```bash
python snip.py /path/to/image.png
```

Or using the wrapper script:
```bash
./run_snip.sh /path/to/image.png
```

### Automation Setup (Watch Folder)

To run this automatically when a screenshot is saved to a folder, you need a "Folder Watcher".

#### 1. Configure the Wrapper Script

The `run_snip.sh` script is provided for use with automation tools. Edit it to set the correct path to your installation:

```bash
# Edit run_snip.sh and update PROJECT_DIR to your installation path
PROJECT_DIR="/path/to/snip-tool"
```

Make sure it's executable:
```bash
chmod +x run_snip.sh
```

#### 2. Configure Automation

**Option A: macOS Folder Actions (Built-in, Free)**
1. Open **Automator.app**.
2. Choose **Folder Action**.
3. At the top, select the folder you want to watch (e.g., `~/Desktop/Screenshots`).
4. Add a **"Run Shell Script"** action.
5. Change "Pass input:" to **"as arguments"**.
6. Paste the following code:
   ```bash
   /path/to/snip-tool/run_snip.sh "$1"
   ```
7. Save the action.

**Option B: Hazel (Paid, Easier)**
1. Add your screenshot folder to Hazel.
2. Add a new rule: "If all conditions met" -> "Extension is png" (or image).
3. Do the following: "Run Shell Script".
4. Select "Embedded script" and point it to your wrapper script:
   ```bash
   /path/to/snip-tool/run_snip.sh "$1"
   ```

**Option C: BetterTouchTool**
While BTT is primarily for inputs, you can use "Folder Triggers" (if available in your version) or bind a keyboard shortcut to run the script on the *currently selected file* in Finder.
1. Add a new Trigger (e.g., Keyboard Shortcut).
2. Action: **"Execute Terminal Command (Async)"**.
3. Command:
   ```bash
   /path/to/snip-tool/run_snip.sh {filepath}
   ```

## License

MIT License
