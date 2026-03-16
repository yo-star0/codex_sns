from __future__ import annotations

from datetime import datetime

from apscheduler.schedulers.background import BackgroundScheduler

from app.ai_generator import generate_post_text
from app.config import load_logs, load_settings, save_logs
from app.sns_clients import post_to_threads, post_to_x

scheduler = BackgroundScheduler(daemon=True)


def append_log(level: str, message: str) -> None:
    logs = load_logs()
    logs.insert(
        0,
        {
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "level": level,
            "message": message,
        },
    )
    save_logs(logs[:200])


def run_post_job() -> None:
    settings = load_settings()
    try:
        text = generate_post_text(
            settings["genre"],
            settings["affiliate_link"],
            settings.get("openai_api_key", ""),
            settings.get("openai_model", "gpt-4o-mini"),
        )
        append_log("INFO", f"生成投稿文: {text}")

        x_result = post_to_x(text, settings)
        append_log("INFO", x_result)

        threads_result = post_to_threads(text, settings)
        append_log("INFO", threads_result)
    except Exception as exc:  # noqa: BLE001
        append_log("ERROR", f"投稿処理でエラー: {exc}")


def reschedule_job() -> None:
    settings = load_settings()
    minutes = int(settings.get("post_interval_minutes", 120))

    if scheduler.get_job("auto_post"):
        scheduler.remove_job("auto_post")

    scheduler.add_job(run_post_job, "interval", minutes=minutes, id="auto_post")
    append_log("INFO", f"スケジューラー更新: {minutes}分間隔")


def start_scheduler() -> None:
    if not scheduler.running:
        scheduler.start()
    reschedule_job()
