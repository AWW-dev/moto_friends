from django import forms

from mf.models import Trip, Relation, Reviews, CommentTrip, CommentRelation, CommentReviews


class AddTripForm(forms.ModelForm):
    class Meta:
        model = Trip
        exclude = ['last_modification','create_date','creator']

class AddRelationForm(forms.ModelForm):
    class Meta:
        model = Relation
        exclude = ['last_modification','create_date','creator']

class AddReviewForm(forms.ModelForm):
    class Meta:
        model = Reviews
        exclude = ['last_modification','create_date','creator']

class CommentTripForm(forms.ModelForm):
    class Meta:
        model = CommentTrip
        exclude = ['trip','create_date','creator']

class CommentRelationForm(forms.ModelForm):
    class Meta:
        model = CommentRelation
        exclude = ['relation','create_date','creator']

class CommentReviewsForm(forms.ModelForm):
    class Meta:
        model = CommentReviews
        exclude = ['reviews','create_date','creator']



