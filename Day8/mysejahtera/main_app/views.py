import django
from django.contrib import messages
from django.db.models import fields
from django.http import request
from django.shortcuts import redirect, render
from django.views.generic.edit import DeleteView, UpdateView
from .models import Post, QRLocation, GeoLocation
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, CreateView
from .forms import HealthUpdateForm, VaccineForm, QRCreateForm
from django.contrib.auth.models import User
import sys
from django.db.models import Count
import requests
import json
from account.models import Profile
# Create your views here.


@login_required
def home(request):
    context = {'posts': Post.objects.all(),
               'location': GeoLocation.objects.filter(author=request.user),
               }
    return render(request, 'main_app/home.html', context)


def is_users(post_user, logged_user):
    return post_user == logged_user


PAGINATION_COUNT = 3


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['text']
    template_name = 'main_app/post_new.html'
    success_url = '/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['text']
    template_name = 'main_app/post_new.html'
    success_url = '/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        return is_users(self.get_object().author, self.request.user)

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['tag_line'] = 'Edit a post'
        return data


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'main_app/post_delete.html'
    context_object_name = 'post'
    success_url = '/'

    def test_func(self):
        return is_users(self.get_object().author, self.request.user)


# vaccine

def vaccineview(request):
    return render(request, 'main_app/vaccine.html')


def vaccine(request):
    if (request.method == 'POST'):
        vform = VaccineForm(
            request.POST, request.FILES, instance=request.user.vaccine)
        if vform.is_valid:
            vform.save()
            return redirect('vaccine')
    else:
        vform = VaccineForm(instance=request.user.vaccine)

    return render(request, 'main_app/vaccine_register.html', {'vform': vform})


# health
# @login_required
def health(request):
    return render(request, 'main_app/health.html')


def healthupdate(request):
    # hform =  HealthUpdateForm()
    # return render(request,'main_app/healthupdate .html', {'hform': hform})

    if (request.method == 'POST'):
        hform = HealthUpdateForm(
            request.POST, request.FILES, instance=request.user.healthinfo)
        if hform.is_valid:
            hform.save()
            return redirect('health')
    else:
        hform = HealthUpdateForm(instance=request.user.healthinfo)

    return render(request, 'main_app/healthupdate.html', {'hform': hform})


# qrcode
@login_required
def qrcode(request):
    context = {'qrcode': QRLocation.objects.filter(author=request.user)}
    return render(request, 'main_app/qrcode.html', context)

# class qrcode(LoginRequiredMixin, ListView):
#     model = QRLocation
#     print (QRLocation.objects.all)
#     template_name = 'main_app/qrcode.html'
#     # context_object_name = 'posts'
#     paginate_by = PAGINATION_COUNT


def create_qr(request):
    print(request.POST)
    print(request.user)

    if (request.method == 'POST'):

        qr = QRLocation.objects.create()
        qr.name = request.POST['name']
        qr.address = request.POST['address']
        qr.city = request.POST['city']
        qr.state = request.POST['state']
        qr.author = request.user
        qr.save()

        return redirect('qrcode')
    else:
        form = QRCreateForm()

    return render(request, 'main_app/qr_create.html', {'form': form})


# location

locationdata = {}


@login_required
def location(request):

    ip = requests.get('https://api.ipify.org?format=json')
    ip_data = json.loads(ip.text)
    res = requests.get('http://ip-api.com/json/' +
                       ip_data["ip"])  # data from json
    location_data_one = res.text
    # convert jason to python dictionary
    location_data = json.loads(location_data_one)

    locationdata = location_data

    return render(request, 'main_app/location.html', {'data': location_data})


def submit_loc(request):

    ip = requests.get('https://api.ipify.org?format=json')
    ip_data = json.loads(ip.text)
    res = requests.get('http://ip-api.com/json/' +
                       ip_data["ip"])  # data from json
    location_data_one = res.text
    # convert jason to python dictionary
    location_data = json.loads(location_data_one)

    locationdata = location_data

    loc = GeoLocation.objects.create()
    loc.country = locationdata["country"]
    loc.regionName = locationdata["regionName"]
    loc.city = locationdata["city"]
    loc.zip = locationdata["zip"]
    loc.latitude = locationdata["lat"]
    loc.longitude = locationdata["lon"]
    loc.country_code = locationdata["countryCode"]
    loc.timezone = locationdata["timezone"]
    loc.author = request.user
    loc.save()

    return render(request, 'main_app/location.html', {'data': location_data})
