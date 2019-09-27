from django.urls import path
from . views import VideoListView, VideoThumbsView, VideoDetailView, VideoCreateView, VideoUpdateView,VideoDeleteView

urlpatterns = [
    path('list/', VideoListView.as_view(), name='videos-list'),
    path('thumbs/<int:category_id>', VideoThumbsView.as_view(), name='videos-thumbs'),
    path('detail/<int:pk>', VideoDetailView.as_view(), name='videos-detail'),
    path('create/', VideoCreateView.as_view(), name='videos-create'),
    path('update/<int:pk>', VideoUpdateView.as_view(), name='videos-update'),
    path('delete/<int:pk>', VideoDeleteView.as_view(), name='videos-delete'),
]

