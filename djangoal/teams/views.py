from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from . import models
from . import mixins

class TeamListView(ListView):
    model = models.Team
    context_object_name = "teams"


class TeamDetailView(DetailView):
    model = models.Team


class TeamCreateView(LoginRequiredMixin, mixins.PageTitleMixin ,CreateView):
    fields = ("name", "practice_location", "coach")
    model =  models.Team
    page_title = "Create a new Team"

    def get_initial(self):
        initial = super(TeamCreateView, self).get_initial()
        initial["coach"] = self.request.user.pk
        return initial



class TeamUpdateView(LoginRequiredMixin, mixins.PageTitleMixin, UpdateView):
    fields = ("name", "practice_location", "coach")
    model =  models.Team

    def get_page_title(self):
        obj = self.get_object()
        return "Update {}".format(obj.name)



class TeamDeleteView(LoginRequiredMixin, DeleteView):
    model = models.Team
    success_url = reverse_lazy("teams:list")


    def get_queryset(self):
        if not self.request.user.is_superuser:
            return self.model.objects.filter(coach=self.request.user)
        return self.model.objects.all()
