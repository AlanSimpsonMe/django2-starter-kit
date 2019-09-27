from django.shortcuts import render
from . models import Video
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin

# Create your views here.
class VideoListView(ListView):
    model = Video
    # Default assumes videos/templates/videos/video_list.html exists.
    # Show the video list in alphabetical order by title.
    queryset = Video.objects.order_by('title')

class VideoThumbsView(ListView):
    model = Video
    # Below we specify a different template for this ListView.
    template_name = "videos/video_thumbs.html"
    # Alternative to using object_list in the template loop.
    context_object_name = 'video_thumbs'

    # Here is how we filter records by category for the thumbnails view.
    def get_queryset(self):
        # Get only video records from requested category (category_id passed in from videos/urls.py)
        #return Video.objects.filter(category_id = self.kwargs['category_id'])
        return Video.objects.filter(category_id = self.kwargs['category_id']).filter(is_active = True)
        
class VideoDetailView(DetailView):
    model = Video
    # Default assumes videos/templates/videos/video_detail.html exists.

class VideoCreateView(SuccessMessageMixin,CreateView):
    model = Video
    fields = ['title', 'author', 'description', 'youtube_vid', 'stars_count', 'category_id', 'skill_level_id', 'is_active']
    # Default assumes videos/templates/videos/video_form.html exists.  
    # Send back to videolist on succesful save.
    success_message = "Video Added!"
    success_url = reverse_lazy('videos-list')    

class VideoUpdateView(SuccessMessageMixin,UpdateView):
    model = Video
    fields = ['title', 'author', 'description', 'youtube_vid', 'stars_count', 'category_id', 'skill_level_id', 'is_active']
    # Default assumes videos/templates/videos/video_form.html exists.
    # Send back to videolist on succesful save.
    success_message = "Video Saved!"
    success_url = reverse_lazy('videos-list')    

class VideoDeleteView(SuccessMessageMixin,DeleteView):
    model = Video
    # Default assumes videos/templates/videos/video_confirm_delete.html exists.
    # Send back to videolist on succesful save.
    success_message = "Video Deleted"
    success_url = reverse_lazy('videos-list')    