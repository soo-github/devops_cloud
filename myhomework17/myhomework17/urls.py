from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from books.views import bookstore_list, bookstore_detail

urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', bookstore_list),
    path('books/<int:pk>/', bookstore_detail),
]

urlpatterns += static(settings.MEDIA_URL,
                      documet_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]
