#!/bin/bash

# Snip Tool Runner Script
# This script is designed to be called by automation tools like Hazel, 
# macOS Folder Actions, or BetterTouchTool.

# Get the directory where this script is located
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Check if an image path was provided
if [ -z "$1" ]; then
    echo "Usage: $0 <image_path>"
    exit 1
fi

# Change to the project directory (required for config.yaml to be found)
cd "$SCRIPT_DIR"

# Use the virtual environment Python if it exists, otherwise use system Python
if [ -f "$SCRIPT_DIR/.venv/bin/python" ]; then
    PYTHON_EXEC="$SCRIPT_DIR/.venv/bin/python"
else
    PYTHON_EXEC="python3"
fi

# Run the snip tool
"$PYTHON_EXEC" "$SCRIPT_DIR/snip.py" "$1"
