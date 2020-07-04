from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.forms import ModelForm
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect


# Create your views here.
from django.views import View

from mf.models import Trip, Relation, Reviews, CommentTrip, CommentRelation, CommentReviews
from motofriends.forms import AddTripForm, AddRelationForm, AddReviewForm, CommentTripForm, CommentRelationForm, \
    CommentReviewsForm
from register.models import UserProfile


def index(request):
    trips = Trip.objects.all()
    return render(request, 'base.html', {'trips':trips})

class AddTripView(View):
    def get(self, request):
        form = AddTripForm()
        return render(request, 'addTrip.html', {'form': form})

    def post(self, request):
        t = AddTripForm(request.POST)
        # print(request)
        # print(t)
        if t.is_valid():
            # print('hey')
            trip=t.save(commit=False)
            trip.creator=request.user
            trip.save()
        return render(request, "base.html")


class ShowTripsView(View):
    def get(self, request):
        trips = Trip.objects.all()
        return render(request, 'trips.html', {'trips':trips})


class ShowTripDetailsView(View):
    def get(self, request, id):
        trip = Trip.objects.get(id=id)
        comments = CommentTrip.objects.filter(trip=id)
        return render(request, 'trip_details.html', {'trip': trip, 'comments':comments})

class AddRelationView(View):
    def get(self, request):
        form = AddRelationForm()
        return render(request, 'addRelation.html', {'form': form})

    def post(self, request):
        r = AddRelationForm(request.POST)
        if r.is_valid():
            relation= r.save(commit=False)
            relation.creator = request.user
            relation.save()
        return render(request, "base.html")

class ShowRelationDetailsView(View):
    def get(self, request, id):
        relation = Relation.objects.get(pk=id)
        comments = CommentRelation.objects.filter(relation=id)
        return render(request, 'relation.html', {'relation': relation, 'comments':comments})

class ShowRelationView(View):
    def get(self, request):
        relations = Relation.objects.all()
        return render(request, 'relations.html', {'relations':relations})

class AddReviewView(View):
    def get(self, request):
        form = AddReviewForm()
        return render(request, 'addReview.html', {'form': form})

    def post(self, request):
        b = AddReviewForm(request.POST)
        if b.is_valid():
            review = b.save(commit=False)
            review.creator = request.user
            review.save()
        return render(request, "base.html")

class ShowReviewDetailsView(View):
    def get(self, request, id):
        reviews = Reviews.objects.get(pk=id)
        comments = CommentReviews.objects.filter(reviews=id)
        return render(request, 'review.html', {'reviews': reviews,'comments':comments})

class ShowReviewView(View):
    def get(self, request):
        reviews = Reviews.objects.all()
        return render(request, 'reviews.html', {'reviews':reviews})

class AddCommentTripView(View):
    def get(self, request, id):
        form = CommentTripForm()
        return render(request, 'addcommenttrip.html', {'form': form})

    def post(self, request, id):
        trip = Trip.objects.get(id=id)
        y = CommentTripForm(request.POST)
        if y.is_valid():
            comment = y.save(commit=False)
            comment.creator = request.user
            comment.trip = trip
            comment.save()
        return render(request, 'base.html')

class AddCommentRelationView(View):
    def get(self, request, id):
        form = CommentRelationForm()
        return render(request, 'addcommentrelation.html', {'form': form})

    def post(self, request, id):
        relation = Relation.objects.get(id=id)
        y = CommentRelationForm(request.POST)
        if y.is_valid():
            comment = y.save(commit=False)
            comment.creator = request.user
            comment.relation = relation
            comment.save()
        return render(request, 'base.html')

class AddCommentReviewsView(View):
    def get(self, request, id):
        form = CommentReviewsForm()
        return render(request, 'addcommentreview.html', {'form': form})

    def post(self, request, id):
        reviews = Reviews.objects.get(id=id)
        y = CommentReviewsForm(request.POST)
        if y.is_valid():
            comment = y.save(commit=False)
            comment.creator = request.user
            comment.reviews = reviews
            comment.save()
        return render(request, 'base.html')