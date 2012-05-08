from django.conf.urls import patterns, include, url
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'program.views.view_program_all', name='view_program_all'),

    url(r'^program/manage/$', 'program.views.manage_program'),
    url(r'^program/create/', 'program.views.create_program'),
    url(r'^program/(?P<program_id>\d+)/$', 'program.views.view_program' , name='view_program'),
    url(r'^program/(?P<program_id>\d+)/edit/$', 'program.views.edit_program' , name='edit_program'),
    url(r'^program/(?P<program_id>\d+)/delete/$', 'program.views.delete_program' , name='delete_program'),

    url(r'^login/$', 'operators.views.operator_login', name='operator_login'),
    url(r'^logout/$', 'operators.views.operator_logout', name='operator_logout'),

    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
   )

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns += staticfiles_urlpatterns()