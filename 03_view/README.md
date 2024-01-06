## 1 仮想環境

```sh
cd ./03_view
python3 -m venv venv
source venv/bin/activate
python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt
```

## 2 Djangoプロジェクト

* プロジェクト作成

```sh
django-admin startproject view_proj
cd ./view_proj
python3 manage.py startapp view_app
```

* migration

```sh
python3 manage.py makemigrations view_app
python3 manage.py migrate
```

* サーバーの起動

```sh
python3 manage.py runserver
```

## 3 テスト

新しいターミナルに移動

```sh
cd ./03_view
source venv/bin/activate
python3 request.py
```
