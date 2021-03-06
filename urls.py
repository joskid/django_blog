from django.conf.urls.defaults import *

import os.path

from django.contrib import admin
admin.autodiscover()

site_media = os.path.join(
    os.path.dirname(__file__), 'site_media'
)

urlpatterns = patterns('',
    
    # Blog
    (r'^', include('blog.urls.posts')),
    
    # Categories
    (r'^categories/', include('blog.urls.categories')),
    
    # Tag
    (r'^tag/', include('blog.urls.tags')),

    # Profiles
    (r'^profiles/', include('django_blog.profiles.urls')),
    
    # Flat Pages
    #(r'^flat/', include('django.contrib.flatpages.urls')),

    # Comments
    (r'^comments/', include('django.contrib.comments.urls')),

    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/(.*)', admin.site.root),
)

from django.conf import settings
if settings.DEBUG:
    urlpatterns += patterns('',
	    # Images, Css, etc...
	    (r'site_media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': site_media }),
    )
