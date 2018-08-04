from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView
from account.models import Profile


class UserProfile(DetailView):
    model = Profile
    slug_field = "user__username"


class SignUpUser(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/register.html'

    def form_valid(self, form):
        new_user = form.save()
        messages.success(self.request, "Спасибо за регистрацию. Вы были автоматически авторизованы.")
        new_user = authenticate(username=form.cleaned_data['username'],
                                password=form.cleaned_data['password1'])
        login(self.request, new_user)
        return redirect('edit-profile')


class EditProfile(UpdateView):
    model = Profile
    fields = ('image', )

    def get_object(self, queryset=None):
        obj = Profile.objects.get(user=self.request.user)
        return obj

    def form_valid(self, form):
        updated = form.save()
        if form.cleaned_data.get('first_name'):
            self.request.user.first_name = form.cleaned_data['first_name']
        if form.cleaned_data.get('last_name'):
            self.request.user.last_name = form.cleaned_data['last_name']
        self.request.user.save()
        return redirect('profile', slug=self.request.user.username)

