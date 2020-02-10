from django.urls import path
from .views import *

urlpatterns=[
    path('jobs/',view_get_post_jobs),
    path('jobs/<int:ID>',view_getByID_updateByID_deleteByID),
    path('jobs/<int:pageNo>/<int:items>',pagination)
]