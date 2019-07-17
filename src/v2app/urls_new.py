from django.urls import path, re_path
from django.conf.urls import url
from .views_new import *

urlpatterns = [
  url(r'^$', ping),
  path('actions', actions),
  path('action/<int:id>', action),
  path('action-properties', ping),
  path('action-property/<int:id>', ping),
  path('billing-statements', ping),
  path('billing-statement/<int:id>', ping),
  path('communities', ping),
  path('community/<int:id>', ping),
  path('community-admins', ping),
  path('community-admins/<int:id>', ping),
  path('data', ping),
  path('data/<int:id>', ping),
  path('email-categories', ping),
  path('email-category/<int:id>', ping),
  path('events', ping),
  path('event/<int:id>', ping),
  path('event-attendees',ping),
  path('event-attendee/<int:id>',ping),
  path('goals',ping),
  path('goal/<int:id>',ping),
  path('graphs',ping),
  path('graph/<int:id>',ping),
  path('households',ping),
  path('household/<int:id>',ping),
  path('locations',ping),
  path('location/<int:id>',ping),
  path('media',ping),
  path('media/<int:id>',ping),
  path('media/<slug:id>',ping),
  path('menu', ping),
  path('menu/<int:id>', ping),
  path('pages', ping),
  path('page/<int:id>', ping),
  path('page-sections',ping),
  path('page-section/<int:id>',ping),
  path('permissions',ping),
  path('permission/<int:id>',ping),
  path('policies', ping),
  path('policy/<int:id>', ping),
  path('roles',ping),
  path('role/<int:id>',ping),
  path('services', ping),
  path('service/<int:id>', ping),
  path('sliders',ping),
  path('slider/<int:id>',ping),
  path('slider-images',ping),
  path('slider-image/<int:id>',ping),
  path('statistics',ping),
  path('statistic/<int:id>',ping),
  path('stories', ping),
  path('story/<int:id>', ping),
  path('subscribers',ping),
  path('subscriber/<int:id>',ping),
  path('subscriber-email-preferences',ping),
  path('subscriber-email-preference/<int:id>',ping),
  path('tags',ping),
  path('tag/<int:id>',ping),
  path('tag-collections',ping),
  path('tag-collection/<int:id>',ping),
  path('teams', ping),
  path('team/<int:id>', ping),
  path('testimonials',ping),
  path('testimonial/<int:id>',ping),
  path('users',ping),
  path('user/<int:id>',ping),
  path('user/<int:id>/households',ping),
  path('user/<int:id>/household/<household_id>/actions',ping),
  path('user/<int:id>/household/<household_id>/todo',ping),
  path('user/<int:id>/household/<household_id>/completed',ping),
  path('user/<int:id>/actions',ping),
  path('user/<int:id>/teams',ping),
  path('user/<int:id>/testimonials',ping),
  path('user-groups',ping),
  path('user-group/<int:id>',ping),
  path('vendors',ping),
  path('vendor/<int:id>',ping),
]