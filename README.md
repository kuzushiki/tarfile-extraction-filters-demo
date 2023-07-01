# tarfile-extraction-filters-demo

[３２回 初心者のためのセキュリティ勉強会（オンライン開催）](https://sfb.connpass.com/event/285981/)で発表した  **Extraction Filters** のデモです

発表資料は[こちら](https://github.com/kuzushiki/tarfile-extraction-filters-demo/blob/main/slides-export.pdf)

なにか質問等あれば[Twitter](https://twitter.com/kuzu7shiki)で連絡ください

## 環境構築 (要Docker Compose)

1. 本リポジトリをクローンします
```
git clone git@github.com:kuzushiki/tarfile-extraction-filters-demo.git
```

2. ディレクトリを移動します
```
cd tarfile-extraction-filters-demo
```

3. Docker Composeでコンテナを起動します
```
docker compose up
```

4. URLにアクセスして、ページが表示されることを確認します
```
http://localhost:5000
```

## デモ内容

アクセスすると、下記のシンプルなファイルアップロード画面が表示されます。

また、`Filter`の値を選択することができます。ここで選択した値がExtraction Filtersにおける`filter`引数の値として渡されます。

<img width="466" alt="image" src="https://github.com/kuzushiki/tarfile-extraction-filters-demo/assets/50363796/e05a59e3-fb00-4779-9220-78b63f817341">

色々なtarアーカイブをアップロードし、`Filter`の値ごとの挙動の違いを確認してみましょう。

`test`ディレクトリにテスト用のtarアーカイブを用意しています。

1.  `absolute_link_test.tar` : `/etc/passwd`を参照するシンボリックリンクを格納
2.  `absolute_path_test.tar` : `hacked!!`と書かれた`/etc/passwd`を格納
3.  `link_outside_destination_test.tar` : `../../../../etc/passwd`を参照するシンボリックリンクを格納
4. `outside_destination_test.tar` : `hacked!!`と書かれた`../../../../etc/passwd`を格納

`Clear Uploads Directory`ボタンをクリックすることで、アップロードディレクトリを空にすることができます。
