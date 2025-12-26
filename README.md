# Snip Tool (OCR to Markdown/KaTeX)

A Python utility that converts images (like screenshots) into Markdown with KaTeX math formatting using an LLM via [OpenRouter](https://openrouter.ai/). The result is automatically copied to your clipboard.

## Workflow

1. Take a screenshot of a math formula or text
2. Run the tool (manually or via automation)
3. Paste the converted Markdown/KaTeX anywhere

Works great with automation tools like **Hazel**, **macOS Folder Actions**, or **BetterTouchTool**.

## Prerequisites

- Python 3.x
- An [OpenRouter](https://openrouter.ai/) API Key

## Installation

1. **Clone this repository**:
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

4. **Configure your API key**:
   
   Create a `.env` file in the project root:
   ```
   OPENROUTER_API_KEY=sk-or-v1-your-api-key...
   ```

5. **Optional - Customize the model**:
   
   Edit `config.yaml` to change the model or prompt:
   ```yaml
   model_name: "google/gemini-2.0-flash-001"
   prompt_ocr: "Your custom prompt here..."
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

The converted Markdown/KaTeX is automatically copied to your clipboard.

### Automation Setup (Folder Watcher)

The `run_snip.sh` script automatically detects its installation directory and uses the virtual environment if present. No manual path configuration needed.

Make sure it's executable:
```bash
chmod +x run_snip.sh
```

#### macOS Folder Actions (Built-in, Free)

1. Open **Automator.app**
2. Choose **Folder Action**
3. Select the folder to watch (e.g., `~/Desktop/Screenshots`)
4. Add a **"Run Shell Script"** action
5. Set "Pass input:" to **"as arguments"**
6. Enter:
   ```bash
   /path/to/snip-tool/run_snip.sh "$1"
   ```
7. Save the action

#### Hazel (Paid)

1. Add your screenshot folder to Hazel
2. Create a rule: "Extension is png"
3. Action: "Run Shell Script"
4. Script:
   ```bash
   /path/to/snip-tool/run_snip.sh "$1"
   ```

#### BetterTouchTool

1. Add a Keyboard Shortcut trigger
2. Action: **"Execute Terminal Command (Async)"**
3. Command:
   ```bash
   /path/to/snip-tool/run_snip.sh {filepath}
   ```

## Configuration

| File | Purpose |
|------|---------|
| `.env` | API key (required, not committed to git) |
| `config.yaml` | Model and prompt settings (optional) |

### Default Model

The default model is `google/gemini-2.0-flash-001`. You can change it in `config.yaml`:

```yaml
model_name: "gpt-4o-mini"
```

## What's next ?

I might rewrite it in Golang as a single binary, stay tunned !

## License

MIT License
