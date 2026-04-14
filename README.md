# Legacy Revitalizer

## Overview
This project refactors a legacy Python script that originally used global variables, cryptic names, insecure authentication, mixed responsibilities, and weak file handling.

## Original issues
- Global mutable state
- Poor variable and function naming
- Mixed authentication, business logic, persistence, and UI flow
- No proper error handling for file operations
- Unused dead code
- Hardcoded insecure credentials

## Improvements made
- Removed global variables
- Introduced clearer naming
- Separated responsibilities into focused components
- Extracted file persistence logic
- Added error handling
- Cleaned the execution flow using `main()`
- Removed unused code
- Added docstrings and documentation

## Files
```
copilot-legacy-revitalizer/
├── src/
│   ├── __init__.py          # Marks src/ as a Python package
│   ├── data_manager.py      # Manages data items: add, retrieve, display
│   ├── authenticator.py     # Handles user authentication
│   ├── data_persistence.py  # Saves/loads data to/from JSON file with error handling
│   ├── application.py       # Orchestrates app flow: auth, data ops, persistence
│   └── main.py              # Entry point: initializes and runs the app
├── process_data.py          # Refactored single-file version (reference)
├── process_data.original.py # Original legacy/spaghetti code (seed for this project)
├── docker-compose.yml       # Docker Compose config for containerized run
├── dockerfile               # Dockerfile for Python environment
├── plan.md                  # Refactoring plan
├── log.md                   # Implementation log
├── README.md                # This file
└── data.txt                 # JSON data file (auto-created if missing)
```

## How to run
Run the multi-file version:
```bash
python -m src.main
```

For the refactored single-file version:
```bash
python process_data.py
```

For the original legacy version:
```bash
python process_data.original.py
```

## Running with Docker
If Python is not installed locally, use Docker to run the application in a containerized bash console.

1. Ensure Docker and Docker Compose are installed.
2. Build and run the container:
```bash
docker-compose up --build
```
3. This opens an interactive bash console in the container. Run the scripts as needed:
```bash
python process_data.original.py  # for original
python -m src.main              # for refactored
```

## Use of GitHub Copilot

GitHub Copilot was used throughout the process to:
- Understand the legacy code using @workspace
- Identify code smells
- Generate docstrings
- Suggest refactoring strategies
- Improve error handling and structure
