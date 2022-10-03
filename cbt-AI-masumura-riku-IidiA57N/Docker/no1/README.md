# 問1

以下の問題に対する答えをyamlファイルに記載してください。

## Section1：Dockerの基本

---

#### Q1: コンテナ型仮想化ソフトウェアであるDockerに関する説明として正しいものにはTを、誤ったものにはFを記入せよ。

A. コンテナはマイクロサービスと相性が良い

B. コンテナは実行環境ごとにパッケージ化するため、開発環境と本番環境で同じようにアプリケーションを動作させることができる

C. コンテナはホストOSを共有しているため、OSのバージョンの違いや互換性次第では正しく動作しない場合がある

D. 名前空間(namespace)の仕組みを利用して、コンテナは外部から隔離されている

E. コンテナを削除してもコンテナ上のデータは削除されない

F. コンテナイメージに含まれるファイルシステムに差分管理の仕組みを利用しているため、高速なデプロイが可能である

<br>

#### Q2: 次のDocker instructionの説明として正しいものをそれぞれ回答せよ。

FROM, RUN, CMD, ENV, ADD, COPY, WORKDIR

ア. ローカルにあるファイル、ディレクトリや、リモートにあるファイルなどをイメージのファイルシステム上に追加する。追加したいものがローカルにあり、無圧縮、gzip、gzip2、xzのいずれかの圧縮形式のtarファイルである場合は、ディレクトリとして展開する。

イ. ローカルにあるファイルやディレクトリをイメージのファイルシステム上に追加する。

ウ. 新しいbuild stageを初期化して、以降の命令で使うベースイメージを指定する。

エ. Dockerfile内で以降に続くコマンドの処理時に使う作業ディレクトリを指定する。

オ. 現在のイメージよりも上にある新しいレイヤでコマンドを実行し、その結果をcommitする。

カ. 環境変数を設定する。この値はそれ以降のbuild stageで環境変数として保持される。

キ. コンテナ起動時のデフォルトコマンドを指定する。

## Section2：Dockerfile
以下に示すDockerfileを元にDocker imageとコンテナの作成を行なった。次に問いに答えよ。
ただし、以下のDockerfileは理解を問うために作成されたものであるため、実際にはこのようなDockerfileの書き方は推奨されない。

---

```Dockerfile
FROM python:3.9-buster

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir code
RUN cd /code
RUN touch test1.txt

RUN python3 -m pip install --upgrade pip setuptools

WORKDIR /code
RUN touch test2.txt
RUN ls > test2.txt
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . ./
RUN touch test3.txt
RUN ls > test3.txt

RUN touch test4.txt test5.txt
RUN chmod 764 test4.txt
RUN ls -l > test5.txt

EXPOSE 8000

ENTRYPOINT ["echo","This is ENTRYPOINT"]
CMD ["echo", "This is CMD"]
```

### Q1. コンテナ内のtext1.txtとrequirements.txtはどこのディレクトリ直下にあるか、以下の選択肢の中から適切なものをそれぞれ選べ。

ア. /
イ. /bin
ウ. /code

### Q2: コンテナ内のtest2.txt, test3.txtの中身として適切なものを以下より全て選べ。ただし、ファイルの中身が空の場合は「空」と解答せよ。ただし、複数個解答する場合はあいうえお順にカンマ区切りで回答せよ。(例)ア,ウ,オ

ア. test1.txt
イ. test2.txt
ウ. test3.txt
エ. test4.txt
オ. test5.txt
カ. code
キ. requirements.txt
ク. Dockerfile

### Q3: コンテナ内のtest4.txtにおいて、所有グループに与えられている権限として最も適切なものを以下より選べ。

ア. 読み取り+実行
イ. 読み取り+書き込み+実行
ウ. 読み取り+書き込み
エ. 読み取り

### Q4: Dockerfileが配置されているディレクトリ上で以下のコマンドを順に打ったときの出力を答えよ。

`docker build -t test_image .`
`docker run -it test_image bash`

## Section3：Docker Compose
docker-compose を用いて、Django + Postgresアプリの開発環境を構築したい。その際に使用する以下の`docker-compose.yaml`と`Dockerfile`, Djangoの設定が記載されている`settings.py`について、空欄を埋めなさい。フォルダ構成は以下のようになっているものとする。オについては、数字で回答せよ。

【フォルダ構成】
```
.
├── docker-compose.yml
├── sample_app
│   ├── __init__.py
|   ├── settings.py
|   ├── urls.py
|   └── wsgi.py
├── manage.py
├── Dockerfile
└── requirements.txt
```

【Dockerfile】
```Dockerfile
FROM python:3.9
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip install -r requirements.txt
ADD . /code/
```

【docker-compose.yaml】
```docker-compose.yaml
version: '3'

services:
  sample_db:
    image: postgres:12
    environment:
      - POSTGRES_DB=(ア)
      - POSTGRES_USER=(イ)
      - POSTGRES_PASSWORD=(ウ)
    ports:
      - "5432"
  sample_web:
    build: .
    command: python3 manage.py runserver 0.0.0.0:8000
    volumes:
      - .:/code
    ports:
      - "8000:8000"
    depends_on:
      - (エ)
```

【settings.py】
```python
# ...略
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'test-user',
        'PASSWORD': 'somepassword',
        'HOST': 'db',
        'PORT': (オ),
    }
}
# ...略
```
