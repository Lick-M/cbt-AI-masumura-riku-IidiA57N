# 問2

以下の指示に従ってcsvファイルを整形してください。コードは`DeepLearning/no2/main.py`に記述してください。

## ファイルの説明
次のフィールド定義に従うcsvファイルが与えられます。
* `examination_train_meta.csv`

|  フィールド  |  説明  |
|:---------|:-------|
|     id      |0から始まる一意に定まる整数|
|    year      |出題年度（西暦）を表す4桁の整数|
|   college    |大学名を表す文字列|
|   subject    |教科名を表す文字列|

* `examination_train_text.csv`

|  フィールド  |  説明  |
|:-------------|:-------|
|     id      |0から始まる一意に定まる整数|
|    meta_id  |`examination_train_meta.csv`の`id`に対応する外部キー|
|   share   |問題文の文字列|

## Section1
`examination_train_text.csv`は`meta_id`を外部キーとして、`examination_train_meta.csv`（主キーは`id`）を参照できる。これらをmergeした上で(text側の)`id`による並び替えを行ってください。その際、カラムは`‘id’, ‘year’, ‘college’, ‘subject’, ‘share’`のみをこの順番で残してください。mergeが完了したら`DeepLearning/no2/no2_1.csv`に出力してください。

例)
`examination_train_text.csv`
```
id,meta_id,share
0,0, 次の文章は、日本の大学生ヒロシ...
1,0, 日本人のOさんとAさんは、...
2,0, エミさんはの小説「二十四...
3,1, 近年の世界経済では、...
```
`examination_train_meta.csv`
```
id,year,college,subject
0,2000,センター試験,地理
1,2000,一橋大学,地理
2,2000,京都大学,地理
3,2000,北海道大学,地理
```
`DeepLearning/no2/no2_1.csv`
```
id,year,college,subject,share
0,2000,センター試験,地理, 次の文章は、日本の大学生ヒロシ...
1,2000,センター試験,地理, 日本人のOさんとAさんは、...
2,2000,センター試験,地理, エミさんはの小説「二十四...
3,2000,一橋大学,地理, 近年の世界経済では、...
```

## Section2
先ほどmergeした表のうちいくつかの行では、カラム`share`が空になってしまっています。
これらの欠損値を含む行を削除してください。完了したら`DeepLearning/no2/no2_2.csv`に出力してください。

## Section3
その２までで作成した表から、カラム`‘subject’, ‘share’`のみをこの順番で残したcsvファイルを`DeepLearning/no2/train_clean.csv`に出力してください。その際「‘utf8’, ‘ヘッダー行あり‘, ‘インデックス列なし‘, ‘カンマ区切り’」の条件でcsv出力してください。

## 注意事項
採点は格納されたcsvファイルのみを対象として行います。
