#!/bin/bash

SCRIPT_DIR=$(dirname "$0")
PYTHON_SCRIPT="$SCRIPT_DIR/mac_changer.py"

if [ -f "$PYTHON_SCRIPT" ]; then
    python3 "$PYTHON_SCRIPT" "$@"
else
    echo "El archivo $PYTHON_SCRIPT no existe."
    exit 1
fi

