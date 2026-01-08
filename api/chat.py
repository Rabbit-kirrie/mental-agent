import os
import requests

def handler(request):
    try:
        data = request.json()
        user_text = data.get("text", "")
        payload = {
            "model": "deepseek-chat",
            "messages": [
                {"role": "system", "content": "你是一名会用中文回复的心理健康助手。"},
                {"role": "user", "content": user_text}
            ],
            "stream": False
        }
        headers = {
            "Authorization": f"Bearer {os.getenv('DEEPSEEK_API_KEY')}",
            "Content-Type": "application/json"
        }
        resp = requests.post(os.getenv('DEEPSEEK_API_URL'), json=payload, headers=headers, timeout=15)
        resp.raise_for_status()
        data = resp.json()
        reply = data.get("choices", [{}])[0].get("message", {}).get("content", "") if "choices" in data else str(data)
        return {
            "statusCode": 200,
            "headers": {"Content-Type": "application/json"},
            "body": f'{{"reply": "{reply}"}}'
        }
    except Exception as e:
        return {
            "statusCode": 500,
            "headers": {"Content-Type": "application/json"},
            "body": f'{{"error": "{str(e)}"}}'
        }
