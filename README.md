# SE3 租借系統
租借Sim卡，從這裡開始。

## 預先安裝

1. Python
2. django
3. django.bootstrap3
4. python-psycopg2(postgresql)

## 操作說明

### PostgreSql
#### 操作指令(Mac)
* 啟動(背景)：pg_ctl -D /usr/local/var/postgres -l /usr/local/var/postgres/server.log start
* 關閉：pg_ctl -D /usr/local/var/postgres stop -s -m fast
* 新增資料庫使用者：createuser -s -P <username>
	> -s superuser
	> -P 自訂密碼
* 移除使用者：dropuser <username>
* 新增資料庫：createdb <dbname>

### Django

* 新增專案： django-admin.py startproject <project name>
* 新增功能： django-admin.py startapp <app name>
	這個是泛指某一塊功能ex:登入功能
* 調整 settins.py
``` 
INSTALLED_APPS = (
'django.contrib.admin',
'django.contrib.auth',
'django.contrib.contenttypes',
'django.contrib.sessions',
'django.contrib.messages',
'django.contrib.staticfiles',
'<app name>',
)
```
* 修改資料庫： 使用postgresql
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': <database name>,
        'USER': <user name>,
        'PASSWORD': <password>,
        'HOST': '',
        'PORT': '',
    }
}
```
* 修改資料庫： sqlite
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
```

* 建立對應： python manage.py makemigrate
* 建立資料表： python manage.py migrate
* 啟動：python manage.py runserver

---
Web 框架
### bootstrap
* 安裝django.bootstrap3: pip install django.bootstrap3

* 在html 放上以下程式段，就會直接載入相關css,js檔案
```
{# Load the tag library #} 
{% load bootstrap3 %} 

{# Load CSS and JavaScript #} 
{% bootstrap_css %} 
{% bootstrap_javascript %} 

{# Display django.contrib.messages as Bootstrap alerts #} 
{% bootstrap_messages %}
```
* bootstrap相依 jquery

---

 ##### 關於映射model to database
1. 建立準備映射的檔案到migrations資料夾 
	```
	python manage.py makemigrations
	```
 	
2. 產生映射
	```
	python manage.py migrate
	```
3. 找不到auth_user

	```
	python manage.py migrate auth
	```
	再執行 python manage.py migrate 就好
---

### Django Project Deploy To Heroku Platform With Github.
1. 先準備heroku要看的發布設定檔 "Procfile" 檔名就是這樣 沒有附檔名!沒有附檔名!沒有附檔名!
並輸入以下內容
```
web: gunicorn myproject.wsgi --log-file -
```

> 參考用: foreman 可以讓你local 去執行你要建立在Heroku的app
> Gunicorn是一个高效的Python WSGI Server,通常用它執行wsgi application

2. 相關安裝項目參考
```
dj-database-url==0.4.2
Django==1.8.18
django-bootstrap3==8.2.3
gunicorn==19.7.1
psycopg2==2.7.1
pytz==2017.2
whitenoise==3.3.0

pip freeze > requirements.txt
```

3. 準備runtime.txt 指定heroku 運行的python version
文件內輸入以下內容
```
python-2.7.13
```

4. settings.py
```
# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

import dj_database_url

db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'staticfiles')
STATIC_URL = '/static/'

# Extra places for collectstatic to find static files.
STATICFILES_DIRS = (
    os.path.join(PROJECT_ROOT, 'static'),
)

# SIMPLIFIED STATIC FILE SERVING.
# HTTPS://WAREHOUSE.PYTHON.ORG/PROJECT/WHITENOISE/
STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'
```

5. wsgi.py
```
import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "se3_borrows.settings")

from whitenoise.django import DjangoWhiteNoise


application = DjangoWhiteNoise(get_wsgi_application())
```

!注意 ```from whitenoise.django import DjangoWhiteNoise``` 必須要在
```os.environ.setdefault("DJANGO_SETTINGS_MODULE", "se3_borrows.settings")```
的下一行，不然會web crash


6. 相關 heroku指令
```
$ heroku login
$ git push heroku master
$ heroku open

$ heroku run python manage.py migrate auth
$ heroku run python manage.py makemigrations
$ heroku run python manage.py migrate

$ heroku run python manage.py createsuperuser
$ heroku git:clone -a myapp
```

