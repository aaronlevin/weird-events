#featuredEvents.restViews.py
from django.http import HttpResponse
from featuredEvents.controllers.restController import RestController

def getUpcomingEvents(request):
    try:
        controller = RestController()
        return controller.getUpcomingEvents(request)
    except Exception:
        return HttpResponse(content='', content_type=None, status=500)

def getUpcomingEventsByCity(request, city):
    try:
        controller = RestController()
        return controller.getUpcomingEventsByCity(request, city)
    except Exception:
        return HttpResponse(content='', content_type=None, status=500)

def getEventsByDescription(request, searchString):
    try:
        controller = RestController()
        return controller.getEventsByDescription(request, searchString)
    except Exception:
        return HttpResponse(content='', content_type=None, status=500)

def getEventsByPresenter(request, searchString):
    try:
        controller = RestController()
        return controller.getEventsByPresenter(request, searchString)
    except Exception:
        return HttpResponse(content='', content_type=None, status=500)
