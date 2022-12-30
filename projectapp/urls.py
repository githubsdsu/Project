from django.contrib import admin
from django.urls import path,include

from projectapp import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('',views.login,name='login'),
    path('signup',views.signup,name='signup'),
    path('forgot',views.forgot,name='forgot'),
    path('otp',views.otp,name='otp'),
    path('update',views.update,name='update'),
    path('facescan',views.facescan,name='facescan'),
    path('result',views.result,name='result'),
    path('finalresult',views.finalresult,name='finalresult'),
    path('result_wrinkles',views.result_wrinkles,name='wrinkles'),
    path('result_puffyeyes',views.result_puffyeyes,name='puffyeyes'),
    path('result_darkspots',views.result_darkspots,name='darkspots'),
    path('history',views.history,name='history'),
    path('know_more_darkspots',views.know_darkspots,name='know_darkspots'),
    path('know_more_puffyeyes',views.know_puffyeyes,name='know_puffyeyes'),
    path('know_more_wrinkles',views.know_wrinkles,name='know_wrinkles')
]
if settings.DEBUG:  
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)  
