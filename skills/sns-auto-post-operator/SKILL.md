---
name: sns-auto-post-operator
description: Configure, operate, and troubleshoot the Flask-based Raspberry Pi SNS auto-posting tool (genre/interval/affiliate settings, AI text generation, X and Threads posting, scheduler, and logs). Use when users ask for setup, daily operation, failure diagnosis, or safe credential handling for this app.
---

# SNS Auto Post Operator

## Overview
Use this skill to run the local SNS auto-posting app safely and quickly.
Prioritize simple Japanese explanations if the user is non-technical.

## Quick Workflow
1. Confirm app files exist (`run.py`, `app/`, `templates/`, `static/`).
2. Install dependencies and start app.
3. Open dashboard and configure settings.
4. Run manual post once.
5. Check logs and fix errors.

## Standard Commands
Run from repository root.

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python run.py
```

If dependency install fails due to restricted network, report it as environment limitation and continue with static checks (e.g., `python3 -m compileall app run.py`).

## Dashboard Operation Checklist
- Set `投稿ジャンル`.
- Set `投稿間隔（分）`.
- Set `アフィリエイトリンク`.
- Set credentials:
  - `X Access Token`
  - `Threads Access Token`
  - `Threads User ID`
  - `OpenAI API Key`
- Click `設定を保存`.
- Click `今すぐ投稿実行` for one-shot test.
- Review `投稿ログ` for `INFO` / `ERROR`.

## Troubleshooting Rules
- Missing token/user ID: explain that posting is skipped by design.
- API 401/403: treat as credential or permission issue.
- API timeout/connection issue: treat as network issue.
- Repeated scheduler errors: verify interval value and API keys, then trigger manual post.

## Communication Style
- Explain in short steps.
- For beginner users, use everyday Japanese and avoid jargon.
- When giving commands, provide copy-paste blocks.

## References
Load `references/kids-manual-template.md` when the user asks for a child-friendly guide.
