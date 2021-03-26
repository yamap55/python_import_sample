# Python の import について

---

## アジェンダ

- はじめに
- 概要
- コードで説明
- 参考

---

## はじめに

--

- 仕様書からの情報ではありません
- 詳細は仕様書を確認お願いします
  - 何かわかったら教えてください 🙇

https://docs.python.org/ja/3/reference/import.html

---

## 概要

--

- import がどうやって動いているのかよくわからない
- コードで試した

---

## コードの紹介

--

- `./src/main1.py`
  - b.py から値を取得してそれを使った文字列を返す
- `./src/b.py`
  - define.py で定義されている固定値を返す関数が定義されている
- `./src/define.py`
  - 固定値が定義されている

---

## やりたい事

- `./src/define.py` を変更しないで固定値を変更したい

---

## 直接値を変更

- `./src/main2.py`

---

## import されているコードで値を変更

- `./src/main3.py`

---

## import 前に直接値を変更

- `./src/main4.py`

---

## どういう時に使うの？

- -> ユニットテストで使用する
- `./tests/test_main.py`
- 実行は `python -m pytest`

--

- 普通にテスト
- 固定値を変更したい
  - ファイルの読み込み元とか？
- 関数自体をモック化する事もよくある

---

## 参考

- 公式ドキュメント
  - https://docs.python.org/ja/3/reference/import.html
- 試すためのリポジトリ
  - https://github.com/yamap55/python_import_sample
