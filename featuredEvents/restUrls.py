from django.conf.urls import patterns, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('featuredEvents.restViews',
    url(r'^$', "getUpcomingEvents", name="getUpcomingEvents"),
    url(r"^city/(?P<city>(.+))/$",
        "getUpcomingEventsByCity", name="getUpcomingEventsByCity"),
    url(r"^search/(?P<searchString>[a-zA-Z0-9_-]+)/$",
        "getEventsByDescription", name="getEventsByDescription"),
    url(r"^presenter/(?P<searchString>[a-zA-Z0-9_-]+)/$",
        "getEventsByPresenter", name="getEventsByPresenter"),
)
