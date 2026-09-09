from app.llm.gemini import generate_text


response = generate_text(
    "Reply with exactly: Gemini connection successful"
)

print(response)