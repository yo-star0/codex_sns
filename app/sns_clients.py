from __future__ import annotations

import requests


def post_to_x(text: str, settings: dict) -> str:
    token = settings.get("x_access_token", "")
    if not token:
        return "X投稿スキップ: アクセストークン未設定"

    response = requests.post(
        "https://api.twitter.com/2/tweets",
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
        },
        json={"text": text},
        timeout=20,
    )
    response.raise_for_status()
    return "X投稿成功"


def post_to_threads(text: str, settings: dict) -> str:
    token = settings.get("threads_access_token", "")
    user_id = settings.get("threads_user_id", "")
    if not token or not user_id:
        return "Threads投稿スキップ: トークンまたはユーザーID未設定"

    create_res = requests.post(
        f"https://graph.threads.net/v1.0/{user_id}/threads",
        data={
            "media_type": "TEXT",
            "text": text,
            "access_token": token,
        },
        timeout=20,
    )
    create_res.raise_for_status()
    media_id = create_res.json().get("id")

    publish_res = requests.post(
        f"https://graph.threads.net/v1.0/{user_id}/threads_publish",
        data={
            "creation_id": media_id,
            "access_token": token,
        },
        timeout=20,
    )
    publish_res.raise_for_status()
    return "Threads投稿成功"
