from __future__ import annotations

from datetime import datetime

import requests


def generate_post_text(
    genre: str,
    affiliate_link: str,
    openai_api_key: str,
    model: str,
) -> str:
    """Generate Japanese SNS post text by AI, fallback to template if no key."""
    if not openai_api_key:
        return _fallback_text(genre, affiliate_link)

    prompt = (
        f"あなたはSNS運用担当です。ジャンル: {genre}。"
        "日本語で120文字以内の魅力的な投稿文を1つ作成してください。"
        f"最後に自然な形でこのリンクを含めてください: {affiliate_link}"
    )

    response = requests.post(
        "https://api.openai.com/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {openai_api_key}",
            "Content-Type": "application/json",
        },
        json={
            "model": model,
            "messages": [
                {"role": "system", "content": "日本語のSNS投稿コピーライターとして振る舞ってください。"},
                {"role": "user", "content": prompt},
            ],
            "temperature": 0.8,
        },
        timeout=20,
    )
    response.raise_for_status()
    data = response.json()
    text = data["choices"][0]["message"]["content"].strip()
    return text


def _fallback_text(genre: str, affiliate_link: str) -> str:
    now = datetime.now().strftime("%H:%M")
    return (
        f"【{genre}の豆知識 {now}】今日も役立つ情報をシェア！"
        f"詳細はこちら→ {affiliate_link}"
    )
