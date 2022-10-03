# 問3

問3で作成したcsvファイルを利用して、`share`から`subject`を推論するためのコードを作成してください。<br>
`DeepLearning/no3/main.py`にてコードを作成し、テストデータに対する推論結果を`DeepLearning/no3/pred.csv`に出力してください。その際、encodingは'utf-8'、ヘッダー行あり、カラムは'subject'のみの条件で出力してください。

## ファイルの説明
examination_test.csv : (テスト用) 入試の問題文 (1行は1つの大問に対応)

## 利用可能なライブラリ
 numpy, pandas, sklearn, janome, mecab, torch, torchvision, torchnet, torchtext, transformers, tensorflow, keras
 
## 注意事項
採点は格納されたcsvファイルのみを対象として行います。