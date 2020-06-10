"""
Django settings for propertyManagement project.

Generated by 'django-admin startproject' using Django 3.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
# import django_heroku

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))



# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = 'r6ta9=p6f_$+)*$cjc#3og24sno96z-m2xo)!b2bn8x1@36k0f'
SECRET_KEY = os.getenv('SECRET_KEY', default='r6ta9=p6f_$+)*$cjc#3og24sno96z-m2xo)!b2bn8x1@36k0f')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    'https://basemera-property-management.herokuapp.com',
    'basemera-property-management.herokuapp.com',
    'localhost',
    'ec2-3-16-148-152.us-east-2.compute.amazonaws.com',
    'ec2-18-216-84-128.us-east-2.compute.amazonaws.com',
    
]

AUTH_USER_MODEL = 'user.User'

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'role',
    'user',
    'graphene_django',
    'permissions',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',

]

ROOT_URLCONF = 'propertyManagement.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'propertyManagement.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

# DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    # }
#     'ENGINE': 'django.db.backends.mysql',
#         'OPTIONS': {
#             'read_default_file': os.path.join(BASE_DIR, '.env'),
#         },
#     }
# }

 
# DATABASES = {
    # 'default': {
        # 'ENGINE': 'django.db.backends.mysql',
        # 'NAME': 'new_user@properties;',
        # 'NAME' : 'properties',
        # 'alias' : 'properties',
        # 'USER': 'new_user',
        # 'PASSWORD': 'root',
        # 'HOST' : 'localhost',
        # 'HOST': '/Applications/MAMP/tmp/mysql/mysql.sock',
        # 'PORT': '8889',
        # 'OPTIONS': {
        # 'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"
#         }
#     }
# }

DATABASES = {
    'default': {
        # 'ENGINE': 'django.db.backends.mysql',
        'ENGINE' : os.environ.get('ENGINE', 'django.db.backends.postgresql'),
        # 'NAME': 'new_user@properties;',
        # 'NAME' : 'properties',
        'NAME' : os.environ.get('DB_NAME', 'enju-properties'),
        # 'alias' : 'properties',
        # 'USER': 'new_user',
        'USER' : os.environ.get('DB_USER', 'postgres'),
        # 'PASSWORD': 'root',
        'PASSWORD' : os.environ.get('DB_PASSWORD', 'Welcome123!'),
        # 'HOST' : 'localhost',
        'HOST' : os.environ.get('DB_HOST', 'enju-properties.c5l67bhqsieq.us-east-2.rds.amazonaws.com'),
        # 'HOST': '/Applications/MAMP/tmp/mysql/mysql.sock',
        # 'PORT': '8889',
        'PORT' : os.environ.get('DB_PORT', '5432'),
        'OPTIONS': {
        # 'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"
        }
    }
}


if os.environ.get('GITHUB_WORKFLOW'):
    DATABASES = {
        'default': {
           'ENGINE': 'django.db.backends.mysql',
           'NAME' : 'properties',
           'USER': 'new_user',
           'PASSWORD': '',
           'HOST': 'localhost',
           'PORT': '8889',
        }
    }

    if os.environ.get('test'):
        DATABASES = {
        'default': {
           'ENGINE': 'django.db.backends.mysql',
           'NAME': 'test_properties',
           'USER': 'new_user',
           'PASSWORD': '',
           'HOST': '127.0.0.1',
           'PORT': '8889',
        }
    }

# DATABASES = {
#     'default': {
#         'ENGINE': os.getenv('ENGINE', default='django.db.backends.postgresql_psycopg2'),
#         'NAME': os.getenv('DB_NAME',default='property_management'),
#         'USER': os.getenv('DB_USER',default='root'),
#         'PASSWORD': os.getenv('DB_PASSWORD', default='root'),
#         'HOST': os.getenv('HOST', default='/Applications/MAMP/tmp/mysql/mysql.sock'),
#         'PORT': '8889',
#     }
# }

# DATABASES = {
#     'default': {
#         'ENGINE': os.getenv('ENGINE', default='django.db.backends.mysql'),
#         'NAME': os.getenv('DB_NAME',default='property_management'),
#         'USER': os.getenv('DB_USER',default='property'),
#         'PASSWORD': os.getenv('DB_PASSWORD', default='root'),
#         'HOST': os.getenv('HOST', default='/Applications/MAMP/tmp/mysql/mysql.sock'),
#         'PORT': '8889',
#     }
# }

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/
# STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATIC_URL = '/static/'

# STATICFILES_DIRS = (
#     os.path.join(BASE_DIR, 'static'),
# )

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


GRAPHENE = {
    'SCHEMA': 'propertyManagement.schema.schema',
}

# django_heroku.settings(locals())
