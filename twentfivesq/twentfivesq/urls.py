"""twentfivesq URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
##from django.conf.urls import url
##from django.contrib import admin
##
##urlpatterns = [
##    url(r'^admin/', admin.site.urls),
##    
##]
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.views import login, logout
from twentfivesq import views
from manager import views as manager_views
from grid2 import views as grid2_views
from player import views as player_views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    #url(r'^accounts/login/$', login, {'template_name': 'admin/login.html'}),
    #url(r'^accounts/logout/$', logout),
    url(r'^&admin/', include(admin.site.urls)),
    url(r'[i]', views.Hmpage, name='Hmpage.html'),
    url(r'[yip]', views.Shome, name='Shome.html'),
    url(r'[G]', views.Grid_FB),
    url(r'[L]', player_views.enter, name = 'enter.html'),
    url(r'[uU]', manager_views.SignUp, name='SignUp'),
    url(r'[SO]', manager_views.Cat, name= 'SignOn'),
    url(r'[M]', manager_views.Dog, name='M'),
    url(r'[ZT]', manager_views.Rat, name = 'ZT'),
    url(r'[FF]', views.Gull, name = 'SS'),
    url(r'[PP]', views.Fish, name ='PP'),
    url(r'[R]', views.Ram, name ='R'),
    url(r'[D]', grid2_views.Trout, name = 'D'),
    url(r'[E]', grid2_views.Elephant, name = 'E'),
    url(r'[A]', views.More, name = 'A'),
    url(r'[C]', views.Contact, name = 'C'),
    url(r'[W]', grid2_views.Mammoth, name = 'EP'),
    url(r'[B]', grid2_views.Mastedon, name = 'Z'),
    url(r'[J]', views.Ghome, name = 'J'),
    url(r'[K]', grid2_views.Badger, name = 'K'),
    url(r'[V]', views.Archive, name = 'V'),
    url(r'[II]', grid2_views.TRex, name ='II'),
    url(r'[N]', views.Index, name = 'N'),
    url(r'[Q]', views.ArchiveM, name = 'Q'),
    url(r'[X]', manager_views.IndexR, name = 'X'),
    url(r'[Y]', views.Dash, name = 'Y'),
    url(r'[d]', views.Lemur, name = 'd'),
    url(r'[b]', manager_views.Kit, name = 'b'),
    url(r'[g]', grid2_views.Giraffe, name = 'g'),
    url(r'[o]', views.logout_view, name = 'o'),
    url(r'[q]', grid2_views.Petrodyl, name = 'd'),
    url(r'[sz]', manager_views.Enroll, name = 'sz'),
    url(r'[r]', manager_views.BuyGames, name = 'r'),
    url(r'[e]', views.Tomenus, name = 'e'),
    url(r'[h]', manager_views.Purchase, name = 'h'),
    url(r'[v]', grid2_views.Triceritops, name = 'v'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
