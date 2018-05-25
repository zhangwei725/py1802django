import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = '98220o6prt=^o)y0)@$@*ujte&yx)_-ujvd1j04px0($beb+$%'

DEBUG = True

ALLOWED_HOSTS = []

# 当我们创建app(项目功能模板//用户模块 设置模块,首页模块(门户模块))
INSTALLED_APPS = [
    'django.contrib.admin',  # 系统内置的站点管理模块
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'hello.apps.HelloConfig',
    'model01',
    'model02',
    'model03.apps.Model03Config',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'djangodemo.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'djangodemo.wsgi.application'

"""
大型的关系数据库     oracle(oracle) DB2(ibm)  Sybase
中型的关系型数据库   mysql   postgreSql  sql Server
小型的关系型数据     sqlite3   Access
"""
# ctrl +shift +u  大小切换
DATABASES = {
    'default': {
        # 支持的关系型数据
        'ENGINE': 'django.db.backends.mysql',
        # 'ENGINE': 'django.db.backends.oracle',
        # 'ENGINE': 'django.db.backends.sqlite3',
        # 'ENGINE': 'django.db.backends.postgresql',
        # 数据的名称
        # 'NAME': 'django',
        # 'USER': 'root',
        # 'PASSWORD': 'root',
        # 'HOST': '127.0.0.1',
        # 'PORT': '3306',
        # 'CHARSET': 'utf8'
        'OPTIONS': {
            'read_default_file': 'config/db.cnf'
        }
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]
# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/
# 修改成中文
LANGUAGE_CODE = 'zh-hans'
# 亚洲 上海
TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django.db.backends': {
            'handlers': ['console'],
            'propagate': True,
            'level': 'DEBUG',
        },
    }
}
