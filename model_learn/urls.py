from django.urls import path
from . import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('',views.index),
    path('detail',views.detail),
    path('update',views.update),
    path('delete',views.delete),
]
