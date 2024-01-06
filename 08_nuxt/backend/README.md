## 1 仮想環境

```sh
cd ./08_nuxt/backend
python3 -m venv venv
source venv/bin/activate
python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt
```

## 2 Djangoプロジェクト

* プロジェクト作成

```sh
django-admin startproject login_proj
cd ./login_proj
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
