from django.http import HttpResponse
import datetime
from django.template import Template, Context
from django.template.loader import get_template
from django.shortcuts import render_to_response
def hello(request):
	return HttpResponse("hello world")



def current_datetime(request):
	now = datetime.datetime.now()
	html = "<html><body> It is now %s.hiahia</body></html>" % now
	t = get_template('current_datetime.html')

	#t = Template("<html><body> It is now {{time}}.</body></html>")
	c = Context({'current_date':now})
	html = t.render(c)
	return render_to_response("current_datetime.html",{"current_date":now})
	return HttpResponse(html)

def hours_ahead(request, offset):
	try:
		offset = int(offset)
	except ValueError:
		raise Http404()
	dt = datetime.datetime.now()+datetime.timedelta(hours=offset)
	html="<html><body> In %s hour(s), it will be %s.</body></html>"%(offset, dt)
	return HttpResponse(html)

import os 
print(os.path)

