## 1 仮想環境

```sh
cd ./04_relational
python3 -m venv venv
source venv/bin/activate
python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt
```

## 2 Djangoプロジェクト

* プロジェクト作成

```sh
django-admin startproject relational_proj
cd ./relational_proj
python3 manage.py startapp relational_app
```

* migration

```sh
python3 manage.py makemigrations relational_app
python3 manage.py migrate
```

* サーバーの起動

```sh
python3 manage.py runserver
```

## 3 テスト

新しいターミナルに移動

```sh
cd ./04_relational
source venv/bin/activate
python3 request.py
```
