#featuredEvents.restViews.py
from django.http import HttpResponse
from featuredEvents.controllers.restController import RestController

# The "Controller" is not stateful, so let's just make a singleton.
restController = RestController()

def makeRestView(controllerAction):
    def restView(request, **kwargs):
        try:
            return controllerAction(request, **kwargs)
        except Exception:
            return HttpResponse(content='', content_type=None, status=500)
    return restView


getUpcomingEvents = makeRestView(restController.getUpcomingEvents)
getUpcomingEventsByCity = makeRestView(restController.getUpcomingEventsByCity)
getEventsByDescription = makeRestView(restController.getEventsByDescription)
getEventsByPresenter = makeRestView(restController.getEventsByPresenter)
