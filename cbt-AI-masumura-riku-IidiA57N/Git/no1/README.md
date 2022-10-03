# 問1

以下の問題に対する答えをyamlファイルに記載してください。

## Section1

---

#### Q1: Gitに関する説明として正しいものにTを、誤ったものにFを記入せよ。

A. 更新履歴を確認したり戻したりすることができる

B. チームの共同作業に向いている

C. 作業の記録の流れを切り替えられる

D. ほとんどの操作でネットワーク通信が必須であり、オフラインでの作業が困難

<br>

#### Q2: 次のGitに関する用語とその説明について正しく対応させよ。

A. プッシュ
B. リポジトリ
C. ステージングエリア(インデックス)
D. プル
E. ブランチ

##### 説明
1. 履歴管理を枝のようにわかれさせたもの
2. コミットしたいファイルやフォルダの一部を登録する部分
3. ファイルやフォルダの履歴管理を行う場所
4. リモートリポジトリの変更をローカルリポジトリに反映させること
5. ローカルリポジトリの変更をリモートリポジトリに反映させること

<br>

Gitにおいて、複数人で同一ファイルの同じ個所を編集するとコンフリクト(競合)が発生する。以下はGitにおけるコンフリクトに関する問いである。

#### Q3: コンフリクトが起きた際の対応の手順を答えよ。また、回答は必ずカンマ区切りで入力すること。（回答例）A, B, C, D 

A. `$ git add`で編集したファイルをステージングエリアに置く

B. `$ git commit`と`$ git push`で変更を反映

C. `$ git status`でコンフリクトを起こしたファイルなどを確認

D. コンフリクトを起こしたファイルを開き、修正をした後で保存する

<br>

#### Q4: コンフリクトが起こらないようにする方法の説明として正しい選択肢を全て選べ。ただし、回答が複数ある場合はアルファベット順にカンマ区切りで回答すること。（回答例）A, C

A. ローカルのmainブランチを最新に保ち、そこからブランチを切る

B. 誰がどのファイルを編集するかを決めておく

C. なるべく多くのメンバーが同一ブランチで作業を行う

<br>

## Section 2

---

#### Q1: プロジェクトに参加し、既存のリポジトリを自分の環境に複製することになりました。そのときに使用するコマンドのうち、最も適切なものは次のうちどれか。ただし、リポジトリのURLは`https://hogehoge.backlog.com/git/fuga/test.git`であるとする。

A. `git merge https://hogehoge.backlog.com/git/fuga/test.git`

B. `git clone https://hogehoge.backlog.com/git/fuga/test.git`

C. `git create repository https://hogehoge.backlog.com/git/fuga/test.git`

D. `git pull https://hogehoge.backlog.com/git/fuga/test.git`

<br>

#### Q2: mainブランチから新しくyamada/testブランチを作成し、作成したブランチに移動するとき、最も適切なコマンドは次のうちどれか。

A. `git checkout -b yamada/test`

B. `git add yamada/test`

C. `git pull origin yamada/test`

D. `git merge yamada/test`

<br>

#### Q3: 作成したyamada/testブランチで新しいファイル(sample.txt)を作成し、リモートリポジトリに反映させるとき、以下の3つのコマンドを使用する順番を答えよ。また、回答は必ずカンマ区切りで入力すること。(例)A, B, C

A. `git add sample.txt`

B. `git push origin yamada/test`

C. `git commit -m "create sample.txt"`

<br>

#### Q4. 上記コマンド`git add sample.txt`実行後は、sample.txtは次のどこにあるか。

A. ワーキングエリア（作業ディレクトリ）

B. インデックス（ステージングエリア）

C. ローカルリポジトリ

<br>

#### Q5: yamada/testブランチはmainブランチにマージされたとする。不要になったyamada/testブランチを削除するコマンドは次のうちどれか。

A. `git branch -a yamada/test`

B. `git branch -b yamada/test`

C. `git branch -c yamada/test`

D. `git branch -d yamada/test`

<br>

#### Q6. リモートリポジトリとローカルリポジトリのmainブランチを同期させるためのコマンドは次のうちどれか。

A. `git pull origin main`

B. `git merge main`

C. `git sync main`

D. `git branch -m main`

<br>

以下はGitHubにて、リポジトリに対するプッシュやプルリクエストなどの特定の操作をトリガーとしてあらかじめ定義しておいた処理を実行する機能が備わっているGitHub Actionsに関する問いである。

#### Q7:GitHub Actionsで自動テスト等を行う際にはワークフローをyamlファイルに記述する必要がある。そのyamlファイルは次のうちどこに配置すればよいか。

A. .git

B. .github/workflows

C. workflows

D. workflows/yaml

<br>

#### Q8: mainブランチに更新があったときと、mainブランチに対するプルリクエストが作成された場合にテストを自動実行したい。そのために記述したyamlファイルが以下になる。ア、イに当てはまる文字をそれぞれ答えよ。

```
name: Test CI

on:
  push:
    branches: [ ア ]
  イ:
    branches: [ main ]

jobs:
  test:
    name: 自動テスト
    runs-on: ubuntu-latest
    env:
      SECRET_KEY: ${{ secrets.SECRET_KEY }}
    steps:
    - uses: actions/checkout@v2
    - name: Run Tests
      run: >
        docker-compose run
        --rm
        -e SECRET_KEY
        web python3 manage.py test
```
