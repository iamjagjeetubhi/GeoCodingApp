from django.conf.urls import include, url, handler404
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from accounts import views
from django.contrib.auth import views as auth_views
handler404 = 'accounts.views.index'

urlpatterns = [
  
	url(r'^password_reset/$', auth_views.password_reset, name='password_reset'),
    url(r'^password_reset/done/$', auth_views.password_reset_done, name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.password_reset_confirm, name='password_reset_confirm'),
    url(r'^reset/done/$', auth_views.password_reset_complete, name='password_reset_complete'),
    url(r'^$', views.index, name="indexview"),
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('accounts.urls')),
]

if settings.DEBUG is True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
