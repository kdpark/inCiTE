from django.shortcuts import render_to_response, get_object_or_404, render
from django.template import RequestContext, Context, Template, loader
from django.contrib.auth.forms import AuthenticationForm
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login

def home(request):
  data={}
  
  #return HttpResponse("inCiTE page is under construction now.")
  #return render(request, "core/index.html", data)
  return render_to_response("core/index.html", data, context_instance=RequestContext(request)) 
  
def about(request):
  data={}
  return render_to_response("core/about.html", data, context_instance=RequestContext(request)) 

def contact(request):
  data={}
  return render_to_response("core/contact.html", data, context_instance=RequestContext(request)) 