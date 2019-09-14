# history-browser-for-chrome

- chromeの履歴データベースを自動で参照し表示します。パスの指定も必要ありません。現在windowsのみ対応。Linux対応は要望あればすぐに考えます。
- 閲覧にはpythonにもとからインストールされているtkinterというGUIツールを用いたものと、flaskかBottleを用いたものなどを考えてます
- 自分用なので、まずニコニコ動画の視聴履歴を分析するツールとして開発しています。

# 実行

- requirements.txt(準備中)を用い必要なパッケージをインストール後、
    - flask(ウェブブラウザ閲覧)の起動は、`python nicovideo_flask.py`を使用してください。（現在こちらのみ鋭意更新中です。他のはまあコードの中身を見て判断してください。）
    
# staticディレクトリについて

- bootstrapなどが入っています。ライセンス情報などはソースを参照。

# ぼやき

- bootstrapを使おうと思って途中でsemantic UIの存在を知ったためその跡形がコメントとかで残ってます。ごめんなさい。 

# 動作イメージ

- flask
![image](https://user-images.githubusercontent.com/24700480/64904433-029a8480-d705-11e9-974e-53b4acf0bb75.png)
