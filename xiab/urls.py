from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin

from wagtail.admin import urls as wagtailadmin_urls
from wagtail.core import urls as wagtail_urls
from wagtail.documents import urls as wagtaildocs_urls

from xiab.search import views as search_views
from xiab.apps.users import views as user_views

urlpatterns = [
    url(r'^django-admin/', admin.site.urls),
    url(r'^admin/', include(wagtailadmin_urls)),
    url(r'^documents/', include(wagtaildocs_urls)),
    url(r'^search/$', search_views.search, name='search'),

    url(r'^profile/$', user_views.profile, name='profile'),
    url(r'^sign-up/$', user_views.register, name='sign-up'),
    url(r'^logout/$', user_views.user_logout, name='logout'),
    url(r'^login/$', user_views.user_login, name='login'),

    # For anything not caught by a more specific rule above, hand over to
    # Wagtail's page serving mechanism. This should be the last pattern in
    # the list:
    url(r'', include(wagtail_urls)),
]


if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    # Serve static and media files from development server
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
