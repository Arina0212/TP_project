from django.urls  import path, re_path


from .views import *


app_name = 'polls'
urlpatterns = [
    path('', about, name='UX/UI дизайнер'),
    path('demand/', demand, name='Востребованность'),
    path('geografy/', geografy, name='География'),
    path('skillvac/', skillvac, name='Навыки'),
    path('lastvacv/', lastvacv, name='Последние вакансии'),
]
