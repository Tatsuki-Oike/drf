## 1 仮想環境

```sh
cd ./07_jwt/backend
python3 -m venv venv
source venv/bin/activate
python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt
```

## 2 Djangoプロジェクト

* プロジェクト作成

```sh
django-admin startproject jwt_proj
cd ./jwt_proj
python3 manage.py startapp jwt_app
```

* migration

```sh
python3 manage.py migrate
```

* スーパーユーザー作成

```sh
python manage.py createsuperuser
python3 manage.py runserver
```
