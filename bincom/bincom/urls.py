"""
URL configuration for bincom project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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

from django.urls import path
from john_ali.views import polling_unit_list, polling_unit_detail, local_government_results, save_polling_unit

urlpatterns = [

    path('polling-units/<int:uniqueid>/', polling_unit_detail, name='polling_unit_detail'),
    path('polling-units/', polling_unit_list, name='polling_unit_list'),
    path('local-government-results/', local_government_results, name='local_government_results'),
     path('save_polling_unit/', save_polling_unit, name='save_polling_unit'),
]

