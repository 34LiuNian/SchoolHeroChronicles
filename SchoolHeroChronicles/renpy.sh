#!/bin/bash

# Ren'Py game launcher script
# This script starts the Ren'Py engine with the specified project.

# Set the path to the Ren'Py launcher
RENPY_PATH="/path/to/renpy"

# Set the project directory
PROJECT_DIR="$(dirname "$0")"

# Start the Ren'Py engine with the specified project
"$RENPY_PATH/renpy.sh" "$PROJECT_DIR"