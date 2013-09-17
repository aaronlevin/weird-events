from django.conf.urls import patterns, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', "featuredEvents.restViews.getUpcomingEvents", name="getUpcomingEvents"),
    url(r"^city/(?P<city>(.+))/$",
        "featuredEvents.restViews.getUpcomingEventsByCity", name="getUpcomingEventsByCity"),
    url(r"^search/(?P<searchString>[a-zA-Z0-9_-]+)/$",
        "featuredEvents.restViews.getEventsByDescription", name="getEventsByDescription"),
    url(r"^presenter/(?P<searchString>[a-zA-Z0-9_-]+)/$",
        "featuredEvents.restViews.getEventsByPresenter", name="getEventsByPresenter"),
)
