from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from anthropic import Anthropic
import os

app = FastAPI()

# CORS configuration to allow requests from the frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify your domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class GenerateRequest(BaseModel):
    prompt: str
    text: str
    title: str = ""
    api_key: str
    model: str = "claude-sonnet-4-5-20250929"  # Default model


@app.post("/api/generate")
async def generate(request: GenerateRequest):
    """
    Generate AI content using Claude API.
    The API key is provided by the user (BYOK model).
    """
    if not request.api_key:
        raise HTTPException(status_code=400, detail="API key is required")

    if not request.prompt or not request.text:
        raise HTTPException(status_code=400, detail="Prompt and text are required")

    try:
        # Initialize Anthropic client with user's API key
        client = Anthropic(api_key=request.api_key)

        # Build the full prompt by replacing template variables
        full_prompt = request.prompt.replace("@doc", request.text)
        full_prompt = full_prompt.replace("@title", request.title)

        # Make the API call
        response = client.messages.create(
            model=request.model,
            max_tokens=1000,
            messages=[
                {"role": "user", "content": full_prompt}
            ]
        )

        # Extract the generated content
        generated_text = response.content[0].text

        return {
            "success": True,
            "content": generated_text,
            "model": request.model,
            "usage": {
                "prompt_tokens": response.usage.input_tokens,
                "completion_tokens": response.usage.output_tokens,
                "total_tokens": response.usage.input_tokens + response.usage.output_tokens
            }
        }

    except Exception as e:
        # Handle Anthropic API errors
        error_message = str(e)
        if "invalid_api_key" in error_message.lower() or "authentication" in error_message.lower():
            raise HTTPException(status_code=401, detail="Invalid Anthropic API key")
        elif "rate_limit" in error_message.lower():
            raise HTTPException(status_code=429, detail="Rate limit exceeded")
        else:
            raise HTTPException(status_code=500, detail=f"AI generation failed: {error_message}")


@app.get("/health")
async def health():
    """Health check endpoint"""
    return {"status": "ok"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)