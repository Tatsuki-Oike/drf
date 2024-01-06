## 1 仮想環境

```sh
cd ./05_vue/backend
python3 -m venv venv
source venv/bin/activate
python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt
```

## 2 Djangoプロジェクト

* プロジェクト作成

```sh
django-admin startproject vue_proj
cd ./vue_proj
python3 manage.py startapp vue_app
```

* サーバー起動

```sh
python3 manage.py runserver
```