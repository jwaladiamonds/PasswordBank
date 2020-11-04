from django.urls import reverse_lazy
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth import login, logout

from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import CreateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin

from accounts.forms import LoginForm, SignUpForm
from accounts.models import User


class UserLoginView(SuccessMessageMixin, LoginView):
    authentication_form = LoginForm
    template_name = 'accounts/login.html'
    success_message = 'Successfully logged in to Password Bank'
    redirect_authenticated_user=True

    def form_valid(self, form):
        user = form.get_user()
        login(self.request, user)
        if not self.request.POST.get('remember_me', None):
            self.request.session.set_expiry(0)
        return redirect(self.get_success_url())


class UserSignUpView(SuccessMessageMixin, CreateView):
    form_class = SignUpForm
    template_name = 'accounts/signup.html'
    success_url = reverse_lazy('accounts:login')
    success_message = 'Successfully created new user in Password Bank'

    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return super().get(request, *args, **kwargs)
        return redirect('dash:home')


class UserDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = User
    template_name = 'accounts/delete_confirm.html'
    success_message = 'Successfully removed your account from Password Bank'


    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        print(self.object)
        if self.object == request.user:
            self.object.delete()
            logout(request)
            return redirect('accounts:login')
        return redirect('dash:home')

    def get_object(self):
        username = self.kwargs.get("username")
        return get_object_or_404(User, username=username)

user_login = UserLoginView.as_view()
user_signup = UserSignUpView.as_view()
user_delete = UserDeleteView.as_view()
user_logout = LogoutView.as_view()