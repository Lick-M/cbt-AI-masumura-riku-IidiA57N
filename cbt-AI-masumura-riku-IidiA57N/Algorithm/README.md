# Algorithm

問1,2,3に解答してください。それぞれ[no1](no2), [no2](no2), [no3](no3)にあります。

## 回答形式

### 短答問題(no1)について

短答問題の回答形式確認のテストでは、与えられた`answer.yaml`のキーを勝手に変更したり、削除しない限りは通ります。ただ、1点注意として、`key: value` のようにコロンの後には半角スペースを必ず入れるようにしてください。入れない場合、正しく採点されない場合があります。

（良い例）
![yaml良い例](../docs/yaml1.png)

（悪い例）
![yaml悪い例](../docs/yaml2.png)

### コーディング問題(no2, no3)について

アルゴリズムのコーディング問題の回答形式確認テストでは、与えられた`data/`以下のサンプルケースの答えを正しく出力できるかをテストします。回答が間違っている場合や、何も出力できていない場合は以下の様なエラーが出ます。

```bash
E   AssertionError: '' != 'Fizz!\n22\nBuzz!\nFizz Buzz!'
E   + Fizz!
E   + 22
E   + Buzz!
E   + Fizz Buzz!
```