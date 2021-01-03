from django.urls import path
from .views import *
from.import views
from django.contrib.auth.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
path('main/add_song',CreatePostView.as_view(),name = 'add'),
path('main/',main,name = 'main'),
path('accounts/mycab',Lk,name = 'cabinet'),
path('accounts/mycab/edit/<int:pk>', OpisEdit.as_view(),name = 'cab_ed'),
path('main/viewuser/<int:user_id>/',viewuser,name = 'viewuser'),
path('main/<int:rub_id>',sort_by_g,name = 'genre'),
path('register/',reg_user,name = 'reg'),
path('<str:pk>/',PostEditView.as_view(),name = 'edit'),
path('main/delete/<str:pk>',PostDeleteView.as_view(),name = 'del'),
path('main/result',SearchResultsView.as_view(),name = 'search_results'),
path('accounts/mycab/add', CreateOpisView.as_view(), name = 'add_mycab')

]