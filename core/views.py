from django.shortcuts import render_to_response, get_object_or_404, render
from django.template import RequestContext, Context, Template, loader
from django.contrib.auth.forms import AuthenticationForm
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login
import datetime

#datetime.datetime.now()

def home(request):
  data={}
  return render_to_response("core/index.html", data, context_instance=RequestContext(request)) 
  
def about(request):
  data={}
  return render_to_response("core/about.html", data, context_instance=RequestContext(request)) 

def contact(request):
  data={}
  return render_to_response("core/contact.html", data, context_instance=RequestContext(request)) 

def member(request):
  data={}
  return render_to_response("core/member.html", data, context_instance=RequestContext(request)) 

def relation(request):
  data={}
  return render_to_response("core/relationship.html", data, context_instance=RequestContext(request)) 

def calendar(request):
  data={}
  return render_to_response("core/calendar.html", data, context_instance=RequestContext(request)) 

def idea(request):
  data={}
  return render_to_response("core/idea.html", data, context_instance=RequestContext(request)) 

def board(request):
  data={}
  return render_to_response("core/board.html", data, context_instance=RequestContext(request)) 
