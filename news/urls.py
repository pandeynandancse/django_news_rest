from django.contrib import admin
from  django.urls import path
from django.urls.conf import include
from news import views
from django.views.generic.base import RedirectView
from rest_framework import routers



router = routers.DefaultRouter()
router.register(r'newss',views.NewsViewSet)

urlpatterns = [
	path(r'api/',include(router.urls)),
	path(r'',RedirectView.as_view(url='api/')),
	# path('status/', views.index),

]