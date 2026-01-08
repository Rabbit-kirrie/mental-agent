import os
import requests

API_URL = os.getenv('DEEPSEEK_API_URL', 'https://api.deepseek.example/v1/chat')
API_KEY = os.getenv('DEEPSEEK_API_KEY')

def call_deepseek(user_text):
    headers = {'Authorization': f'Bearer {API_KEY}', 'Content-Type': 'application/json'}
    payload = {
        'model': 'deepseek-chat',
        'messages': [
            {"role": "system", "content": "你是一名会用中文回复的心理健康助手。"},
            {"role": "user", "content": user_text}
        ],
        'stream': False
    }
    resp = requests.post(API_URL, json=payload, headers=headers, timeout=15)
    resp.raise_for_status()
    data = resp.json()
    # DeepSeek 返回格式与 OpenAI 类似
    if 'choices' in data and data['choices']:
        return data['choices'][0]['message']['content']
    return str(data)
