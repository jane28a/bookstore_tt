from django.db import models


class Request(models.Model):

    '''Model representating of the HttpRequest objects to store
    basic request data in the db'''

    time = models.DateTimeField(auto_now_add=True)
    path = models.CharField(null=False,
                            blank=False,
                            max_length=300)
    method = models.CharField(null=False,
                            blank=False,
                            max_length=20)
    content_type = models.CharField(null=False,
                                    blank=False,
                                    max_length=150)
    content_params = models.TextField(null=True,
                                    blank=True)
    headers = models.TextField(null=False,
                                blank=False)
    get_data = models.TextField(null=True,
                                blank=True)
    post_data = models.TextField(null=True,
                                blank=True)
    cookies = models.TextField(null=True,
                                blank=True)
    response_status = models.IntegerField(null=False,
                                        blank=False)

    def __str__(self):
        return '{}: {} to {}. Status: {}'.format(self.time.strftime("%Y-%m-%d %H:%M:%S"),
                                                self.method,
                                                self.path,
                                                self.response_status)
