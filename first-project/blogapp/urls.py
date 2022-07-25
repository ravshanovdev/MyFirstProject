from django.urls import path
from .views import kirmaview
from .views import about

urlpatterns = [
    path('', kirmaview, name='kirmaview'),
    path('about/', about, name= 'about' ),
]