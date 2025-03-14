"""journal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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

from django.urls import include
from django.urls import path

from django.views.generic import RedirectView

from django.conf import settings
from django.conf.urls.static import static
import catalog.views as views
from catalog.views import DiariesJson

urlpatterns = [
    path('admin/', admin.site.urls),
    path('datatable/', DiariesJson.as_view(), name='diaries_json'),
    path('entries_json/<query>', views.entries_json, name="entries_json"),
    path('entries_text/<query>', views.entries_text, name="entries_text"),
    path('charts/<type>/<query>', views.charts, name="charts"),

]

urlpatterns += [
    path('catalog/', include('catalog.urls')),
]

urlpatterns += [
    path('', RedirectView.as_view(url='/catalog/', permanent=True)),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
