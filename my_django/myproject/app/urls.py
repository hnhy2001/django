from django.urls import path,include
from . import views
from rest_framework.routers import  DefaultRouter

router = DefaultRouter()
router.register('customer', views.CustomerViewSet)
router.register('oder', views.OderViewSet)


urlpatterns = [
    path('', views.index, name="index"),
    path('test/', views.TestView.as_view()),
    path('', include(router.urls)),
]