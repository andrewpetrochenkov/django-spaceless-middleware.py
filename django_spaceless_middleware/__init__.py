from django.utils.html import strip_spaces_between_tags


class SpacelessMiddleware(object):

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        response.content = strip_spaces_between_tags(
            response.content.decode('utf-8')).encode('utf-8')
        return response
