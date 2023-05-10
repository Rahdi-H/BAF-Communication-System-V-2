"""signal_center URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from unit import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('login/', views.loginn, name='login'),
    path('logout/', views.logoutt, name='logout'),
    path('in-los/', views.in_los, name='in-los'),
    path('in-crpt/', views.in_crpt, name='in-crpt'),
    path('out-los/', views.out_los, name='out-los'),
    path('out-crpt/', views.out_crpt, name='out-crpt'),
    # path('dispatch/add/', views.DispCreateView.as_view(), name='dispatch-add'),
    path('dispatch/<str:ref>/', views.dispatch, name='dispatch'),
    path('out-los/add/', views.LosCreateView.as_view(), name='los-add'),
    path('out-crpt/add/', views.CrptCreateView.as_view(), name='crpt-add'),
    path('out-los/update/<int:pk>/', views.LosUpdateView.as_view(), name='los-update'),
    path('out-crpt/update/<int:pk>/', views.CrptUpdateView.as_view(), name='crpt-update'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)