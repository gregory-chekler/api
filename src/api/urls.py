from django.urls import path, re_path
from django.conf.urls import url
from .views import *
from api.handlers.team import TeamHandler

team_handler = TeamHandler()


urlpatterns = [
  url(r'^$', ping),
  path('actions', actions),
  path('action/<int:id>', action),
  path('action/<int:id>/copy', action_copy),
  path('action/<int:id>/testimonials', action_testimonials),
  path('action-properties', action_properties),
  path('action-property/<int:id>', action_property),
  path('billing-statements', billing_statements),
  path('billing-statement/<int:id>', billing_statement),
  path('communities', communities),
  path('communities/stats', communities_stats),
  path('community/<int:cid>/stats', community_stats),
  path('community/<int:cid>', community),
  path('community/<int:cid>/full', community_profile_full),
  path('community/<int:cid>/actions', community_actions),
  path('community/<int:cid>/members', community_members),
  path('community/<int:cid>/impact', community_impact),
  path('community/<int:cid>/pages', community_pages),
  path('community/<int:cid>/events', community_events),
  path('community/<int:cid>/households', community_households),
  path('community/<int:cid>/teams', community_teams),
  path('community/<int:cid>/data', community_data),
  path('community/<int:cid>/testimonials', community_testimonials),
  path('community/<int:cid>/stories', community_testimonials),
  path('community/<int:cid>/vendors', community_vendors),
  path('community/<int:cid>/admins', community_admins_by_id_or_subdomain),
  path('community/<int:cid>/startup', startup_data),
  path('community/<str:subdomain>', community),
  path('community/<str:subdomain>/actions', community_actions),
  path('community/<str:subdomain>/members', community_members),
  path('community/<str:subdomain>/impact', community_impact),
  path('community/<str:subdomain>/pages', community_pages),
  path('community/<str:subdomain>/events', community_events),
  path('community/<str:subdomain>/households', community_households),
  path('community/<str:subdomain>/teams', community_teams),
  path('community/<str:subdomain>/data', community_data),
  path('community/<str:subdomain>/testimonials', community_testimonials),
  path('community/<str:subdomain>/stories', community_testimonials),
  path('community/<str:subdomain>/vendors', community_vendors),
  path('community/<str:subdomain>/admins', community_admins_by_id_or_subdomain),
  path('community/<str:subdomain>/startup', startup_data),
  path('community-admins', community_admins),
  path('community-admin-group/<int:id>', community_admin_group),
  path('data', data),
  path('data/<int:id>', data_by_id),
  path('email-categories', email_categories),
  path('email-category/<int:id>', email_category),
  path('events', events),
  path('event/<int:id>', event),
  path('event-attendees', event_attendees),
  path('event-attendee/<int:id>', event_attendee),
  path('goals', goals),
  path('goal/<int:id>', goal),
  path('graphs', graphs),
  path('graph/<int:id>', graph),
  path('households', households),
  path('household/<int:id>', household),
  path('locations', locations),
  path('location/<int:id>', location),
  path('media', media),
  path('media/<int:id>', media_by_id),
  path('media/<slug:slug>', media_with_slug),
  path('menus', menus),
  path('menu/<int:id>', menu),
  path('pages', pages),
  path('page/<int:id>', page),
  path('page-sections', page_sections),
  path('page-section/<int:id>', page_section),
  path('permissions', permissions),
  path('permission/<int:id>', permission),
  path('policies', policies),
  path('policy/<int:id>', policy),
  path('roles', roles),
  path('role/<int:id>', role),
  path('services', services),
  path('service/<int:id>', service),
  path('sliders', sliders),
  path('slider/<int:id>', slider),
  path('slider-images', slider_images),
  path('slider-image/<int:id>', slider_image),
  path('statistics', data),
  path('statistic/<int:id>', data_by_id),
  path('stories', testimonials),
  path('story/<int:id>', testimonial),
  path('subscribers', subscribers),
  path('subscriber/<int:id>', subscriber),
  path('subscriber-email-preferences', subscriber_email_preferences),
  path('subscriber-email-preference/<int:id>', subscriber_email_preference),
  path('tags', tags),
  path('tag/<int:id>', tag),
  path('tag-collections', tag_collections),
  path('tag-collection/<int:id>', tag_collection),
  path('teams', teams),
  path('teams/stats', teams_stats),
  path('team/<int:id>', team),
  path('team/<int:id>/stats', team_stats),
  path('team/<int:team_id>/member/<str:member_id>', team_member),
  path('testimonials', testimonials),
  path('testimonial/<int:id>', testimonial),
  path('users', users),
  path('user/<str:id>', user),
  path('user/<str:id>/households', user_households),
  path('user/<str:id>/household/<int:hid>/actions', user_household_actions),
  path('user/<str:id>/actions', user_actions),
  path('user/<str:id>/action/<int:aid>', user_action),
  path('user/<str:id>/teams', user_teams),
  path('user/<str:id>/testimonials', user_testimonials),
  path('user/e/<str:email>', user_by_email),
  path('user/e/<str:email>/households', user_households_by_email),
  path('user/e/<str:email>/household/<int:hid>/actions', user_household_actions_by_email),
  path('user/e/<str:email>/actions', user_actions_by_email),
  path('user/e/<str:email>/action/<int:aid>', user_action_by_email),
  path('user/e/<str:email>/teams', user_teams_by_email),
  path('user/e/<str:email>/testimonials', user_testimonials_by_email),
  path('user-groups', user_groups),
  path('user-group/<int:id>', user_group),
  path('vendors', vendors),
  path('vendor/<int:id>', vendor),
  path('verify', verify_captcha)
]

urlpatterns.extend(team_handler.get_routes_to_views())