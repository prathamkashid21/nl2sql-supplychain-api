import os
import time

from google import genai
from dotenv import load_dotenv


load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

client = genai.Client(
    api_key=API_KEY
)

MODEL_NAME = "gemini-3.6-flash"


def generate_text(prompt: str) -> str:

    max_retries = 3

    for attempt in range(max_retries):

        try:

            response = client.models.generate_content(
                model=MODEL_NAME,
                contents=prompt
            )

            return response.text.strip()

        except Exception as e:

            error_message = str(e)

            if "429" in error_message or "RESOURCE_EXHAUSTED" in error_message:
               raise RuntimeError(
                "Gemini API quota exceeded. "
                 "Please wait for the quota to reset or check your Gemini API plan."
                   )

            if "503" in error_message or "UNAVAILABLE" in error_message:
                if attempt < max_retries - 1:

                    wait_time = 2 ** attempt

                    print(
                        f"Gemini temporarily unavailable. "
                        f"Retrying in {wait_time} seconds..."
                    )

                    time.sleep(wait_time)

                else:
                    raise

            else:
                raise