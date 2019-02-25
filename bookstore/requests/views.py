from django.shortcuts import render
from django.http import HttpResponseNotAllowed 

from .models import Request


def last_requests(request):

    '''Get last 10 request instanses from db.
    Current request not included in this list'''

    if request.method == 'GET':
        requests_list = Request.objects.order_by('-time')[:10]
        return render(request, 'requests/list.html', {'requests': requests_list})
    else: 
        return HttpResponseNotAllowed(['GET'])