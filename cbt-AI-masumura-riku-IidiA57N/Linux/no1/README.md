# 問1 Unixコマンドに関する知識問題

以下の5つの章からなる問題の答えを`answer.yaml`に記入してください．

## section1 基礎知識

### Q1: WindowsにおいてUnixコマンドを利用したCUI操作を行う方法として正しい選択肢を全て選べ。ただし、回答が複数ある場合はアルファベット順にカンマ区切りで回答すること。（回答例）A, C

---

#### 選択肢

A. Windows PowerShellを利用する

B. コマンドプロンプトを利用する

C. WSLやWSL2を利用する

### Q2: ターミナルにおける標準入力と標準出力の説明として正しい組み合わせを選べ．

---

#### 選択肢

|  選択肢  |  標準入力  |  標準出力 |
|:-:|:-:|:-:|
|  A  |  プログラムの標準的な入力であり，リダイレクトの際には `<` が使われる  |  プログラムの標準的な出力であり，リダイレクトの際には `>` が使われる  |
|  B  |  プログラムの標準的な入力であり，リダイレクトの際には `>` が使われる  |  プログラムの標準的な出力であり，リダイレクトの際には `<` が使われる  |
|  C  |  プログラムの標準的な入力であり，リダイレクトの際には `1>` が使われる  |  プログラムの標準的な出力であり，リダイレクトの際には `2<` が使われる  |
|  D  |  プログラムの標準的な入力であり，リダイレクトの際には `1<` が使われる  |  プログラムの標準的な出力であり，リダイレクトの際には `2>` が使われる  |

### Q3: 次のUnixコマンドとその**一般的な用法**を正しく対応させ，一つのコマンドに対し最も適切な一つの用法を記入せよ．

---

#### コマンド

A. cat

B. df

C. source

D. touch

E. wc

#### 用法

1. テキストを検索する
2. ディスク空き容量を確認する
3. ファイルやディレクトリを表示する
4. ファイルを作成する
5. ファイルの中身を表示する
6. プロセス情報を確認する
7. 単語数や行数を数える
8. 成功/失敗した場合に次の処理を行う
9. 現在のシェルでファイルを実行する

### Q4 次のシェルスクリプトは正常に実行されない．エラーの原因となる行とエラーの解消の組み合わせとして正しい選択肢を選べ．ただし，行は`arr=(1 2 3 4 5)`の行を1行目として数えるものとする．

```bash
arr=(1 2 3 4 5)
s=0
for v in "${arr[@]}"; do
    ((s=s+v))
done
if [ "$s" >= 10 ]; then
    echo "large"
else
    echo "small"
fi
```
---
#### 選択肢

|  選択肢  |  エラーの原因となる行  |  エラーの解消 |
|:-:|:-:|:-:|
|A|1|`arr=[1,2,3,4,5]`|
|B|1|`arr=(seq 1 5)`|
|C|4|`$s=$s+v`|
|D|6|`if [ $s >= 10]; then`|
|E|6|`if [ "$s" -ge 10]; then`|
### Q5 ターミナルにおける環境変数の説明として正しい選択肢を全て選べ。ただし、回答が複数ある場合はアルファベット順にカンマ区切りで回答すること。（回答例）A, C

---

#### 選択肢

A. 環境変数 PATH に登録した絶対パスで指定されるディレクトリ下に配置したバイナリファイルがコマンドとして実行可能となる

B. 全ての環境変数は現在のシェルのみで有効である

C. `~/.bash_profile` はログインしたときにのみ読み込まれる．

D. ディレクトリ `/bin` にはユーザーが作成したバイナリファイルが格納されている．

## section2 ファイル・ディレクトリの操作

### Q1: 次の操作を書かれている順に実行するために，各コマンドが何番目に実行されるかその番号を答えよ．

---

#### 操作

1. ホームディレクトリ直下に `test` フォルダを作成する
2. その `test` フォルダ内に `file_1.txt` を作成する
3. その `test` フォルダを `test.zip` としてzip化する
4. `test` フォルダを削除する
5. ホームディレクトリ下に更に `result/temp1` フォルダを作成する
6. `test.zip` を `result/temp1` フォルダ内に移動する

#### コマンド

A. `cd ..`

B. `cd test/`

C. `cd ~`

D. `mkdir -p result/temp1`

E. `mkdir test`

F. `mv test.zip result/temp1`

G. `rm -r test`

H. `touch file_1.txt`

I. `zip -r test.zip test`


### Q2: 次の操作を書かれている順に実行するために，各コマンドが何番目に実行されるかその番号を答えよ．

---

#### 操作

1. ホームディレクトリ直下に `project` というフォルダを作成する
2. `project` フォルダ内に `initialize.sh` を作成して `touch init.txt` と書き込む
3. `project` フォルダ内に `dirs` というフォルダを作成する．
4. `dirs` フォルダ内に `dir1`, `dir2`, ..., `dir5` のフォルダを作成し，それぞれのフォルダ`dir1`, `dir2`, ..., `dir5`から`initialize.sh`を実行する


#### コマンド

A. `cd ../../../`

B. `cd project/dirs/dir$i`

C. `cd ~`

D. `done` 

E. `echo "touch init.txt" > project/initialize.sh`

F. `for i in 1 2 3 4 5; do`

G. `mkdir project/dirs/dir$i`

H. `mkdir project/dirs`

I. `mkdir project`

J. `source ../../initialize.sh`

## section3 Linuxパイプライン

### Q1 `./results` フォルダ下の全てのファイル (サブディレクトリを含む) の合計の行数をカウントしたい．期待する動作をするシェルコマンドの選択肢を全て選べ。ただし、回答が複数ある場合はアルファベット順にカンマ区切りで回答すること。（回答例）A, C

---

#### 選択肢

A. `cat $(find ./results/* -type f) | find . | wc -l`

B. `cat $(find ./results/* -type f) | wc -l`

C. `du --all ./results/* | xargs cat | wc -l`

D. `find ./results/* -type f | xargs cat | wc -l`

E. `find ./results/* | xargs cat | wc -l`

### Q2 `./results` フォルダ以下のすべてのファイルのうち，ファイルサイズの大きい上位5つを表示したい．期待する動作をするシェルコマンドの選択肢を全て選べ。ただし、回答が複数ある場合はアルファベット順にカンマ区切りで回答すること。（回答例）A, C

#### 選択肢

A. `du -a ./results/* | sort -rn | head -n 5`

B. `du -a ./results/* | sort -rn | tac | head -n 5`

C. `find ./results/* -type f | xargs du | sort -rn | head -n 5`

D. `find ./results/* -size +1c | sort -n | tac | head -n 5`

### Q3 `./results` フォルダ下すべての`.log`で終わるログファイルのうち，作成日時が1週間以上前のログファイルを削除したい．期待する動作をするシェルコマンドの選択肢を全て選べ。ただし、回答が複数ある場合はアルファベット順にカンマ区切りで回答すること。（回答例）A, C

#### 選択肢

A. `find ./results/* -name "*\.log" -mtime 7 | xargs rm`

B. `find ./results/* -name "*\.log" -mtime +7 | xargs rm`

C. `find ./results/* -mtime +7 | grep "\.log" | xargs rm` 

D. `find ./results/* -name "*\.log" -mtime 7 -delete`

## section4 SSH

### 管理者側 問題

東進太郎さんは自宅からサーバーAにSSH接続するために以下の操作を操作を行う．
そのサーバーの管理者であるあなたは東進太郎さんからSSHの公開鍵`server_a.pub`を受け取った．
これからあなたは，新規のユーザー `taro.toshin` を作成し，東進太郎さんがSSHでアクセスできるようにセットアップを行う必要がある．
セットアップの手順に関して以下の問に答えよ．

---

### Q1 東進太郎さんから公開鍵`server_a.pub`を受け取ったあとあなたは何をすべきか．正しい答えを全て選べ。ただし、回答が複数ある場合はアルファベット順にカンマ区切りで回答すること。（回答例）A, C

---

#### 選択肢

A. `.ssh/authorized_keys` に公開鍵を登録する

B. `server_a.pub`の中身の先頭にある文字列`ssh-rsa`は以降の操作で不要なので削除する．

C. `ssh-keygen`コマンドで公開鍵・秘密鍵を新たに生成し，新たに生成した公開鍵を東進太郎さんに送信する

D. `useradd`コマンドで新規のユーザー`taro.tohsin`を作成する


### Q2 あなたは`TaroToshin`という誤った名前のユーザーを作成してしまったのでこのユーザーを削除したい．入力するべきコマンドは次のうちどれか一つ答えよ．

---

#### 選択肢

A. `sudo rm -r /home/TaroToshin && sudo sed /^TaroToshin/d /etc/group > /etc/group`

B. `sudo rm -r /home/TaroToshin && sudo sed /^TaroToshin/d /etc/passwd > /etc/passwd`

C. `sudo rm -r /home/TaroToshin`

D. `sudo userdel TaroToshin`
### 利用者側 問題

あなたはオフィスPCにSSH接続するために以下の操作を行う．ただし，「管理者側 問題」の問題文の手順に従ってあなたは`server_a.pub`として公開鍵を送信し，サーバーAはSSH接続する準備が完了しているとする．
あなたはSSH接続を試みて`ssh`コマンドを入力したものの，エラーメッセージが表示された．それぞれのエラーメッセージに関して，次の問に答えよ．

### Q3 エラーメッセージが`Permission denied (publickey)`である場合に，考えられる操作として不適切な選択肢を一つ答えよ．

---

#### 選択肢

A. `chmod`コマンドにより`server_a`の秘密鍵を適切な権限に変更する

B. `sudo`コマンドでSSH接続を試みる

C. ログインするホスト名とユーザー名が正しいか確認する

D. 秘密鍵と公開鍵のキーペアが正しいか確認する

### Q4 エラーメッセージが`'/home/taro.toshin/.ssh/server_a' are too open`と表示されたため，このファイルの権限を変更したい．最も適切な操作は次のうちどれか答えよ．なお`server_a`の権限は次の通りであった．
`-rw-r--r-- 1 taro.toshin taro.toshin 2655 Feb 26 15:07 server_a` 

---
#### 選択肢

A. `sudo chmod 000 ~/.ssh/server_a`

B. `sudo chmod 600 ~/.ssh/server_a`

C. `sudo chmod 777 ~/.ssh/server_a`

D. `sudo chown 000 ~/.ssh/server_a`

E. `sudo chown 600 ~/.ssh/server_a`

F. `sudo chown 777 ~/.ssh/server_a`


## sectoin5 Processes

### Q1 処理に時間のかかるプログラム main.py をssh先のサーバーで実行したが、これから回線工事が始まるので処理を続けたままログアウトしたい．次の空欄に当てはまる語に対応するコマンドをそれぞれ答えよ

#### 問題文

まず，(A) で実行中の main.py を停止する．(B)によってジョブの状態を表示させたところ，次の通りであった．

```shell
  [1]-  Stopped                 man exec
  [2]+  Stopped                 python3 main.py
```

この状態に対して (C) を実行することで main.py はバックグラウンドで実行させることができる． 最後に (D) によって main.py をデーモンプロセスとすることで処理は完了する．

#### 選択肢

1. `Ctrl + C`
2. `Ctrl + Z`
3. `kill main.py`
4. `jobs`
5. `ps aux`
6. `ps`
7. `bg %2`
8. `bg main.py`
9. `fg %2`
10. `fg main.py`
11. `disown %1`
12. `disown %2` 
13. `disown main.py`

### Q2 `./csv/` 下の全csvに対して、`process.py` (コマンドライン引数 `-p` にcsvを指定する)を実行することでcsvの整形を行いたい. pcのメモリの関係上、20プロセス並列で`process.py`を実行したい．次のシェルスクリプトを読んで空欄に当てはまる適切な選択肢を答えよ．

```bash
i=0
files=$(find ./csv/*.csv -type f)
for file in ${files[@]}; do
  i=$((i += 1))
  python3 process.py -p ${file} (空欄A)
  if [ $((i % 20)) -eq 0 ]; then
    (空欄B)
  fi
done

```

### 空欄A 選択肢

A. `&`

B. `$`

C. `-p`

D. `--thread`

### 空欄B 選択肢

A. `respawn`

B. `sleep 10`

C. `wait`

D. `wait %19`
