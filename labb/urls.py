from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from django.urls import include, path, reverse_lazy

handler404 = 'pages.views.page_not_found'

handler500 = 'pages.views.server_error'

CSRF_FAILURE_VIEW = 'pages.views.csrf_failure'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('django.contrib.auth.urls')),
    path(
        'auth/registration/',
        CreateView.as_view(
            template_name='registration/registration_form.html',
            form_class=UserCreationForm,
            success_url=reverse_lazy('tours:index'),
        ),
        name='registration',
    ),
    path('', include('tours.urls', namespace='tours')),
    path('pages/', include('pages.urls', namespace='pages')),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
