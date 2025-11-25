from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.UserSignupView.as_view(), name='user-signup'),
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('events/', views.EventListView.as_view()),
    path('events/<int:pk>/', views.EventDetailView.as_view()),
    path('events/<int:pk>/register/', views.RegisterEventView.as_view()),
    path('registrations/', views.UserRegistrationListView.as_view()),
    path('registrations/<int:pk>/cancel/', views.CancelRegistrationView.as_view()),
]
