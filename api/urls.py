from django.urls import path
from .views import ClienteList, Logout

urlpatterns = [
    path('cliente/', ClienteList.as_view(), name='cliente_list'),
    path('logout/', Logout.as_view(), name='logout'),
]

