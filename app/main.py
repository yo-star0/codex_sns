from __future__ import annotations

from flask import Flask, flash, redirect, render_template, request, url_for

from app.config import load_logs, load_settings, save_settings
from app.services import reschedule_job, run_post_job, start_scheduler


def create_app() -> Flask:
    app = Flask(__name__)
    app.secret_key = "change-this-secret"

    @app.route("/", methods=["GET", "POST"])
    def dashboard():
        settings = load_settings()

        if request.method == "POST":
            settings["genre"] = request.form.get("genre", settings["genre"])
            settings["post_interval_minutes"] = int(
                request.form.get("post_interval_minutes", settings["post_interval_minutes"])
            )
            settings["affiliate_link"] = request.form.get(
                "affiliate_link", settings["affiliate_link"]
            )
            settings["x_access_token"] = request.form.get("x_access_token", "")
            settings["threads_access_token"] = request.form.get(
                "threads_access_token", ""
            )
            settings["threads_user_id"] = request.form.get("threads_user_id", "")
            settings["openai_api_key"] = request.form.get("openai_api_key", "")
            settings["openai_model"] = request.form.get(
                "openai_model", settings.get("openai_model", "gpt-4o-mini")
            )

            save_settings(settings)
            reschedule_job()
            flash("設定を保存しました", "success")
            return redirect(url_for("dashboard"))

        logs = load_logs()[:50]
        return render_template("dashboard.html", settings=settings, logs=logs)

    @app.post("/post-now")
    def post_now():
        run_post_job()
        flash("手動投稿を実行しました", "success")
        return redirect(url_for("dashboard"))

    start_scheduler()
    return app


if __name__ == "__main__":
    application = create_app()
    application.run(host="0.0.0.0", port=5000, debug=True)
