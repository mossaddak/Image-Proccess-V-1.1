from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    #account
    path('api/', include("account.urls")),

    #password recovery
    path('api/', include("recovery_account.urls")),

    #app
    path('api/app/', include("app.urls")),

    #payment
    path('api/payment-method/', include("payment_method.urls")),

    
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
