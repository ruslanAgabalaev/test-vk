from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Friends, Group

class FriendsView(LoginRequiredMixin, ListView):
    model = Friends
    template_name = 'friends.html'
    context_object_name = 'friends'
    login_url = '/login/'

class FriendsDetailView(LoginRequiredMixin, DetailView):
    model = Friends
    template_name = 'friend_detail.html'
    context_object_name = 'friend'
    login_url = '/login/'

class GroupsView(LoginRequiredMixin, ListView):
    model = Group
    template_name = 'groups.html'
    context_object_name = 'groups'
    login_url = '/login/'

class FriendsCreateView(LoginRequiredMixin, CreateView):
    model = Friends
    template_name = 'friends_form.html'
    fields = ['first_name', 'last_name', 'birth_date', 'group']
    success_url = reverse_lazy('friends')
    login_url = '/login/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class GroupCreateView(LoginRequiredMixin, CreateView):
    model = Group
    template_name = 'group_form.html'
    fields = ['name', 'description', 'members']
    success_url = reverse_lazy('groups')
    login_url = '/login/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)