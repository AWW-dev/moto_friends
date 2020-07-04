from django.contrib import admin
from .models import Trip, CommentTrip, Relation, CommentRelation, Reviews, CommentReviews

admin.site.register(Trip)
admin.site.register(CommentTrip)
admin.site.register(Relation)
admin.site.register(CommentRelation)
admin.site.register(Reviews)
admin.site.register(CommentReviews)

# Register your models here.
