from pyconbalkan.conference.models import Conference


class ConferenceSelectionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response


    def __call__(self, request):
        try:
            request.conference = Conference.objects.get(active=True)
        except Conference.DoesNotExist:
            pass

        return self.get_response(request)
