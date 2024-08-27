#kimiapi.py

from openai import OpenAI


def get_kimi_response(user_message): 
    client = OpenAI(
    api_key="sk-5LW3cdjUg63f6ZijkEM0gWnjRcbYRUe6QuUjkoVxuiWqqo9p", # 在这里将 MOONSHOT_API_KEY 替换为你从 Kimi 开放平台申请的 API Key
    base_url="https://api.moonshot.cn/v1",)
 
    completion = client.chat.completions.create(
    model = "moonshot-v1-8k",
    messages = [
        {"role": "system", "content": "你是 Kimi，由 Moonshot AI 提供的人工智能助手，你的回答在20字以内，标点符号只能使用句号的逗号"},
        {"role": "user", "content": "user_message"}
    ],
    temperature = 0.3,)
 
# 通过 API 我们获得了 Kimi 大模型给予我们的回复消息（role=assistant）
    return completion.choices[0].message.content