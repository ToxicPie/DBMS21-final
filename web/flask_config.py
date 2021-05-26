import secrets

DEBUG = True
TEMPLATES_AUTO_RELOAD = True

SECRET_KEY = secrets.token_bytes(32)
