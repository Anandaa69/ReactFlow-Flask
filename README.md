# ReactFlow-Flask Setup Guide

## Prerequisites
```
- Node.js and npm
- Python 3.12
- Git
```

## Installation & Setup

### 1. Clone the Repository
```
git clone git@github.com:Anandaa69/ReactFlow-Flask.git
cd ReactFlow-Flask
```

### 2. Frontend Setup (Terminal 1)
```
cd client
npm install
npm run dev
```
`Frontend will be running on the development server`

### 3. Backend Setup (Terminal 2)
```
cd ../server
# Create virtual environment
python3.12 -m venv venv

# Activate virtual environment
# On Windows:
.\venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install poetry
poetry install --no-root

# Run the server
python main.py
```
`Backend server will be running`

## Running the Application

You'll need `two terminals` running simultaneously:

```
Terminal 1: Frontend (React) -> npm run dev
Terminal 2: Backend (Flask)  -> python main.py
```

## Project Structure
```
ReactFlow-Flask/
├── client/          # React frontend
│   ├── package.json
│   └── ...
├── server/          # Flask backend
│   ├── main.py      # Flask backend entry point
│   ├── pyproject.toml
│   └── ...
└── README.md
```

## Troubleshooting
```
- Make sure both terminals are running for full functionality
- Ensure Python 3.12 is installed and accessible
- Check that all dependencies are properly installed before running servers
```
