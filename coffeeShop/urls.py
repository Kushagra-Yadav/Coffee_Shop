from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from coffeeItems.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('coffee/',Home),
    path('pricing/',Pricing),
    path('register/',SignIn),
    path('login/',LogIn),
    path('FAQs/',FrequentlyAskedQuestion),
    path('AboutUs/',AboutUs),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)