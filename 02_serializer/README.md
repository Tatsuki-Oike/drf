## 1 仮想環境

```sh
cd ./02_serializer
python3 -m venv venv
source venv/bin/activate
python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt
```

## 2 Djangoプロジェクト

* プロジェクト作成

```sh
django-admin startproject serializer_proj
cd ./serializer_proj
python3 manage.py startapp serializer_app
```

* migration

```sh
python3 manage.py makemigrations serializer_app
python3 manage.py migrate
```

* サーバーの起動

```sh
python3 manage.py runserver
```

## 3 テスト

新しいターミナルに移動

```sh
cd ./02_serializer
source venv/bin/activate
python3 request.py
```
