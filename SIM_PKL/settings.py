import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'y&ma&g0z0r603*p2qz9^hotn**h60eey1w2kwb)glz#sdtt8&)'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']
# ALLOWED_HOSTS = [
#    'labsosv2.herokuapp.com',
#    'localhost',
# ]



# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'crispy_forms',
    'bootstrap_datepicker_plus',
    'accounts',
    'home',
    'dosen',
    'mahasiswa',
    'catatan',
    'mitra',
    'forum',
    'countable_field',
    'crispy_bootstrap4',
    'rest_framework',
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

ROOT_URLCONF = 'SIM_PKL.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR + '/templates',
        ],
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
CRISPY_TEMPLATE_PACK = 'bootstrap4'
WSGI_APPLICATION = 'SIM_PKL.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
        'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        # 'NAME': 'd5clsp00utpdqc',
        # 'PORT': '5432',
        # 'NAME': 'd5clsp00utpdqc',
        # 'USER': 'jzehigmazjuqsl',
        # 'PASSWORD': '4e051db742ca832a67976573b69c689bbf409c444983343506f29fe1565f7d29',
        # 'HOST': 'ec2-52-6-75-198.compute-1.amazonaws.com',

        'NAME': 'labsosv2',
        # 'USER': 'postgres',
        # 'PASSWORD': 'tatam123',
        # 'HOST': 'localhost',
        # 'PORT': '5432',
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'id-idn'

TIME_ZONE = 'Asia/Jakarta'

USE_I18N = True

USE_L10N = True

USE_TZ = True

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'hatami391998@gmail.com'
EMAIL_HOST_PASSWORD = 'istimewajogja123'


#message verifikasi account
HTML_MESSAGE_TEMPLATE = "/templates/email_messages.html"

VERIFICATION_SUCCESS_TEMPLATE = "/templates/succes_verifikasi.html"

VERIFICATION_FAILED_TEMPLATE = "/templates/failed_verifikasi.html"
SUBJECT = 'Email Verification Mail'


STATIC_URL = '/static/'

STATICFILES_DIRS =[
    BASE_DIR + "/static",
    'var/www/static',
]
MEDIA_ROOT =  os.path.join(BASE_DIR, 'media') 
MEDIA_URL = '/media/'

BOOTSTRAP4 = {
    'include_jquery': True,
}
DEFAULT_AUTO_FIELD='django.db.models.AutoField' 

from django.contrib.messages import constants as messages

MESSAGE_TAGS ={
    messages.DEBUG : 'alert-info',
    messages.INFO : 'alert-info',
    messages.ERROR : 'alert-danger',
    messages.SUCCESS : 'alert-success',
    messages.WARNING : 'alert-warning',
}