import os
from dotenv import load_dotenv

load_dotenv()

def require_env(var_name: str) -> str:
    value = os.getenv(var_name)
    if not value:
        raise EnvironmentError(f"Required environment variable '{var_name}' is not set.")
    return value

GOOGLE_GENAI_USE_VERTEXAI=require_env("GOOGLE_GENAI_USE_VERTEXAI")
GOOGLE_API_KEY=require_env("GOOGLE_API_KEY")
GITLAB_TOKEN=require_env("GITLAB_TOKEN")

print("Constants loaded successfully.")
print(GOOGLE_API_KEY)

