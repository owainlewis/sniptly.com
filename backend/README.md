# Sniptly Backend

Python backend for Sniptly AI writing assistant using FastAPI and Claude (Anthropic).

## Setup

This project uses [uv](https://github.com/astral-sh/uv) as the package manager.

### Install dependencies

```bash
cd backend
uv sync
```

### Run the server

```bash
uv run python main.py
```

Or using uvicorn directly:

```bash
uv run uvicorn main:app --reload --port 8000
```

The API will be available at `http://localhost:8000`

## API Endpoints

### POST /api/generate

Generate AI content using Claude.

**Request:**
```json
{
  "prompt": "Create a tweet from this text: @doc",
  "text": "Your article content here",
  "api_key": "sk-ant-...",
  "model": "claude-sonnet-4-5-20250929"
}
```

**Response:**
```json
{
  "success": true,
  "content": "Generated content here...",
  "model": "claude-sonnet-4-5-20250929",
  "usage": {
    "prompt_tokens": 100,
    "completion_tokens": 50,
    "total_tokens": 150
  }
}
```

### GET /health

Health check endpoint.

## Security

- User API keys are **never stored** on the server
- Keys are passed through the request and used only for that generation
- CORS is configured to allow frontend requests
- In production, update CORS settings to allow only your domain