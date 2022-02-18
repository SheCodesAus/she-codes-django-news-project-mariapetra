from django.urls import path
from . import views

app_name = 'news'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>', views.StoryView.as_view(), name='story'),
    path('<int:pk>/delete', views.DeleteStoryView.as_view(), name='delete'),
    path('<int:pk>/ammend', views.AmmendStoryView.as_view(), name='ammend'),
    path('add-story/', views.AddStoryView.as_view(), name='newStory'),
    path('category/', views.CategoryListView.as_view(), name='category'),
]


