from django.contrib import admin
from django.urls import path, include
import blogapp.views
import portfolio.views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blogapp.views.home, name="home"),
    path('blog/', include('blogapp.urls')),#blogapp안에있는 urls로부터 include해와라. 그리고 그 형식은 blog/로 하겠다.
    path('portfolio/', portfolio.views.portfolio, name="portfolio"),
    path('portfolio/new_portfolio/', portfolio.views.new_portfolio, name="new_portfolio"),
    path('portfolio/create_portfolio', portfolio.views.create_portfolio, name="create_portfolio"),
    path('accounts/', include('accounts.urls')),
] 

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
