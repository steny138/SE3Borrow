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
