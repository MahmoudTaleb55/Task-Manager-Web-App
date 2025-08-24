from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),  # Authentication URLs
    path('tasks/', include('tasks.urls')),  # Task management URLs
    path('', RedirectView.as_view(url='/accounts/login/', permanent=False)),  # Redirect to login
]
