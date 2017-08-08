from os import environ

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "moztrap",
        "USER": "moztrap",
        "HOST": environ.get("MYSQL_PORT_3306_TCP_ADDR", ""),  # empty string == localhost
        "PASSWORD": environ.get("MYSQL_ENV_MYSQL_ROOT_PASSWORD","000000"),
        "STORAGE_ENGINE": "InnoDB",
        "OPTIONS": {
            "init_command": "SET default_storage_engine=InnoDB"
        }
    }
}

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
    }
}

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
DEFAULT_FROM_EMAIL = environ.get("DEFAULT_FROM_EMAIL","localhost")
EMAIL_HOST = environ.get("EMAIL_HOST","localhost")
EMAIL_PORT = environ.get("EMAIL_PORT",25)
EMAIL_HOST_USER = environ.get("EMAIL_HOST_USER","")
EMAIL_HOST_PASSWORD = environ.get("EMAIL_HOST_PASSWORD","")
EMAIL_SUBJECT_PREFIX = "[MozTrap]"
EMAIL_USE_TLS = environ.get("EMAIL_USE_TLS",False)

USE_BROWSERID = False
