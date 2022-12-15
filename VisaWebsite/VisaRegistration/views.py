from django.shortcuts import render, redirect
from django import views
from django.http import Http404, HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from VisaWebsite import settings
from .forms import LoginForm, RegistrationForm, VisaForm
from .models import Visa, User
from django.utils import timezone


class MainView(views.View):

    def get(self, request, *args, **kwargs):
        users_count = User.objects.filter(is_superuser='0').count()
        visa_count = Visa.objects.filter(status__status='Видано').count()

        return render(request, 'main/main.html', {'users': users_count, 'visa_count': visa_count })

    def post(self, request, *args, **kwargs):
        users_count = User.objects.filter(is_superuser='0').count()
        visa_count = Visa.objects.filter(status__status='Видано').count()

        return render(request, 'main/main.html', {'users': users_count, 'visa_count': visa_count })


class InfoView(views.View):
    template_name = 'info.html'

    def get(self, request, *args, **kwargs):

        return render(request, 'main/info.html')

    def post(self, request, *args, **kwargs):

        return render(request, 'main/info.html')


class VisaView(views.View):
    template_name = 'visa_processing.html'

    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseRedirect(request.GET.get('next',
                                                        settings.NOT_LOGGED_REDIRECT_URL))
        if request.user.is_authenticated:
            form = VisaForm(request.POST or None)
            context = {
                'form': form
            }
            return render(request, 'main/visa_processing.html', context)

    def post(self, request, *args, **kwargs):

        form = VisaForm(request.POST or None)
        username = None
        if request.user.is_authenticated:
            if form.is_valid():
                date_issue = timezone.datetime.now()
                username = request.user.username
                new_visa = form.save(commit=False)
                new_visa.username = username
                new_visa.first_name = form.cleaned_data['first_name']
                new_visa.surname = form.cleaned_data['surname']
                new_visa.series_passport = form.cleaned_data['series_passport']
                new_visa.country = form.cleaned_data['country']
                new_visa.visa_type = form.cleaned_data['visa_type']
                new_visa.tariff_number = form.cleaned_data['tariff_number']
                new_visa.phone = form.cleaned_data['phone']
                new_visa.email = form.cleaned_data['email']
                new_visa.date_issue = date_issue
                tariff_days = int(str(form.cleaned_data.get('tariff_number')))
                new_visa.valid_date = date_issue.date() + timezone.timedelta(days=tariff_days)
                new_visa.save()
                tariff_days = int(str(form.cleaned_data.get('tariff_number')))
                messages.success(request, 'Вітаємо! Залишилося трохи.')
                return redirect('/profile')


class LoginView(views.View):

    def get(self, request, *args, **kwargs):
        username = None
        if request.user.is_authenticated:
            username = request.user.username
            return HttpResponseRedirect(request.GET.get('next',
                                                        settings.LOGIN_REDIRECT_URL))
        else:
            form = LoginForm(request.POST or None)
            context = {
                'form': form
            }

            return render(request, 'main/login.html', context)

    def post(self, request, *args, **kwargs):

        form = LoginForm(request.POST or None)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return HttpResponseRedirect('/profile')
        context ={
            'form': form
        }
        if not request.user.is_authenticated:
            return render(request, 'main/login.html', context)
        if request.user.is_authenticated:
            return render(request, 'main/visa_processing.html', context)


class RegistrationView(views.View):

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            username = request.user.username
            return HttpResponseRedirect(request.GET.get('next',
                                                        settings.NOT_LOGGED_REDIRECT_URL))
        form = RegistrationForm(request.POST or None)
        context = {
            'form': form
        }

        return render(request, 'main/registration.html', context)

    def post(self, request, *args, **kwargs):
        form = RegistrationForm(request.POST or None)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.username = form.cleaned_data['username']
            new_user.email = form.cleaned_data['email']
            new_user.first_name = form.cleaned_data['first_name']
            new_user.last_name = form.cleaned_data['last_name']
            new_user.birthday = form.cleaned_data['birthday']
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            login(request, user)
        context = {
            'form': form
        }
        return render(request, 'main/profile.html', context)


class UserProfile(views.View):
    template_name = 'profile.html'

    def get(self, request, *args, **kwargs):

        username = None
        if request.user.is_authenticated:
            username = request.user
            visa_issued = Visa.objects.filter(username=username).order_by('code_visa')
        else:
            raise Http404("You're not loggined")

        return render(request, 'main/profile.html', {'visa': visa_issued})

    def post(self, request, *args, **kwargs):
        username = None
        if request.user.is_authenticated:
            username = request.user
        else:
            raise Http404("You're not loggined")

        return render(request, 'main/main.html', {'username': username})
