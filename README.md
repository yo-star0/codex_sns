# Raspberry Pi向け SNS自動投稿ツール

Python + Flaskで動作するSNS自動投稿ツールです。

## 実装機能
- 管理画面（投稿ジャンル / 投稿間隔 / アフィリエイトリンク設定）
- AI投稿生成（OpenAI API、未設定時はテンプレート文）
- X API投稿
- Threads API投稿
- スケジューラー投稿（APScheduler）
- 投稿ログ表示

## フォルダ構成
```text
codex_sns/
├── app/
│   ├── __init__.py
│   ├── ai_generator.py
│   ├── config.py
│   ├── main.py
│   ├── services.py
│   └── sns_clients.py
├── skills/
│   └── sns-auto-post-operator/
│       ├── SKILL.md
│       └── references/
│           └── kids-manual-template.md
├── static/
│   └── style.css
├── templates/
│   └── dashboard.html
├── MANUAL_しょうがくせいむけ.md
├── requirements.txt
├── run.py
└── README.md
```

## セットアップ
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python run.py
```

ブラウザで `http://<RaspberryPiのIP>:5000` にアクセスしてください。

## マニュアル
- 小学生向けの操作マニュアル: `MANUAL_しょうがくせいむけ.md`
- 運用スキル: `skills/sns-auto-post-operator/`

## 補足
- X投稿は `x_access_token` をBearerとして送信しています（運用時はOAuth 2.0や署名方式の調整が必要な場合があります）。
- Threads投稿はGraph APIを利用しています。
- APIキー類は本番では`.env`や秘密管理サービスに保存してください。
