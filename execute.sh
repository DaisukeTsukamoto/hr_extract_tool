#!/bin/bash

# ログファイルのディレクトリとファイル名を設定
mkdir -p log
log_file="log/$(date +%Y%m%d%H%M%S).log"

# ログの開始時刻をファイルに記録
echo "開始時刻: $(date)" > "$log_file"

# Pythonの仮想環境を有効にする
. .venv/Scripts/activate

# Python スクリプトを実行し、出力をログファイルに追加（コンソールにも出力）
python . | tee -a "$log_file"

# ログの終了時刻をファイルに記録
echo "終了時刻: $(date)" | tee -a "$log_file"

# ユーザーが何かキーを押すまで待機
echo "実行が完了しました。ウィンドウを閉じるには何かキーを押してください..."
read -p ""
