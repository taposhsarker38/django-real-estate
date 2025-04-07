from .base import *

DATABASES={
   'default':{
      'ENGINE':env("POSTGRES_ENGINE"),
      'NAME': env("DB_NAME"),
      'USER': env("DB_USER"),
      'PASSWORD':env("DB_PASSWORD"),
      'HOST': env("DB_HOST"),
      'PORT': env("DB_PORT"),
   }
}