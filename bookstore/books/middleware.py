import json 

from .models import Request


def dumps(data):

    '''Helper function for dumping dict-like objects to string representation
    via json.dumps with given default value to avoid TypeError during convertation'''

    return json.dumps(data, default=lambda d: None)


class RequestStoringMiddleware:

    '''Simple middleware that takes basic request data and 
    creates object of the Request midel and then saves it to db'''

    def __init__(self, get_response):

        self.get_response = get_response


    def __call__(self, request):

        #We have to save only http requests
        if request.scheme == 'http':
            req = Request(
                path = request.path,
                method = request.method,
                content_type = request.content_type,
                content_params = dumps(request.content_params),
                headers = dumps(request.META),
                get_data = dumps(request.GET),
                post_data = dumps(request.POST),
                cookies = dumps(request.COOKIES)
            )

        response = self.get_response(request)

        if req:
            req.response_status = response.status_code
            req.save()

        return response