from django.urls import path

from menu.views import IndexPageView

urlpatterns = [
    path('menu', IndexPageView.as_view(), name='menu')
]