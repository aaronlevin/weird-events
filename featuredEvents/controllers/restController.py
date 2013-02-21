# restController.py

import json

from django.core.serializers.json import DjangoJSONEncoder
from django.http import HttpResponse

from featuredEvents.models.FeaturedEvent import FeaturedEvent


class RestController():

    MAX_NUMBER_EVENTS = 10


    def getUpcomingEvents(self, request):
        if (request.method == "GET"):
            events = FeaturedEvent.objects.all().order_by('-eventDateTime').values(
                'pk', 'presenter', 'eventDateTime', 'description',
                'venueName', 'city', 'url')[0:self.MAX_NUMBER_EVENTS]
            return HttpResponse(json.dumps(list(events), cls=DjangoJSONEncoder), mimetype="application/json")
        else:
            return HttpResponse(content='', content_type=None, status=405)

    def getUpcomingEventsByCity(self, request, city):
        if (request.method == "GET"):
            events = FeaturedEvent.objects.filter(city__icontains=city).order_by(
                '-eventDateTime').values(
                    'pk', 'presenter', 'eventDateTime', 'description',
                    'venueName', 'city', 'url')[0:self.MAX_NUMBER_EVENTS]
            return HttpResponse(json.dumps(list(events), cls=DjangoJSONEncoder), mimetype="application/json")
        else:
            return HttpResponse(content='', content_type=None, status=405)

    def getEventsByDescription(self, request, searchString):
        if (request.method == "GET"):
            events = FeaturedEvent.objects.filter(description__icontains=searchString).order_by(
                '-eventDateTime').values(
                    'pk', 'presenter', 'eventDateTime', 'description',
                    'venueName', 'city', 'url')[0:self.MAX_NUMBER_EVENTS]
            return HttpResponse(json.dumps(list(events), cls=DjangoJSONEncoder), mimetype="application/json")
        else:
            return HttpResponse(content='', content_type=None, status=405)

    def getEventsByPresenter(self, request, searchString):
        if (request.method == "GET"):
            events = FeaturedEvent.objects.filter(presenter__icontains=searchString).order_by(
                '-eventDateTime').values(
                    'pk', 'presenter', 'eventDateTime', 'description',
                    'venueName', 'city', 'url')[0:self.MAX_NUMBER_EVENTS]
            return HttpResponse(json.dumps(list(events), cls=DjangoJSONEncoder), mimetype="application/json")
        else:
            return HttpResponse(content='', content_type=None, status=405)
