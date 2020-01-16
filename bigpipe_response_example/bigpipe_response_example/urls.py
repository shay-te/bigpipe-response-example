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

from .views import view_landing
from .views import view_demo_piping
from .views import view_demo_multi_framework


from django.urls import path
from django.views.i18n import JavaScriptCatalog


urlpatterns = [
    path('admin/', admin.site.urls),

    path('', view_demo_piping.demo_piping, name='demo main'),
    path('landing', view_landing.demo, name='landing'),

    path('demo_piping', view_demo_piping.demo_piping, name='demo main'),
    path('demo_piping/news_feed', view_demo_piping.news_feed, name='news_feed'),
    path('demo_piping/navigation_menu', view_demo_piping.navigation_menu, name='demo_pagelet_navigation'),
    path('demo_piping/information_boxes', view_demo_piping.information_boxes, name='information_boxes'),
    path('demo_piping/top_blue_bar', view_demo_piping.top_blue_bar, name='demo_pagelet_top_blue_bar'),


    path('demo_multi_frameworks', view_demo_multi_framework.demo, name='demo multiple frameworks main'),
    path('demo_multi_frameworks/vue', view_demo_multi_framework.vue_view, name='vue'),
    path('demo_multi_frameworks/markdown', view_demo_multi_framework.markdown_view, name='markdown'),

    path('jsi18n', JavaScriptCatalog.as_view(), name='javascript-catalog'),
]
