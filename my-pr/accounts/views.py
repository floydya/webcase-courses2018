from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView

from accounts.models import Profile


class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/register.html'


class ProfileView(DetailView):
    model = Profile


class EditProfileView(UpdateView):
    model = Profile
    fields = ['first_name', 'last_name', 'avatar', 'gender']
    template_name = 'accounts/edit.html'

    def dispatch(self, request, *args, **kwargs):
        profile = Profile.objects.get(pk=self.get_object().pk)
        if self.request.user.is_authenticated:
            if self.request.user == profile.user:
                return super().dispatch(request, *args, **kwargs)
            else:
                raise PermissionError
        else:
            raise PermissionError
