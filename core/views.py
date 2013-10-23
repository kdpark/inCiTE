from django.shortcuts import render_to_response, get_object_or_404, render
from django.template import RequestContext, Context, Template, loader
from django.contrib.auth.forms import AuthenticationForm
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.contrib.auth import authenticate, login
from core.models import Participant
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

def test1(request):

  p = Participant(name= request.POST['pid'], extype=1)
  # duplication problem
  try:
    p.save()
  except:
    return HttpResponse("Duplication Problem!")
  # how to collect the like_id
  # ajax
  data={}
  data['pid'] = request.POST['pid']
  return render_to_response("core/test1.html", data, context_instance=RequestContext(request)) 

def test2(request):
  p = Participant(name= request.POST['pid'], extype=2)
  # duplication problem
  try:
    p.save()
  except:
    return HttpResponse("Duplication Problem!")
  
  data={}
  data['pid'] = request.POST['pid']
  return render_to_response("core/test2.html", data, context_instance=RequestContext(request)) 

def start1(request):
  data={}
  return render_to_response("core/start1.html", data, context_instance=RequestContext(request)) 

def start2(request):
  data={}
  return render_to_response("core/start2.html", data, context_instance=RequestContext(request))   

def clicklike(request, uid, lid):
  
  user = Participant.objects.get(name=uid)
  print lid

  if lid=='0':
    user.article0 = 1
    user.save()

  elif lid =='1':
    user.article1 = 1
    user.save()
  elif lid =='2':
    user.article2 = 1
    user.save()
  elif lid =='3':
    user.article3 = 1
    user.save()
  elif lid =='4':
    user.article4 = 1
    user.save()
  elif lid =='5':
    user.article5 = 1
    user.save()
  elif lid =='6':
    user.article6 = 1
    user.save()
  elif lid =='7':
    user.article7 = 1
    user.save()
  elif lid =='8':
    user.article8 = 1
    user.save()
  elif lid =='9':
    user.article9 = 1
    user.save()
  elif lid =='10':
    user.article10 = 1
    user.save()
  elif lid =='11':
    user.article11 = 1
    user.save()
  elif lid =='12':
    user.article12 = 1
    user.save()
  elif lid =='13':
    user.article13 = 1
    user.save()
  elif lid =='14':
    user.article14 = 1
    user.save()
  
  return HttpResponse('<html><body onload="finish()">Good</body><script>function finish(){window.opener = window.location.href; self.close();}</script></html>');


