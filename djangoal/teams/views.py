from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from . import models


class TeamListView(ListView):
    model = models.Team
    context_object_name = "teams"


class TeamDetailView(DetailView):
    model = models.Team