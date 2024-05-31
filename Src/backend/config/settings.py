"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 5.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""
from datetime import timedelta
from pathlib import Path
import environ
import os

from django.urls import reverse_lazy

env = environ.Env(
    DEBUG=(bool,False)
)
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
# Take environment variables from .env file
environ.Env.read_env(
    env_file = os.path.join(BASE_DIR, '.env'))


SECRET_KEY = "SECRET_KEY"
DEBUG = True
# Set the project base directory




# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!

# SECURITY WARNING: don't run with debug turned on in production!

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    "rest_framework", #rest framework를 사용할 것이라 알림
    "rest_framework_simplejwt", # 인증 관련
    "rest_framework.authtoken",# 인증 관련
    "dj_rest_auth", # 인증 관련
    'dj_rest_auth.registration', # 인증 관련
    'allauth', # 인증 관련
    'allauth.account', #인증 관련
    'corsheaders', #front 통신 관련

    # 앱
    'accounts',  # 유저 정보 관련 기능
    "mainpage", # 메인페이지 관련 기능
    "bookmark", # 북마크 관련 기능
    "crawling"
]

REST_USE_JWT = True #jwt 사용 여부
JWT_AUTH_COOKIE = 'accounts-auth' # 호출할 cookie key 값
JWT_AUTH_REFRESH_COOKIE = 'accounts-refresh-token' # refresh token cookie key 값
# JWT_SECRET_KEY 설정 추가
JWT_SECRET_KEY = env('JWT_SECRET_KEY')

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=15),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
}




REST_FRAMEWORK = {
    # 토큰을 통한 인증을 기본 인증 클래스로
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    # 승인된 사람이 아니면 페이지에 들어갈 수 없다
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    )


}

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    'allauth.account.middleware.AccountMiddleware',
]
REST_AUTH = {
   "REGISTER_SERIALIZER":"accounts.serializers.CustomRegisterSerializer",
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=15),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
}

SITE_ID = 1
ACCOUNT_USER_MODEL_USERNAME_FIELD = 'username' # User 모델의 username 변경 x
ACCOUNT_EMAIL_REQUIRED = False          # email 필드 사용 x
ACCOUNT_USERNAME_REQUIRED = True        # username 필드 사용 o
ACCOUNT_AUTHENTICATION_METHOD = 'username'
ACCOUNT_EMAIL_VERIFICATION = 'none' # 회원가입 과정에서 이메일 인증 사용 X

# CORS 설정 추가
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",  # 프론트엔드 도메인
    "http://127.0.0.1:4040",
    "http://127.0.0.1:8000",
    # 실제 배포 도메인 추가
]

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE':'django.db.backends.mysql',
        'NAME': env("DB_NAME"),
        'USER': env("DB_USER"),
        'PASSWORD': env("DB_PASSWORD"),
        'HOST': env("DB_HOST"),
        'PORT': env("DB_PORT"),
    }
}

# pymysql을 MySQLdb로 대체
import pymysql
pymysql.install_as_MySQLdb()


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = "ko-kr"

TIME_ZONE = "Asia/Seoul"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = "/static/"
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

AUTH_USER_MODEL = 'accounts.CustomUser'
#django sites app setting
# 미디어 파일이 저장될 디렉토리 경로 설정
# MEDIA_URL = '/media/'
# MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


LOGIN_URL = reverse_lazy('accounts/login/')


CORS_ORIGIN_WHITELIST = ('http://127.0.0.1:3000', 'http://localhost:3000', "http://127.0.0.1:8000",)
CORS_ALLOW_CREDENTIALS = True

CORS_ALLOW_ALL_ORIGINS = True #(모든 포트 허용)
CORS_ALLOW_METHODS = (
"DELETE",
"GET",
"OPTIONS",
"PATCH",
"POST",
"PUT",
)