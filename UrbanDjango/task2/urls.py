from django.urls import path
from . import views

urlpatterns = [
    path('function-view/',views.function_base_view,name='function_view'),
    path('class-view/',views.ClassBasedView.as_view(),name='class_view')
]