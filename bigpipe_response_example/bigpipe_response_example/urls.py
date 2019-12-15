"""bigpipe_response_example URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from django.views.i18n import JavaScriptCatalog

from bigpipe_response.bigpipe import Bigpipe
from .views import view_demo


urlpatterns = [
    # path('admin/', admin.site.urls),

    path('', view_demo.demo, name='demo'),
    path('demo', view_demo.demo, name='demo main'),
    path('demo/news_feed', view_demo.news_feed, name='news_feed'),
    path('demo/navigation_menu', view_demo.navigation_menu, name='demo_pagelet_navigation'),
    path('demo/information_boxes', view_demo.information_boxes, name='information_boxes'),
    path('demo/top_blue_bar', view_demo.top_blue_bar, name='demo_pagelet_top_blue_bar'),


    path('jsi18n', JavaScriptCatalog.as_view(), name='javascript-catalog'),
]
