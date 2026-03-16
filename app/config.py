from __future__ import annotations

import json
from pathlib import Path
from typing import Any

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
SETTINGS_FILE = DATA_DIR / "settings.json"
LOG_FILE = DATA_DIR / "post_logs.json"

DEFAULT_SETTINGS: dict[str, Any] = {
    "genre": "テクノロジー",
    "post_interval_minutes": 120,
    "affiliate_link": "https://example.com/affiliate",
    "x_api_key": "",
    "x_api_secret": "",
    "x_access_token": "",
    "x_access_token_secret": "",
    "threads_access_token": "",
    "threads_user_id": "",
    "openai_api_key": "",
    "openai_model": "gpt-4o-mini",
}


def ensure_data_files() -> None:
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    if not SETTINGS_FILE.exists():
        SETTINGS_FILE.write_text(
            json.dumps(DEFAULT_SETTINGS, ensure_ascii=False, indent=2),
            encoding="utf-8",
        )
    if not LOG_FILE.exists():
        LOG_FILE.write_text("[]", encoding="utf-8")


def load_settings() -> dict[str, Any]:
    ensure_data_files()
    current = json.loads(SETTINGS_FILE.read_text(encoding="utf-8"))
    merged = {**DEFAULT_SETTINGS, **current}
    return merged


def save_settings(settings: dict[str, Any]) -> None:
    ensure_data_files()
    SETTINGS_FILE.write_text(
        json.dumps(settings, ensure_ascii=False, indent=2), encoding="utf-8"
    )


def load_logs() -> list[dict[str, Any]]:
    ensure_data_files()
    return json.loads(LOG_FILE.read_text(encoding="utf-8"))


def save_logs(logs: list[dict[str, Any]]) -> None:
    ensure_data_files()
    LOG_FILE.write_text(json.dumps(logs, ensure_ascii=False, indent=2), encoding="utf-8")
