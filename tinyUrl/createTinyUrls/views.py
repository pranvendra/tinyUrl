from django.shortcuts import render
from django.http import HttpResponse
from .models import TinyUrl
from django.template import loader

def index(request):
	latest_tinyUrl_list = TinyUrl.objects.order_by('-pub_date')[:5]
	template = loader.get_template('createTinyUrls/index.html')
	context = {'latest_tinyUrl_list': latest_tinyUrl_list}
	return HttpResponse(template.render(context, request))

def detail(request, url_id):
	return HttpResponse("You're looking at url %s." % url_id)

def results(request, url_id):
	response = "You're looking at the results of url %s."
	return HttpResponse(response % url_id)

def vote(request, url_id):
	return HttpResponse("You're voting on question %s." % url_id)
