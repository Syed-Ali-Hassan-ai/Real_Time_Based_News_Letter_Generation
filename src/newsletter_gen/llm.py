import requests

# Callable instance of fireworks llm
token = "I7Jd48YOIXXqNeQwuAXGOYGMd0bYbBC7zx9P0ivpe3h663j6"
def llm_model(request: str, **args):
    url = "https://api.fireworks.ai/inference/v1/chat/completions"
    payload = {
        "model": "accounts/fireworks/models/llama-v3p1-8b-instruct",
        "messages": [
            {
            "role": "user",
            "content": request,
            "name": "<string>"
            }
        ],
        "max_tokens": 1024,
        "temperature": 0.3,
        "frequency_penalty": 0.2,
        "response_format": {"type": "text"},
        "context_length_exceeded_behavior": "truncate",
        "user": "string",
        **args
    }

    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "authorization": f"Bearer {token}"
    }

    response = requests.post(url, json=payload, headers=headers)

    if response.status_code == 200:
        response_data = response.json()
        message_content = response_data['choices'][0]['message']["content"]
        return message_content, response_data["usage"]["total_tokens"]
    else:
        print(f"Error: {response.status_code}")
        print(response.text)
        return "Server Error"
