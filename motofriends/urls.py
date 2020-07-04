"""motofriends URL Configuration

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
from django.urls import path, include

from mf import views
from register import views as v

urlpatterns = [
    path('', views.index),
    path('admin/', admin.site.urls),
    path('register/', v.register, name = 'register'),
    path("trips/", views.ShowTripsView.as_view()),
    path("add_trip/", views.AddTripView.as_view()),
    path("trip_details/<int:id>/", views.ShowTripDetailsView.as_view()),
    path('', include('django.contrib.auth.urls')),
    path("user/<int:id>/", v.ShowProfileView.as_view()),
    path("add_relation/", views.AddRelationView.as_view()),
    path("relation_details/<int:id>/", views.ShowRelationDetailsView.as_view()),
    path("relations/", views.ShowRelationView.as_view()),
    path("add_review/", views.AddReviewView.as_view()),
    path("review_details/<int:id>/", views.ShowReviewDetailsView.as_view()),
    path("reviews/", views.ShowReviewView.as_view()),
    path("add_commenttrip/<int:id>", views.AddCommentTripView.as_view()),
    path("add_commentrelation/<int:id>", views.AddCommentRelationView.as_view()),
    path("add_commentreview/<int:id>", views.AddCommentReviewsView.as_view()),
]
