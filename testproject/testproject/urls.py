from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.conf.urls import url, include
from django.contrib.auth.models import User



# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^', include('snippets.urls')),

]