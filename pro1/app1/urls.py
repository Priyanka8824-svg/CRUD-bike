from django.urls import path
from .views import *

urlpatterns=[
    path("hv/",hview),
    path("bv/",bview),
    path("sv/",sview),
    path("uv/<int:pk>/",updateview),
    path("dv/<int:x>/",deleteview)
]