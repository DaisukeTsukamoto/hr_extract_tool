@echo off
REM ログファイルのディレクトリとファイル名を設定
mkdir log
set log_file=log\%date:~0,4%%date:~5,2%%date:~8,2%%time:~0,2%%time:~3,2%%time:~6,2%.log

REM ログの開始時刻をファイルに記録
echo 開始時刻: %date% %time% > %log_file%

REM Pythonの仮想環境を有効にする
call .venv\Scripts\activate

REM Python スクリプトを実行し、出力をログファイルに追加（コンソールにも出力）
python . >> %log_file%

REM ログの終了時刻をファイルに記録
echo 終了時刻: %date% %time% >> %log_file%
