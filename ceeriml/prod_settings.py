STATIC_ROOT = os.path.join(BASE_DIR,'staticfiles')



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'master',
        'USER': 'mlceeri',
        'PASSWORD': 'summerof69',
        'HOST': 'mlceeri.mysql.pythonanywhere-services.com',
        'PORT': '',
    }
}