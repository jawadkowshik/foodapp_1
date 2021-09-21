from django.contrib import admin
from django.urls import path
from customer.views import Index, About, Order, Login, Register
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Index.as_view(), name='index'),
    path('about/', About.as_view(), name='about'),
    path('order/', Order.as_view(), name='order'),
    path('login/', Login.as_view(), name='login'),
    path('register/', Register.as_view(), name='register'),

] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)