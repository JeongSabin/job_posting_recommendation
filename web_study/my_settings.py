#my_settings.py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', #1
        'NAME': 'test', #2
        'USER': 'root', #3
        'PASSWORD': 'password',  #4
        'HOST': 'localhost',   #5
        'PORT': '3306', #6
    }
}
SECRET_KEY ='django-insecure-(sgk3v4&_ux-mg%_02gbdzd1%bz!nfo(mzy1#u*bjj=pnao3ec'