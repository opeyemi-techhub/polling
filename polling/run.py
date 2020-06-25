from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.views import generic
import datetime
from django.utils import timezone
from .models import Voter
class runner():
    print("jjj")
